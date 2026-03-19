# Created by pyp2rpm-3.3.10
%global pypi_name cryptg
%global pypi_version 0.5.2

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        %{autorelease}
Summary:        Cryptographic utilities for Telegram

# cryptg CC0, grammers-crypto MIT, pyo3 Apache-2.0
License:        CC0 AND MIT AND Apache-2.0
URL:            https://github.com/cher-nov/cryptg
Source0:        %{pypi_source}
ExclusiveArch:  %{rust_arches}

Patch0:		Build-RustExtension-with-debug-symbols.patch

## pyproject_buildrequires not work
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-rust)
## otherwise /usr/lib/rpm/redhat/pyproject_wheel.py will fail due to missing module pip
BuildRequires:  python3dist(pip)
# for cargo_generate_buildrequires
BuildRequires:  rust-packaging >= 21

%description
This is a small native extension for Python 3 to help libraries that
want to work with the Telegram API, which uses the uncommon AES-IGE mode for it.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

#Requires:       python3dist(pyaes)
#Requires:       python3dist(rsa)

%description -n python3-%{pypi_name}
This is a small native extension for Python 3 to help libraries that
want to work with the Telegram API, which uses the uncommon AES-IGE mode for it.

# Take https://src.fedoraproject.org/rpms/matrix-synapse/blob/f38/f/matrix-synapse.spec as reference about rust binding
# see https://src.fedoraproject.org/rpms/matrix-synapse/blob/f38/f/0002-Build-RustExtension-with-debug-symbols.patch for debug symbol
%prep
%autosetup -n %{pypi_name}-%{pypi_version}
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
## not work, it requires python3dist(setuptools[core]) >= 68, which fedora don't package extra: core
##%dnl %pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt LICENSES/LICENSE.*
%doc README.rst

%changelog
%autochangelog

