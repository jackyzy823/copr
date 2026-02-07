%global commit a05ddec0d889efe3a9082790df4e2ed380d6a555
%global shortcommit %{sub %{commit} 1 7}
Name:           pycdc
Version:        0.1^20250830git%{shortcommit}
Release:        %autorelease
Summary:        C++ python bytecode disassembler and decompiler

License:        GPL-3.0-or-later
URL:            https://github.com/zrax/pycdc

Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
pycdc aims to translate compiled Python byte-code back into valid and human-readable Python source code. It includes both a disassembler (pycdas) and a decompiler (pycdc).


%prep
%autosetup -n %{name}-%{commit}


%build
%cmake
%cmake_build


%install
install -Dpm0755 -t %{buildroot}%{_bindir} %{_vpath_builddir}/%{name}
install -Dpm0755 -t %{buildroot}%{_bindir} %{_vpath_builddir}/pycdas

%check


%files
%license LICENSE
%doc README.markdown
%{_bindir}/%{name}
%{_bindir}/pycdas


%changelog
%autochangelog

