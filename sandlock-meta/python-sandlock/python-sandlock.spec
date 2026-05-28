Name:           python-sandlock
Version:        0.8.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Lightweight process sandbox using Landlock, seccomp, and seccomp user notification

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/multikernel/sandlock
Source:         %{pypi_source sandlock}

# we have libsandlock_ffi, so we don't need to build it.
Patch:          exclude-setuptools-rust.diff

BuildArch:      noarch
BuildRequires:  python3-devel

# for test: pyproject_check_import
BuildRequires:       libsandlock_ffi = %{version}

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sandlock' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-sandlock
Summary:        %{summary}
Requires:       libsandlock_ffi = %{version}-%{release}

%description -n python3-sandlock %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

# Fedora support python-mcp from 43
%if 0%{?fedora} > 42
%pyproject_extras_subpkg -n python3-sandlock mcp
%{_bindir}/sandlock-mcp

%pyproject_extras_subpkg -n python3-sandlock mcp-remote
%endif

%prep
%autosetup -p1 -n sandlock-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
# Fedora support python-mcp from 43
%if 0%{?fedora} > 42
%pyproject_buildrequires -x mcp,mcp-remote
%else
%pyproject_buildrequires
%endif


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files sandlock
# Fedora support python-mcp from 43
%if 0%{?fedora} <= 42
rm %{buildroot}%{_bindir}/sandlock-mcp
%endif



%check
# Fedora support python-mcp from 43
%if 0%{?fedora} > 42
%pyproject_check_import
%else
%pyproject_check_import -e sandlock.mcp.server
%endif


%files -n python3-sandlock -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
