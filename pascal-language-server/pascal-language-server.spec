# latest commit 5202e1a0c852f2dfe23825a060246978a49ecaf8 failed to build
# due to Cannot find laz_avl_Tree, maybe lazarus too new (we have 4.2)?
# ref: https://github.com/cheat-engine/cheat-engine/issues/3179
# ref: https://gitlab.com/freepascal.org/lazarus/lazarus/-/commit/e65a102527a12597efa384c74ebcfad50a6cbe23
%global commit c28f654f041efba45779b71fea0905f408a462b0
%global shortcommit %{sub %{commit} 1 7}

Name:           pascal-language-server
Version:        0^1.%{shortcommit}
Release:        %autorelease
Summary:        LSP server implementation for Pascal

License:        GPL-3.0-or-later
URL:            https://github.com/genericptr/pascal-language-server
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: lazarus-tools
BuildRequires: lazarus-lcl-gtk2
BuildRequires: pkgconfig(sqlite3)

%description
%{summary}.


%prep
%autosetup -n %{name}-%{commit} -p1


%build
lazbuild src/protocol/lspprotocol.lpk
lazbuild src/serverprotocol/lspserver.lpk
lazbuild src/standard/pasls.lpr


%install
install -Dpm0755 -t %{buildroot}%{_bindir} src/standard/pasls


%check


%files
%license COPYING
%doc README.md
%{_bindir}/pasls


%changelog
%autochangelog

