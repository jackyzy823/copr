# Created by pyp2rpm-3.3.10
%global pypi_name telethon
%global pypi_version 1.42.0

# see description in %generate_buildrequires
%bcond check 0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        %{autorelease}
Summary:        Full-featured Telegram client library for Python 3

License:        MIT
URL:            https://github.com/LonamiWebs/Telethon
Source0:        %{pypi_source}
BuildArch:      noarch

#BuildRequires:  python3-devel
#BuildRequires:  python3dist(setuptools)

%description
Telethon is an asyncio Python 3 MTProto library to interact with Telegram's API
as a user or through a bot account (bot API alternative)

%package -n     python3-%{pypi_name}
Summary:        %{summary}

#Requires:       python3dist(pyaes)
#Requires:       python3dist(rsa)

## cryptg is a python binding for a rust based library.
## so i currently skip this extra dep
## %dnl %pyproject_extras_subpkg -n python3-%{pypi_name} cryptg

%description -n python3-%{pypi_name}
Telethon is an asyncio Python 3 MTProto library to interact with Telegram's API
as a user or through a bot account (bot API alternative)

%prep
%autosetup -n %{pypi_name}-%{pypi_version}

%generate_buildrequires
## no cryptg currently
##%dnl %pyproject_buildrequires -t -x cryptg
##%dnl %pyproject_buildrequires -t
## no tests currently. see https://github.com/tox-dev/tox/issues/3602
## Fedora now have 4.35, we require at least 4.39 to workaround error
## "setup.cfg due to section tox:tox not found"
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%if %{with check}
%check
%tox
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog

