Name:    amd-disable-c6
Version: 0
Release: 4%{?dist}
Summary: Systemd service to automatically disable the C6 power saving state on AMD Zen (Ryzen / Epyc) processors.
License: MIT

%global         author      joakimkistowski
%global         base_name   amd-disable-c6
%global         commit      4eb03b5ae7c51ead162481cab4163ae3ed4a6c29
%global         shortcommit %(c=%{commit};echo ${c:0:7})

%global debug_package %{nil}

URL:     https://github.com/%{author}/%{base_name}
Source0: https://github.com/%{author}/%{base_name}/archive/%{commit}/%{base_name}-%{shortcommit}.tar.gz

Patch: custom.patch
Patch: fix-mixed-value-with-return-code.patch

BuildRequires: gcc-c++
BuildRequires: systemd-rpm-macros

BuildRequires: libstdc++-static
BuildRequires: glibc-static

BuildArch: x86_64

Requires: systemd

%prep
%autosetup -n %{base_name}-%{commit} -p1

%build
make %{?_smp_mflags}

%install
%make_install


%files
%{_sbindir}/%{base_name}
%{_unitdir}/%{base_name}.service

# Systemd scriptlet
%post
%systemd_post %{base_name}.service

%preun
%systemd_preun %{base_name}.service

%postun
%systemd_postun %{base_name}.service

%description
This is a systemd service to automatically disable (after boot/resume) the C6 power saving state on AMD Zen (Ryzen / Epyc) processors as a workaround for Ryzen's freeze/random reboot bug.

%changelog
%autochangelog
