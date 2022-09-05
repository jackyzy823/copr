Name:    plasma-breath
Version: 21.3.0
Release: %autorelease
Summary: Artwork, styles and assets for the Breath visual style for the Plasma Desktop
License: LGPL AND CC-BY-SA-4.0

%undefine __cmake_in_source_build

%global         base_name   breath
%global         commit      3130eb1addeebb4b93f1192c377383618ebecaa3

URL:     https://gitlab.manjaro.org/artwork/themes/%{base_name}

Source0: https://gitlab.manjaro.org/artwork/themes/%{base_name}/-/archive/%{commit}/%{base_name}-%{commit}.tar.bz2
Source1: https://pagure.io/fedora-logos/raw/03c2476f35008c66fa269b8c04828c8ffe168df3/f/fedora/fedora_logo_darkbackground.svg

Patch: change-splash-logo.patch

BuildRequires:  extra-cmake-modules
BuildRequires:  plasma-workspace
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-rpm-macros

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n %{base_name}-%{commit} -p1
rm lnf/breath/contents/splash/images/manjarologo.svgz
rm lnf/breath-dark/contents/splash/images/manjarologo.svgz
cp %{SOURCE1} lnf/breath/contents/splash/images/
cp %{SOURCE1} lnf/breath-dark/contents/splash/images/


%build
%cmake_kf5 -DBUILD_SDDM_THEME=on -DBUILD_PLASMA_THEMES=on -DBUILD_EXTRA_COLORS=on

%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_kf5_datadir}/color-schemes/*.colors
%{_kf5_datadir}/konsole/*.colorscheme
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_datadir}/metainfo/*.appdata.xml

%{_kf5_datadir}/plasma/
%{_kf5_datadir}/sddm/
%{_kf5_datadir}/wallpapers/
%{_kf5_datadir}/yakuake/

%changelog
%autochangelog
