# debug info seem not works with D compiler
# from https://src.fedoraproject.org/rpms/gtkd
## TO include debug info , use --build=release-debug
## see https://dub.pm/dub-reference/build_settings/#buildoptions
## and https://dub.pm/dub-reference/buildtypes/#-buildrelease-debug
#%global debug_package %{nil}

%global _version    0.16.0-beta.3
%global _buildtype  release-debug

Name:           dcd
Version:        %{gsub %{_version} - ~}
Release:        %autorelease
Summary:        The D Completion Daemon is an auto-complete program for the D programming language

License:        GPL-3.0-or-later
URL:            https://github.com/dlang-community/DCD

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

## todo save packges to like /usr/share/dub/packages/xxxx.zip like rust
## use generate_requres -> read dub.selections.json and --> create something like dub(xxxx)

# dub build --registry=file://<> --skip-registery=.....

## from dub.selections.json
Source:         %{dub_source dsymbol 0.14.1}
Source:         %{dub_source emsi_containers 0.9.0}
Source:         %{dub_source libdparse 0.25.0}
Source:         %{dub_source msgpack-d 1.0.5}
Source:         %{dub_source stdx-allocator 2.77.5}


BuildRequires:  dub
BuildRequires:  ldc


%global _description %{expand:
DCD consists of a client and a server. The client (dcd-client) is almost always used through a text editor script or plugin, though it can be used from the command line. The server (dcd-server) is responsible for caching imported files, calculating autocomplete information, and sending it back to the client.
}

%description %_description

%package -n %{name}-client
Summary:    %{summary}
License:        GPL-3.0-or-later

%description -n %{name}-client %{expand:
The client (dcd-client) is almost always used through a text editor script or plugin, though it can be used from the command line.
}

%files -n %{name}-client
%license
%doc
%{_bindir}/%{name}-client


%package -n %{name}-server
Summary:    %{summary}
License:        GPL-3.0-or-later

%description -n %{name}-server %{expand:
The server (dcd-server) is responsible for caching imported files, calculating autocomplete information, and sending it back to the client.
}

%files -n %{name}-server
%license
%doc
%{_bindir}/%{name}-server

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
dub --skip-registry=all --registry=file://%{_buildrootdir}/packages --cache local build --parallel -f -n --compiler=ldc2 --build=%{_buildtype} --config=server
dub --skip-registry=all --registry=file://%{_buildrootdir}/packages --cache local build --parallel -f -n --compiler=ldc2 --build=%{_buildtype} --config=client


%install
install -Dpm0755 -t %{buildroot}%{_bindir} %{name}-client
install -Dpm0755 -t %{buildroot}%{_bindir} %{name}-server
## or
#install -m 0755 -vd %{buildroot}%{_bindir}
#install -m 0755 -vp %{name} %{buildroot}%{_bindir}


%check
# no tests

%changelog
%autochangelog

