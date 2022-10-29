Name:    amd-disable-c6
Version: 0
Release: 1%{?dist}
Summary: Systemd service to automatically disable/enable the C6 power saving state on AMD Zen (Ryzen / Epyc) processors.
License: MIT

%global         author      joakimkistowski
%global         base_name   amd-disable-c6
%global         commit      4eb03b5ae7c51ead162481cab4163ae3ed4a6c29
%global         shortcommit %(c=%{commit};echo ${c:0:7})

%global         enable_c6_serivce amd-enable-c6
%global         disable_c6_service %{base_name}

%global debug_package %{nil}

URL:     https://github.com/%{author}/%{base_name}
Source0: https://github.com/%{author}/%{base_name}/archive/%{commit}/%{base_name}-%{shortcommit}.tar.gz
Source1: %{enable_c6_serivce}.service

Patch: custom.patch

BuildRequires: gcc-c++
BuildRequires: systemd-rpm-macros

BuildRequires: libstdc++-static
BuildRequires: glibc-static

BuildArch: x86_64

Requires: systemd

%prep
%autosetup -n %{base_name}-%{commit} -p1
cp %{SOURCE1} .

%build
make %{?_smp_mflags}

%install
%make_install


%files
%{_sbindir}/%{base_name}
%{_unitdir}/%{enable_c6_serivce}.service
%{_unitdir}/%{disable_c6_service}.service

# Systemd scriptlet
%post
%systemd_post %{enable_c6_serivce}.service
%systemd_post %{disable_c6_service}.service

%preun
%systemd_preun %{enable_c6_serivce}.service
%systemd_preun %{disable_c6_service}.service

%postun
%systemd_postun %{enable_c6_serivce}.service
%systemd_postun %{disable_c6_service}.service

%description
This is a systemd service to automatically disable (after boot/resume)/enable (before sleep) the C6 power saving state on AMD Zen (Ryzen / Epyc) processors as a workaround for Ryzen's freeze/random reboot bug.

%changelog
%autochangelog
