Name:           bmfdec

%global git_commit  c7b72f6ece126a8f686d66402009a14cb032a769
%global git_commit_short  %(c="%{git_commit}"; echo ${c:0:7})

Version:        0^1.git%{git_commit_short}
Release:        %autorelease
Summary:        Decompile binary MOF file (BMF) from WMI buffer

License:        GPL-2.0-only
URL:            https://github.com/pali/bmfdec
Source0:        %{url}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz

BuildRequires:	make
BuildRequires:	gcc

%description
%{summary}.


%prep
%autosetup -n %{name}-%{git_commit}


%build
%make_build


%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp bmfdec %{buildroot}%{_bindir}/
install -m 0755 -vp bmfparse %{buildroot}%{_bindir}/
install -m 0755 -vp bmf2mof %{buildroot}%{_bindir}/


%check


%files
%license
%doc
%{_bindir}/bmf*

%changelog
%autochangelog

