%global _buildtype  release-debug

Name:           dexed
Version:        3.9.26
Release:        %autorelease
Summary:        Dexed, the D Extended EDitor, is an IDE for the D programming language, its compilers, tools and libraries.

License:        BSL-1.0
URL:            https://gitlab.com/basile.b/%{name}

ExclusiveArch:  %{ldc_arches}

Source0:        https://gitlab.com/basile.b/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:        %{name}.desktop

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


## todo save packages to like /usr/share/dub/packages/xxxx.zip like rust
## use generate_requres -> read dub.selections.json and --> create something like dub(xxxx)

# dub build --registry=file://<> --skip-registery=.....

## from dub.selections.json
Source:         %{dub_source libdparse 0.23.2}
Source:         %{dub_source stdx-allocator 2.77.5}

# 1. dont use libdparse from submodule 2) don't static link druntime 3) don't built libdexed-d again in pas project file
Patch0:         fix_build.patch

BuildRequires:  dub
BuildRequires:  ldc

BuildRequires: lazarus-tools
BuildRequires: lazarus-lcl-gtk2

BuildRequires:  pkgconfig(zlib)
BuildRequires:	desktop-file-utils

Recommends:     dub
Recommends:     ldc
Recommends:     dcd
Recommends:     dscanner

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
-- we have desktop file
    if p > 1 then
        print(rpm.expand('cp ' .. sources[i] .. ' %{_buildrootdir}/packages\n'))
    end
end
}

%autosetup -n %{name}-v%{version} -p1

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
pushd dexed-d
dub --skip-registry=all --registry=file://%{_buildrootdir}/packages --cache local build --parallel -f -n --compiler=ldc2 --build=%{_buildtype}
popd
pushd lazproj
lazbuild -B dexeddesigncontrols.lpk
lazbuild -B dexed.lpi
popd


%install
install -Dpm0755 -t %{buildroot}%{_bindir} bin/%{name}
install -Dpm0755 -t %{buildroot}%{_libdir} bin/lib%{name}-d.so
## or
#install -m 0755 -vd %{buildroot}%{_bindir}
#install -m 0755 -vp %{name} %{buildroot}%{_bindir}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
install -Dpm0644 logo/dexed256.png %{buildroot}%{_datadir}/pixmaps/%{name}.png


%check

%files
%license LICENSE_1_0.txt
%doc    README.md
%{_bindir}/%{name}
%{_libdir}/lib%{name}-d.so
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png


%changelog
%autochangelog

