## use srcname or pypi_name
%global         srcname yt_dlp_ejs
%global         pypi_name %{gsub %{srcname} _ -}
Name:           python-%{pypi_name}
Version:        0.3.1
Release:        %autorelease
Summary:        External JavaScript for yt-dlp supporting many runtimes

# astring MIT meriyah ISC
License:        Unlicense AND ISC AND MIT
URL:            https://github.com/ytdlp/ejs
Source:         %{pypi_source %{srcname}}

## astring
## meriyah
Source1:        https://registry.npmjs.org/meriyah/-/meriyah-6.1.4.tgz
Source2:        https://registry.npmjs.org/astring/-/astring-1.9.0.tgz

Source3:        tests.py

## Make hatch build script to build js with esbuild
Patch0:         hatch_with_esbuild.patch

BuildArch:      noarch
BuildRequires:  python3-devel
## note nodejs-devel --> could resolve to nodejs24-devel, which have /usr/bin/node-24 instead of /usr/bin/node
## so we force use node24-devel, and don't use %{__nodejs} macro , instead of fixed path
BuildRequires:	nodejs24-devel

BuildRequires:  golang-github-evanw-esbuild


%global _description %{expand:
%{pypi_name} is external JavaScript for yt-dlp supporting many runtimes.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}
mkdir node_modules
pushd node_modules
mkdir meriyah && tar -x --strip-components=1 -C meriyah -f %{SOURCE1}
mkdir astring && tar -x --strip-components=1 -C astring -f %{SOURCE2}
popd
cp -p %{SOURCE3} .


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pyproject_check_import
## unit test for 0.3.1 +
## NOTE: since js file is not in import path: current folder, this test won't work without copying js file to yt_dlp_ejs folder
# just like .github/workflows/ci.yml , it unzip wheel and update js files to yt_dlp_ejs folder , we copy it
cp dist/yt.solver.core.min.js yt_dlp_ejs/yt/solver/core.min.js
cp dist/yt.solver.lib.min.js yt_dlp_ejs/yt/solver/lib.min.js
## https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#py3_test_envvars
%{py3_test_envvars} %{python3} -m unittest

## test with nodejs
# since js are copied, sys.path hack could be removed.
%{py3_test_envvars} %{python3} tests.py | /usr/bin/node-24

## Otherwise test with yt-dlp's test_ejs_integration.py
# install pytest , download yt-dlp source code
# pytest tests/test_jsc/test_ejs_integration.py


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
