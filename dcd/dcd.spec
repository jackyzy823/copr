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

## todo save packages to like /usr/share/dub/packages/xxxx.zip like rust
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

# must before description to become meta-package's requires
Requires:   %{name}-client = %{version}-%{release}
Requires:   %{name}-server = %{version}-%{release}


%global _description %{expand:
DCD consists of a client and a server. The client (dcd-client) is almost always used through a text editor script or plugin, though it can be used from the command line. The server (dcd-server) is responsible for caching imported files, calculating autocomplete information, and sending it back to the client.
}

%description %_description

%files
## placeholder to create meta-package

%package client
Summary:    %{summary}
License:        GPL-3.0-or-later

%description client %{expand:
The client (dcd-client) is almost always used through a text editor script or plugin, though it can be used from the command line.
}

%files client
%license License.txt
%doc README.md CHANGELOG.md
%{_bindir}/%{name}-client
## man file will be compressed to .gz
%{_mandir}/man1/%{name}-client.1*
%{bash_completions_dir}/%{name}-client

%package server
Summary:    %{summary}
License:        GPL-3.0-or-later

%description server %{expand:
The server (dcd-server) is responsible for caching imported files, calculating autocomplete information, and sending it back to the client.
}

%files server
%license License.txt
%doc README.md CHANGELOG.md
%{_bindir}/%{name}-server
## man file will be compressed to .gz
%{_mandir}/man1/%{name}-server.1*
%{bash_completions_dir}/%{name}-server

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

%setup -n %{upper %{name}}-%{_version}

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

## note dcd's versioncode is generated by common/dub.sdl -> preBuildCommands -> write to bin/dubhash.txt , if it isn't a git repo, then version is vDCD-<version_in_folder_name> and this will make serve-d unhappy if you use serve-d internal dcd client see `orDubFetchFallback`
dub --skip-registry=all --registry=file://%{_buildrootdir}/packages --cache local build --parallel -f -n --compiler=ldc2 --build=%{_buildtype} --config=server
dub --skip-registry=all --registry=file://%{_buildrootdir}/packages --cache local build --parallel -f -n --compiler=ldc2 --build=%{_buildtype} --config=client


%install
install -Dpm0755 -t %{buildroot}%{_bindir} bin/%{name}-client
install -Dpm0755 -t %{buildroot}%{_bindir} bin/%{name}-server
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 man1/%{name}-client.1
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 man1/%{name}-server.1
install -Dpm0644 -t %{buildroot}%{bash_completions_dir} bash-completion/completions/%{name}-client
install -Dpm0644 -t %{buildroot}%{bash_completions_dir} bash-completion/completions/%{name}-server
## or
#install -m 0755 -vd %{buildroot}%{_bindir}
#install -m 0755 -vp %{name} %{buildroot}%{_bindir}


%check
pushd tests
## set DC to run: tests/extra/tc_ufcs_all_kinds/run.sh
DC=ldc2 ./run_tests.sh --extra
popd

%changelog
%autochangelog

