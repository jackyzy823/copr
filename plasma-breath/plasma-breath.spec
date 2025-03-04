Name:    plasma-breath
Version: 24.0.0
Release: 2%{?dist}
Summary: Artwork, styles and assets for the Breath visual style for the Plasma Desktop
License: LGPL AND CC-BY-SA-4.0

%undefine __cmake_in_source_build

%global         base_name   breath
%global         commit      1b708941f52be6f36ed61635659ad1d26c5719d7

URL:     https://gitlab.manjaro.org/artwork/themes/%{base_name}

Source0: https://gitlab.manjaro.org/artwork/themes/%{base_name}/-/archive/%{commit}/%{base_name}-%{commit}.tar.bz2
Source1: https://pagure.io/fedora-logos/raw/03c2476f35008c66fa269b8c04828c8ffe168df3/f/fedora/fedora_logo_darkbackground.svg

# Sync with upstream plasma-desktop's sddm-theme (already done by manjaro team)
Patch0: https://gitlab.manjaro.org/artwork/themes/breath/-/commit/0266802cdbe62a9f18c9fdb9630732d60e49fa90.patch
# Update icon and prevent upgrade conflicts caused by /usr/share/sddm/themes/breath/components is now a file instead of folder
Patch1: breath-logo-and-fix.patch

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-plasma-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(Qt6)

BuildArch:      noarch

Obsoletes:      plasma5-breath <= 22.0.0

%description
%{summary}.

%prep
%autosetup -n %{base_name}-%{commit} -p1
rm lnf/breath/contents/splash/images/manjarologo.svgz
rm lnf/breath-dark/contents/splash/images/manjarologo.svgz
rm sddm-theme/manjarologo.svgz
cp %{SOURCE1} lnf/breath/contents/splash/images/
cp %{SOURCE1} lnf/breath-dark/contents/splash/images/
cp %{SOURCE1} sddm-theme/


%build
%cmake_kf6 -DBUILD_SDDM_THEME=on -DBUILD_PLASMA_THEMES=on -DBUILD_EXTRA_COLORS=on

%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_kf6_datadir}/color-schemes/*.colors
%{_kf6_datadir}/konsole/*.colorscheme
%{_kf6_datadir}/metainfo/*.appdata.xml

%{_kf6_datadir}/plasma/
%{_kf6_datadir}/sddm/
%{_kf6_datadir}/wallpapers/
%{_kf6_datadir}/yakuake/

## /usr/share/sddm/themes/breath/components is now a file instead of folder
## https://stackoverflow.com/questions/56668136/rpm-upgrade-cant-replace-directory-with-file
## https://docs.fedoraproject.org/en-US/packaging-guidelines/Directory_Replacement/
## https://bugzilla.redhat.com/show_bug.cgi?id=447156
## https://bugzilla.redhat.com/show_bug.cgi?id=739318
## So is sddm/themes/breath/components necessary? if not we could delete it in 1) patch (exclude it in CMakeLists.txt) 2) %prep
## so we choose 1) do the same as upstream exclude "components" in CMakeLists.txt
## Also it should be a symlink just like its upstream https://invent.kde.org/plasma/plasma-desktop/-/blob/master/sddm-theme/component but it became a normal file.
#%pretrans
#if [ $1 = 0 ]; then
#	# workaround rpm bug (replacing directory with file fails)
#	[ -d %{_kf6_datadir}/sddm/themes/breath/components ] && rm -rf %{_kf6_datadir}/sddm/themes/breath/components
#	exit 0
#fi


%changelog
%autochangelog
