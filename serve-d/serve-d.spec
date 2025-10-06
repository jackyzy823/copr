# debug info seem not works with D compiler
# from https://src.fedoraproject.org/rpms/gtkd
## TO include debug info , use --build=release-debug
## see https://dub.pm/dub-reference/build_settings/#buildoptions
## and https://dub.pm/dub-reference/buildtypes/#-buildrelease-debug
#%global debug_package %{nil}

%global _version    0.8.0-beta.18
%global _buildtype  release-debug

Name:           serve-d
Version:        %{gsub %{_version} - ~}
Release:        %autorelease
Summary:        Microsoft Language Server Protocol library and D Server

License:        MIT
URL:            https://github.com/Pure-D/serve-d

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
Source:         %{dub_source automem 0.6.10}
Source:         %{dub_source botan 1.12.19}
Source:         %{dub_source botan-math 1.0.3}
Source:         %{dub_source cachetools 0.4.1}
Source:         %{dub_source dcd 0.16.0-beta.2}
Source:         %{dub_source dfmt 0.15.1}
Source:         %{dub_source diet-complete 0.0.3}
Source:         %{dub_source diet-ng 1.8.1}
Source:         %{dub_source dscanner 0.16.0-beta.4}
Source:         %{dub_source dub 1.38.0-beta.1}
Source:         %{dub_source emsi_containers 0.9.0}
Source:         %{dub_source eventcore 0.9.30}
Source:         %{dub_source fuzzymatch 1.0.0}
Source:         %{dub_source inifiled 1.3.3}
Source:         %{dub_source isfreedesktop 0.1.1}
Source:         %{dub_source libasync 0.8.6}
Source:         %{dub_source libddoc 0.8.0}
Source:         %{dub_source libdparse 0.23.2}
Source:         %{dub_source memutils 1.0.10}
Source:         %{dub_source mir-algorithm 3.22.1}
Source:         %{dub_source mir-core 1.7.1}
Source:         %{dub_source mir-cpuid 1.2.11}
Source:         %{dub_source mir-ion 2.3.2}
Source:         %{dub_source mir-linux-kernel 1.0.1}
Source:         %{dub_source msgpack-d 1.0.5}
Source:         %{dub_source openssl 3.3.3}
Source:         %{dub_source openssl-static 1.0.5+3.0.8}
Source:         %{dub_source requests 2.1.3}
Source:         %{dub_source rm-rf 0.1.0}
Source:         %{dub_source sdlfmt 0.1.1}
Source:         %{dub_source sdlite 1.1.2}
Source:         %{dub_source silly 1.1.1}
Source:         %{dub_source standardpaths 0.8.2}
Source:         %{dub_source stdx-allocator 2.77.5}
Source:         %{dub_source taggedalgebraic 0.11.23}
Source:         %{dub_source test_allocator 0.3.4}
Source:         %{dub_source unit-threaded 0.10.8}
Source:         %{dub_source vibe-container 1.3.1}
Source:         %{dub_source vibe-core 2.8.4}
Source:         %{dub_source vibe-d 0.9.8}
Source:         %{dub_source xdgpaths 0.2.5}


BuildRequires:  dub
BuildRequires:  ldc


# requires dcd-server to complete code
#Recommends:     dcd-server
# Note since serve-d internal dcd-client only supports dcd server from [0.8.0,0.14.0), so we recommends dcd-client too
#Recommends:     dcd-client
## so we use dcd meta-package
Recommends:     dcd
## Good to have a compiler
Recommends:     ldc


%global _description %{expand:
Microsoft language server protocol implementation for D.

The purpose of this project is to give every editor the same capabilities and editing features as code-d through the widely available Microsoft Language Server Protocol (LSP).
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

%setup -n %{name}-%{_version}

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
install -Dpm0755 -t %{buildroot}%{_bindir} %{name}
## or
#install -m 0755 -vd %{buildroot}%{_bindir}
#install -m 0755 -vp %{name} %{buildroot}%{_bindir}


%check
dub --skip-registry=all --registry=file://%{_buildrootdir}/packages --cache local test --parallel  --compiler=ldc2 --build=%{_buildtype}

%files
%license LICENSE
%doc    README.md editor-*.md
%{_bindir}/%{name}


%changelog
%autochangelog

