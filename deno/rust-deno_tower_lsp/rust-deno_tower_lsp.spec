# Generated by rust2rpm 27
# * construct dependency fast
%bcond check 0
%global debug_package %{nil}

%global crate deno_tower_lsp

Name:           rust-deno_tower_lsp
Version:        0.1.0
Release:        %autorelease
Summary:        Fork of https://crates.io/crates/tower-lsp, used in Deno

License:        MIT
URL:            https://crates.io/crates/deno_tower_lsp
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
This is a fork of https://crates.io/crates/tower-lsp, used in Deno. At
the moment only floating patches.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/CODE_OF_CONDUCT.md
%doc %{crate_instdir}/CONTRIBUTING.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async-codec-lite-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-codec-lite-devel %{_description}

This package contains library source intended for building other packages which
use the "async-codec-lite" feature of the "%{crate}" crate.

%files       -n %{name}+async-codec-lite-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+proposed-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+proposed-devel %{_description}

This package contains library source intended for building other packages which
use the "proposed" feature of the "%{crate}" crate.

%files       -n %{name}+proposed-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+runtime-agnostic-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+runtime-agnostic-devel %{_description}

This package contains library source intended for building other packages which
use the "runtime-agnostic" feature of the "%{crate}" crate.

%files       -n %{name}+runtime-agnostic-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+runtime-tokio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+runtime-tokio-devel %{_description}

This package contains library source intended for building other packages which
use the "runtime-tokio" feature of the "%{crate}" crate.

%files       -n %{name}+runtime-tokio-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tokio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-devel %{_description}

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%files       -n %{name}+tokio-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tokio-util-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-util-devel %{_description}

This package contains library source intended for building other packages which
use the "tokio-util" feature of the "%{crate}" crate.

%files       -n %{name}+tokio-util-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
