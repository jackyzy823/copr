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
URL:            https://codeberg.org/Lonami/Telethon
Source0:        %{pypi_source}
BuildArch:      noarch

# fix asyncio loop issue in Python 3.14
Patch0:		https://codeberg.org/Lonami/Telethon/commit/577812be4dd5932c463322b85b6829cedaa58a09.patch

#BuildRequires:  python3-devel
#BuildRequires:  python3dist(setuptools)

%description
Telethon is an asyncio Python 3 MTProto library to interact with Telegram's API
as a user or through a bot account (bot API alternative)

%package -n     python3-%{pypi_name}
Summary:        %{summary}

#Requires:       python3dist(pyaes)
#Requires:       python3dist(rsa)


%description -n python3-%{pypi_name}
Telethon is an asyncio Python 3 MTProto library to interact with Telegram's API
as a user or through a bot account (bot API alternative)

%pyproject_extras_subpkg -n python3-%{pypi_name} cryptg

%prep
%autosetup -p1 -n %{pypi_name}-%{pypi_version}

%generate_buildrequires
##%dnl %pyproject_buildrequires -t
## no tests currently. see https://github.com/tox-dev/tox/issues/3602
## Fedora now have 4.35, we require at least 4.39 to workaround error
## "setup.cfg due to section tox:tox not found"
%pyproject_buildrequires -x cryptg

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

