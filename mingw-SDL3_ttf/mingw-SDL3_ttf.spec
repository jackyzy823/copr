%?mingw_package_header

Name:           mingw-SDL3_ttf
License:        Zlib AND MIT

Version:        3.2.2
Release:        1%{?dist}

%global  pkg_summary  MinGW Windows port of the TrueType font handling library for SDL3
Summary: %{pkg_summary}

URL:            https://www.libSDL.org/projects/SDL_ttf/
Source0:        %{URL}release/SDL3_ttf-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  dos2unix

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-harfbuzz
BuildRequires:  mingw32-SDL3

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-harfbuzz
BuildRequires:  mingw64-SDL3


%global  pkg_description  Simple DirectMedia Layer (SDL3) is a cross-platform multimedia library \
designed to provide fast access to the graphics frame buffer and audio device. \
This package contains a library that allows you to use TrueType fonts \
to render text in SDL3 applications.

%description
%{pkg_description}


# Win32
%package -n mingw32-SDL3_ttf
Summary: %{pkg_summary}

%description -n mingw32-SDL3_ttf
%{pkg_description}

# Win32 (static)
%package -n mingw32-SDL3_ttf-static
Summary: %{pkg_summary}

Requires:  mingw32-SDL3_ttf = %{version}-%{release}
Requires:  mingw32-freetype-static
Requires:  mingw32-harfbuzz-static
Requires:  mingw32-SDL3-static

%description -n mingw32-SDL3_ttf-static
%{pkg_description}

# Win64
%package -n mingw64-SDL3_ttf
Summary: %{pkg_summary}

%description -n mingw64-SDL3_ttf
%{pkg_description}

# Win64 (static)
%package -n mingw64-SDL3_ttf-static
Summary: %{pkg_summary}

Requires:  mingw64-SDL3_ttf = %{version}-%{release}
Requires:  mingw64-freetype-static
Requires:  mingw64-harfbuzz-static
Requires:  mingw64-SDL3-static

%description -n mingw64-SDL3_ttf-static
%{pkg_description}

%?mingw_debug_package


%prep
%autosetup -n SDL3_ttf-%{version} -p1
	
dos2unix CHANGES.txt README.md


%build
export MINGW_BUILDDIR_SUFFIX=shared
%mingw_cmake \
    -DSDLTTF_HARFBUZZ:BOOL=ON \
    -DSDLTTF_INSTALL:BOOL=ON \
    -DSDLTTF_INSTALL_CPACK:BOOL=OFF \
    -DSDLTTF_INSTALL_MAN:BOOL=OFF \
    -DSDLTTF_PLUTOSVG:BOOL=OFF \
    -DSDLTTF_RELOCATABLE:BOOL=OFF \
    -DSDLTTF_SAMPLES:BOOL=OFF \
    -DSDLTTF_SAMPLES_INSTALL:BOOL=OFF \
    -DSDLTTF_STRICT:BOOL=ON \
    -DSDLTTF_VENDORED:BOOL=OFF \
    -DSDLTTF_WERROR:BOOL=OFF \
    -DBUILD_SHARED_LIBS:BOOL=ON
%mingw_make %{?_smp_mflags}

export MINGW_BUILDDIR_SUFFIX=static
%mingw_cmake \
    -DSDLTTF_HARFBUZZ:BOOL=ON \
    -DSDLTTF_INSTALL:BOOL=ON \
    -DSDLTTF_INSTALL_CPACK:BOOL=OFF \
    -DSDLTTF_INSTALL_MAN:BOOL=OFF \
    -DSDLTTF_PLUTOSVG:BOOL=OFF \
    -DSDLTTF_RELOCATABLE:BOOL=OFF \
    -DSDLTTF_SAMPLES:BOOL=OFF \
    -DSDLTTF_SAMPLES_INSTALL:BOOL=OFF \
    -DSDLTTF_STRICT:BOOL=ON \
    -DSDLTTF_VENDORED:BOOL=OFF \
    -DSDLTTF_WERROR:BOOL=OFF \
    -DBUILD_SHARED_LIBS:BOOL=OFF
%mingw_make %{?_smp_mflags}


%install
# export DESTDIR="%{buildroot}"
export MINGW_BUILDDIR_SUFFIX=shared
%mingw_make install DESTDIR=%{buildroot}
export MINGW_BUILDDIR_SUFFIX=static
%mingw_make install DESTDIR=%{buildroot}


%files -n mingw32-SDL3_ttf
%doc CHANGES.txt README.md
%license %{mingw32_datadir}/licenses/SDL3_ttf/LICENSE.txt
%{mingw32_bindir}/SDL3_ttf.dll
%{mingw32_libdir}/libSDL3_ttf.dll.a
%{mingw32_libdir}/cmake/SDL3_ttf/
%exclude %{mingw32_libdir}/cmake/SDL3_ttf/*static*
%{mingw32_libdir}/pkgconfig/sdl3-ttf.pc
%{mingw32_includedir}/SDL3_ttf/

%files -n mingw32-SDL3_ttf-static
%{mingw32_libdir}/libSDL3_ttf.a
%{mingw32_libdir}/cmake/SDL3_ttf/*static*

%files -n mingw64-SDL3_ttf
%doc CHANGES.txt README.md
%license %{mingw64_datadir}/licenses/SDL3_ttf/LICENSE.txt
%{mingw64_bindir}/SDL3_ttf.dll
%{mingw64_libdir}/libSDL3_ttf.dll.a
%{mingw64_libdir}/cmake/SDL3_ttf/
%exclude %{mingw64_libdir}/cmake/SDL3_ttf/*static*
%{mingw64_libdir}/pkgconfig/sdl3-ttf.pc
%{mingw64_includedir}/SDL3_ttf/

%files -n mingw64-SDL3_ttf-static
%{mingw64_libdir}/libSDL3_ttf.a
%{mingw64_libdir}/cmake/SDL3_ttf/*static*

%changelog
* Tue Feb 17 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.2.2-1
- Initial packaging
