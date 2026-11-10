Name:           FakeSIP
Version:        0.9.1
Release:        %autorelease
Summary:        Disguise your UDP traffic as SIP protocol to evade DPI detection, using Netfilter Queue (NFQUEUE)

License:        GPL-3.0-or-later
URL:            https://github.com/MikeWang000000/FakeSIP
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
# it will call nft/iptables, so suid %attr(4755, root, root) %{_bindir}/%{name} or setcap in %post or %caps(cap_net_raw, cap_net_admin=ep) won't help. must run under root.
%{_bindir}/%{lower:%{name}}



%changelog
%autochangelog

