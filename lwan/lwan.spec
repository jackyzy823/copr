# disable lto , due to ld error for not finding embedded binary resources
# after test, with NO_INCBIN , lto could pass
# either
%dnl %define _lto_cflags %{nil}
# or use upstream patch 29e0d376dc9e85cd098e1f8ae0a32f012127a98
Name:           lwan
Version:        0.7
Release:        %autorelease
Summary:        Experimental, scalable, high performance HTTP server

License:        GPL-2.0-or-later
URL:            https://lwan.ws

Source0:        https://github.com/lpereira/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(libbrotlicommon)
# optional mimalloc / jemalloc
BuildRequires:  pkgconfig(mbedtls)
# or lua 5.1
BuildRequires:  pkgconfig(luajit)
BuildRequires:  gcc
# test requires python and requests
# sqlite is a dependency for techenmpower benchmark suite
# BuildRequires:  pkgconfig(sqlite3)

# fix bin2hex ld issue
Patch0:         https://github.com/lpereira/lwan/commit/29e0d376dc9e85cd098e1f8ae0a32f012127a98

%description
%{summary}.

%package devel
Summary: Development files for lib%{name}
## i guess package lwan shouldn't be a Requires for devel here.
%description devel
%{summary}.

%prep
%autosetup -p1

%conf
# -DALTERNATIVE_MALLOC=
# -DENABLE_TLS=NO
# -DENABLE_IA32_CRC32
# -DUSE_SYSLOG=OFF
# -DSANITIZER
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DGITVERSIONDETECT_VERSION=%{version} \
    -DMTUNE_NATIVE=OFF \
    -DENABLE_BROTLI=ON \
    -DENABLE_ZSTD=ON

%build
%cmake_build

%install
%cmake_install

%check
# test requires mariadb client which might too heavy

%files
%license COPYING
%doc    README.md
#Lwan will try to find a configuration file based in the executable name in the current directory
#sp package `lwan.conf` as a sample in doc
%doc    lwan.conf
%{_bindir}/%{name}

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.{a,so}
# lwan install lwan.pc in /usr/lib (see CMakeLists.txt)
%dnl %{_libdir}/pkgconfig/%{name}.pc
%{_prefix}/lib/pkgconfig/%{name}.pc

%changelog
%autochangelog

