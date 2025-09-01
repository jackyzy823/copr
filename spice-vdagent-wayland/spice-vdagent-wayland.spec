Name:           spice-vdagent-wayland
Version:        0.22.1
Release:        %autorelease
Summary:        Agent for Spice guests with wayland ext-data-control support
License:        GPL-3.0-or-later
URL:            https://spice-space.org/
%global commit  93612d166ffe48a3a6921f8748d4824f01a60673
%global shortcommit %(c=%{commit}; echo ${c:0:7})
## branch style
# Source0:        https://gitlab.freedesktop.org/jackyzy823/vd_agent/-/archive/wayland-ext-data-control/vd_agent-wayland-ext-data-control.tar.gz
## commitish style
Source0:        https://gitlab.freedesktop.org/jackyzy823/vd_agent/-/archive/%{commit}/spice-vdagent-wayland-%{shortcommit}.tar.gz

BuildRequires: make
BuildRequires:  systemd-devel
BuildRequires:  glib2-devel >= 2.50
BuildRequires:  spice-protocol >= 0.14.3
BuildRequires:  libpciaccess-devel libXrandr-devel libXinerama-devel
BuildRequires:  libXfixes-devel systemd desktop-file-utils libtool
BuildRequires:  alsa-lib-devel dbus-devel libdrm-devel
# For autoreconf, needed after clipboard patch series
BuildRequires:  automake autoconf
%{?systemd_requires}

Conflicts:      spice-vdagent

BuildRequires:  wayland-protocols-devel >= 1.39
BuildRequires:  wayland-devel >= 1.23
## Runtime requirement 1) xwayland (XOpenDisplay) enabled for spice-vdagent running.
# 2) compositors supports ext-data-control protocol
# https://wayland.app/protocols/ext-data-control-v1#compositor-support
# for KDE: kwin >= 6.4
# sway >= 1.11 niri >= 25.08 jay >= 1.11.0 Treeland >= 0.6.1
# other compositors using wlr-ext-data-control protocl will be supported when they converting to ext-data-control protocol.

%description
Spice agent for Linux guests offering the following features:

Features:
* Client mouse mode (no need to grab mouse by client, no mouse lag)
  this is handled by the daemon by feeding mouse events into the kernel
  via uinput. This will only work if the active X-session is running a
  spice-vdagent process so that its resolution can be determined.
* Automatic adjustment of the X-session resolution to the client resolution
* Support of copy and paste (text and images) between the active X-session
  and the client


%prep
# autosetup -p1
## commitish style
%autosetup -p1 -n vd_agent-%{commit}
autoreconf -fi


%build
%configure --with-session-info=systemd --with-init-script=systemd
%make_build V=2


%install
%make_install V=2


%post
%systemd_post spice-vdagentd.service spice-vdagentd.socket

%preun
%systemd_preun spice-vdagentd.service spice-vdagentd.socket

%postun
%systemd_postun_with_restart spice-vdagentd.service spice-vdagentd.socket


%files
%doc COPYING CHANGELOG.md README.md
/usr/lib/udev/rules.d/70-spice-vdagentd.rules
%{_unitdir}/spice-vdagentd.service
%{_unitdir}/spice-vdagentd.socket
%{_prefix}/lib/tmpfiles.d/spice-vdagentd.conf
%{_userunitdir}/spice-vdagent.service
%{_bindir}/spice-vdagent
%{_sbindir}/spice-vdagentd
%{_sysconfdir}/xdg/autostart/spice-vdagent.desktop
# For /usr/share/gdm/autostart/LoginWindow/spice-vdagent.desktop
# We own the dir too, otherwise we must Require gdm
%{_datadir}/gdm
%{_mandir}/man1/spice-vdagent*.1*


%changelog
%autochangelog
