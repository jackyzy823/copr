## use srcname or pypi_name
%global         pypi_name bashlex
Name:           python-%{pypi_name}
Version:        0.18
Release:        %autorelease
Summary:        Python parser for bash

License:        GPL-3.0-or-later
URL:            https://github.com/idank/%{pypi_name}
Source:         %{pypi_source %{pypi_name} %{version}}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
#BuildRequires:  python3-pytest

%global _description %{expand:
%{pypi_name} is a Python port of the parser used internally by GNU bash.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
%pyproject_check_import
%pytest


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
