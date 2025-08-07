# Copied from https://github.com/yorickpeterse/copr/blob/main/lua-language-server/lua-language-server.spec
# since yorickpeterse's Fedora Copr repo for lua-language-server no longer exists, i need to build it by my own.

%global debug_package %{nil}

Name:          lua-language-server
Version:       3.15.0
Release:       %autorelease
Summary:       A language server that offers Lua language support
License:       BSD-3-Clause AND BSL-1.0 AND LGPL-2.1 AND MIT AND Unlicense
URL:           https://github.com/LuaLS/lua-language-server
Source0:       %{url}/releases/download/%{version}/%{name}-%{version}-submodules.zip
Source1:       lua-lsp-launcher.sh
ExcludeArch:   s390x ppc64le ppc64
BuildRequires: fdupes
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: libstdc++-static
BuildRequires: ninja-build
BuildRequires: unzip

%description
A language server that offers Lua language support

%prep
%autosetup -c

%build
sed "s#\(lm.cxx.*\)#\1\nlm.flags = '%{optflags}'\nlm.ldflags = '%{__global_ldflags}'#p" -i make.lua
ninja -C 3rd/luamake -f compile/ninja/linux.ninja
./3rd/luamake/luamake all

%install
install -d -m 0755 %{buildroot}%{_libexecdir}/%{name}
cp -av bin/* %{buildroot}%{_libexecdir}/%{name}
install -d -m 0755 %{buildroot}%{_datadir}/%{name}
cp -av \
    debugger.lua \
    main.lua \
    locale \
    script \
    meta \
    %{buildroot}%{_datadir}/%{name}/
install -d -m 0755 %{buildroot}%{_bindir}
sed -e 's#@LIBEXECDIR@#%{_libexecdir}#' %{SOURCE1} > %{buildroot}%{_bindir}/%{name}
chmod 0755 %{buildroot}%{_bindir}/%{name}

%fdupes %{buildroot}%{_libexecdir}/%{name}
%fdupes %{buildroot}%{_datadir}/%{name}

%check
./3rd/luamake/luamake bee-test unit-test

%files
%license LICENSE
%doc README.md changelog.md
%{_bindir}/%{name}
%{_libexecdir}/%{name}/
%{_datadir}/%{name}/

%changelog
%autochangelog
