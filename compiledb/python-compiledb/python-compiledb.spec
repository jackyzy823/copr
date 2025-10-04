## use srcname or pypi_name
%global         pypi_name compiledb
## Since there's compiledb-go , rust-compiledb, so we don't occupy the name `compiledb`
Name:           python-%{pypi_name}
Version:        0.10.7
Release:        %autorelease
Summary:        Compilation Database Generator

License:        GPL-3.0-or-later
URL:            https://github.com/nickdiego/%{pypi_name}
Source:         %{pypi_source %{pypi_name} %{version}}

BuildArch:      noarch
BuildRequires:  python3-devel

Conflicts:      golang-github-fcying-compiledb
Conflicts:      rust-compiledb

%global _description %{expand:
%{pypi_name} is a tool for generating Clang's JSON Compilation Database files for make-based build systems.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}
install -m644 -p -D sh-completion/%{pypi_name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{pypi_name}.bash

%check
%pyproject_check_import
%tox


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/%{pypi_name}
%{_datadir}/bash-completion/completions/%{pypi_name}.bash

%changelog
%autochangelog
