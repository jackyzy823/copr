Name:           python-kaitaistruct
Version:        0.11
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Kaitai Struct declarative parser generator for binary data: runtime library for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://doc.kaitai.io/
Source:         %{pypi_source kaitaistruct}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'kaitaistruct' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-kaitaistruct
Summary:        %{summary}

%description -n python3-kaitaistruct %_description


%prep
%autosetup -p1 -n kaitaistruct-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files -l kaitaistruct


%check
%pyproject_check_import


%files -n python3-kaitaistruct -f %{pyproject_files}


%changelog
%autochangelog
