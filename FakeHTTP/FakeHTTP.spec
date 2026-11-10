Name:           FakeHTTP
Version:        0.9.18
Release:        %autorelease
Summary:        Obfuscate all your TCP connections into HTTP protocol.

License:        GPL-3.0-or-later
URL:            https://github.com/MikeWang000000/FakeHTTP
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  pkgconfig(libnetfilter_queue)

%description
%{summary}.

%prep
%autosetup
# To create debugsource
sed -i '/$(STRIP)/d' Makefile

%build
%make_build


%install
%make_install PREFIX=%{_prefix}



%files
%license LICENSE
%doc README.md
%{_bindir}/%{lower:%{name}}



%changelog
%autochangelog

