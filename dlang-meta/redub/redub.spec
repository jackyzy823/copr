%global _version    1.25.4
%global _buildtype  release-debug

Name:           redub
Version:        %{gsub %{_version} - ~}
Release:        %autorelease
Summary:        Redub is a Dub Based Build System.

License:        MIT
URL:            https://github.com/MrcSnm/redub

ExclusiveArch:  %{ldc_arches}

# Reference:    https://github.com/dlang/dub/blob/0030b9af02481fb518419bb4e13dd18731a9fd4f/source/dub/packagesuppliers/registry.d#L65
# or https://codemirror.dlang.org
%define __dub_url https://code.dlang.org/packages/
%define dub_source() %{lua:
    local package = rpm.expand('%1')
    local version = rpm.expand('%2')
    local url = rpm.expand('%__dub_url')
    -- first argument missing
    if package == '%1' then
        package = rpm.expand('%name')
    end
    if version == '%2' then
        version = rpm.expand('%version')
    end
    -- replace '~' with '-' for backwards compatibility
    version = version:gsub('~', '-')
    print(url .. package .. '/' .. version .. '.zip#/' .. package .. '-' .. version .. '.zip')
}

Source0:        %{dub_source %name %version}

## todo save packages to like /usr/share/dub/packages/xxxx.zip like rust
## use generate_requres -> read dub.selections.json and --> create something like dub(xxxx)

# dub build --registry=file://<> --skip-registery=.....

## from dub.selections.json
Source:         %{dub_source d-segmented-hashmap 1.0.5}
Source:         %{dub_source arsd-official 12.0.0}
Source:         %{dub_source sdlite 1.3.3}
Source:         %{dub_source taggedalgebraic 1.0.1}
Source:         %{dub_source fswatch 0.6.1}
Source:         %{dub_source xxhash3 0.0.5}

Patch0:         disable-update.patch

BuildRequires:  dub
BuildRequires:  ldc


%global _description %{expand:
%{summary}
}

%description %_description

%prep
## RPM lua's global value `sources` `source_nums` `patches` `patch_nums`
## Reference: https://rpm-software-management.github.io/rpm/man/rpm-lua.7#SPEC_FILES
## use FileSystemProvider 
## Reference: https://github.com/dlang/dub/pull/1616
## https://github.com/dlang/dub/blob/0030b9af02481fb518419bb4e13dd18731a9fd4f/source/dub/dub.d#L111
## https://github.com/dlang/dub/blob/0030b9af02481fb518419bb4e13dd18731a9fd4f/source/dub/packagesuppliers/filesystem.d
## This package supplier searches a certain directory for files with names of the form "[package name]-[version].zip".
## Dont try to mimic ~/.dub/packages , since dub fetch will modify package dub.json/dub.sdl here by adding version field and converting dub.sdl to dub.json
## TODO: Make this a helper for all D lang libraries
%{lua:
print(rpm.expand('mkdir %{_buildrootdir}/packages \n'))

for i, p in ipairs(source_nums) do
    if p ~= 0 then
        print(rpm.expand('cp ' .. sources[i] .. ' %{_buildrootdir}/packages\n'))
    end
end
}

# dcd's dubhash is located in common/ folder, so when building, DUB_PACKAGING_DIR will be dcd-version/common (since it is a dcb:common package) so , the dir.dirName is dcd-version. Situation is not the same as d-scanner, dfmt , their dubhash is located under root folder, so -C -n %{_version}/%{name}-%{_version} is a must. (-C strip root under archive file, -n create with nested folder)
## use <version>/<packgename>-<version> for all dubhash versioing d pacakge.
%autosetup -C -n %{_version}/%{name}-%{_version} -p1
## see: https://github.com/dlang/dub/issues/3077
rm dub.selections.json

#TODO make this a %{dub_build} with --skip-registry=all --registry=file://%{_buildrootdir}/packages
%build
## -f force rebuild
## -n non-interactive
## --arch
## --cache local -> set to <current path>/.dub   user -> set to ~/.dub system /var/lib/dub/ see also $DUB_HOME
## --parallel
## TODO
## --deep (for target=static_libary to build all)
## --combined (will fail)
## --nodeps (will fail)
## --build-mode=separate (default), allAtOnce, singleFile
dub --skip-registry=all --registry=file://%{_buildrootdir}/packages --cache local build --parallel -f -n --compiler=ldc2 --build=%{_buildtype}


%install
install -Dpm0755 -t %{buildroot}%{_bindir} build/%{name}
## or
#install -m 0755 -vd %{buildroot}%{_bindir}
#install -m 0755 -vp %{name} %{buildroot}%{_bindir}


%check
#unit test
dub --skip-registry=all --registry=file://%{_buildrootdir}/packages --cache local test --parallel  --compiler=ldc2 --build=%{_buildtype}

%files
%license LICENSE
%doc    README.md
%{_bindir}/%{name}


%changelog
%autochangelog

