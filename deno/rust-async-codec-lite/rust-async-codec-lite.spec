# Generated by rust2rpm 27
# * construct dependency fast
%bcond check 0
%global debug_package %{nil}

%global crate async-codec-lite

Name:           rust-async-codec-lite
Version:        0.0.2
Release:        %autorelease
Summary:        Adaptors from AsyncRead/AsyncWrite to Stream/Sink using futures

License:        Apache-2.0 WITH LLVM-exception AND MIT
URL:            https://crates.io/crates/async-codec-lite
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Adaptors from AsyncRead/AsyncWrite to Stream/Sink using futures.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-Apache
%license %{crate_instdir}/LICENSE-MIT
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

%package     -n %{name}+cbor-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cbor-devel %{_description}

This package contains library source intended for building other packages which
use the "cbor" feature of the "%{crate}" crate.

%files       -n %{name}+cbor-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+json-devel %{_description}

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%files       -n %{name}+json-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+lines-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+lines-devel %{_description}

This package contains library source intended for building other packages which
use the "lines" feature of the "%{crate}" crate.

%files       -n %{name}+lines-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+memchr-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+memchr-devel %{_description}

This package contains library source intended for building other packages which
use the "memchr" feature of the "%{crate}" crate.

%files       -n %{name}+memchr-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde_cbor-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_cbor-devel %{_description}

This package contains library source intended for building other packages which
use the "serde_cbor" feature of the "%{crate}" crate.

%files       -n %{name}+serde_cbor-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde_json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_json-devel %{_description}

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%files       -n %{name}+serde_json-devel
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
