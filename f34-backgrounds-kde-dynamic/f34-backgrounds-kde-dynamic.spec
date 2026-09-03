%global relnum 34
%global Bg_Name F34
%global bgname %(t="%{Bg_Name}";echo ${t,,})

%global sourcename %{bgname}-backgrounds
Name:		%{bgname}-backgrounds-kde-dynamic
Version:	%{relnum}.0.1
Release:	%autorelease
Summary:	Fedora  %{relnum} default wallpaper for KDE with dynamic

License:	CC-BY-SA-4.0
URL:		https://fedoraproject.org/wiki/_Artwork
Source0:	https://github.com/fedoradesign/backgrounds/releases/download/v%{version}/%{sourcename}-%{version}.tar.xz
Source1:    f34-metadata.json

Patch0:     Makefile.diff
BuildArch:	noarch

# make is no longer part of buildroot from the build system
# https://fedoraproject.org/wiki/Changes/Remove_make_from_BuildRoot
BuildRequires:	make

Conflicts:	%{name}-kde = %{version}
Requires:	kde-filesystem
Requires:	 %{sourcename}-base = %{version}

%description
This package contains desktop backgrounds for the Fedora  %{relnum} default
theme.  Pulls in themes for GNOME, KDE, Mate and Xfce desktops.


%prep
%autosetup -n %{sourcename} -p1
cp %{SOURCE1} default


%build
%make_build


%install
(cd default && %make_install)

%files
%doc
%{_datadir}/wallpapers/%{Bg_Name}/

%changelog
%autochangelog
