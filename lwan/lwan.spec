%global commit 00987b9e0063f810882afc008f5129b996a9ce62
%global shortcommit %{sub %{commit} 1 7}

Name:           lwan
Version:        0.7^20260516git%{shortcommit}
Release:        %autorelease
Summary:        Experimental, scalable, high performance HTTP server

License:        GPL-2.0-or-later
URL:            https://lwan.ws

Source0:        https://github.com/lpereira/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

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

%description
%{summary}.

%package devel
Summary: Development files for lib%{name}
## i guess package lwan shouldn't be a Requires for devel here.
%description devel
%{summary}.

%prep
%autosetup -n %{name}-%{commit}

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

