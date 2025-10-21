%global _version    0.8.19
%global _buildtype  release-debug

Name:           dlangide
Version:        %{gsub %{_version} - ~}
Release:        %autorelease
Summary:        D language IDE based on DlangUI

License:        BSL-1.0
URL:            https://github.com/buggins/%{name}

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
Source1:	%{name}.desktop

## todo save packages to like /usr/share/dub/packages/xxxx.zip like rust
## use generate_requres -> read dub.selections.json and --> create something like dub(xxxx)

# dub build --registry=file://<> --skip-registery=.....

## from dub.selections.json
Source:         %{dub_source arsd-official 10.9.10}
Source:         %{dub_source bindbc-common 0.1.6}
Source:         %{dub_source bindbc-freetype 1.2.6}
Source:         %{dub_source bindbc-loader 1.1.5}
Source:         %{dub_source bindbc-opengl 1.1.1}
Source:         %{dub_source bindbc-sdl 1.4.8}
Source:         %{dub_source dcd 0.16.0-beta.3}
Source:         %{dub_source dlangui 0.10.8}
Source:         %{dub_source dsfml 2.1.1}
Source:         %{dub_source emsi_containers 0.9.0}
Source:         %{dub_source glx-d 1.1.0}
Source:         %{dub_source icontheme 1.2.3}
Source:         %{dub_source inilike 1.2.3}
Source:         %{dub_source isfreedesktop 0.1.1}
Source:         %{dub_source libdparse 0.25.0}
Source:         %{dub_source msgpack-d 1.0.5}
Source:         %{dub_source x11 1.0.21}
Source:         %{dub_source xdgpaths 0.2.5}

BuildRequires:  dub
BuildRequires:  ldc
# https://github.com/buggins/dlangide?tab=readme-ov-file#linux-build-notes
BuildRequires:  SDL2-devel
# TODO change to pkgconfig(sdl2)
#BuildRequires:  pkgconfig(sdl2)
## built failed due to without lz when linking
BuildRequires:  pkgconfig(zlib)

BuildRequires:	desktop-file-utils

# TODO alternative config like : minimal, console, x11 (and split to multi packages?)

## BUG: resource document-new not found , this is a bug of dlangide (lack of document-new.png)

## runtime error: bindbc-freetype requires freetype shared library
## bindbc-freetype will find libfreetype.so (which is in devel, libfreetype.so.6 in normal package)
Requires:	freetype-devel

Recommends:	ldc
Recommends:	dub

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
-- we have desktop file so skip one more
    if p > 1 then
        print(rpm.expand('cp ' .. sources[i] .. ' %{_buildrootdir}/packages\n'))
    end
end
}

# dcd's dubhash is located in common/ folder, so when building, DUB_PACKAGING_DIR will be dcd-version/common (since it is a dcb:common package) so , the dir.dirName is dcd-version. Situation is not the same as d-scanner, dfmt , their dubhash is located under root folder, so -C -n %{_version}/%{name}-%{_version} is a must. (-C strip root under archive file, -n create with nested folder)
## use <version>/<packgename>-<version> for all dubhash versioing d pacakge.
%setup -C -n %{_version}/%{name}-%{_version}

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
install -Dpm0755 -t %{buildroot}%{_bindir} bin/%{name}
## or
#install -m 0755 -vd %{buildroot}%{_bindir}
#install -m 0755 -vp %{name} %{buildroot}%{_bindir}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
install -Dpm0644 views/res/mdpi/dlangui-logo1.png %{buildroot}%{_datadir}/pixmaps/%{name}.png



%check

%files
%license LICENSE.txt
%doc    README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
%autochangelog

