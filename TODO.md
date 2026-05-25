Rust
    - llmfit
    - trougnouf/cfait
        * winresouce could be removed, since it is used when building and CARGO_CFG_TARGET_OS==windows
        * uniffi is used for ANDROID / INTEROP
    - espanso
        * Already done via https://discussion.fedoraproject.org/t/espanso-copr-available-for-testing/88921
        * https://copr.fedorainfracloud.org/coprs/eclipseo/espanso/
        * not in crates.io
    - [amdgpu_top](https://github.com/Umio-Yasuno/amdgpu_top)
    - [sandlock](https://github.com/multikernel/sandlock)

Python
    - [bup](https://github.com/bup/bup)
        * Not in PyPI (don't confused with the PyPI one, it is another package)
    - mitmproxy
        * https://rathann.fedorapeople.org/review/mitmproxy/mitmproxy.spec
        * https://bugzilla.redhat.com/show_bug.cgi?id=2109939
        * https://build.opensuse.org/projects/openSUSE:Factory/packages/python-mitmproxy/files/python-mitmproxy.spec
        * it requires https://github.com/mitmproxy/mitmproxy_rs, which is not in crates.io
        * it is basically unpackagable.
        * python-mitmproxy depends on python-mitmproxy_rs
        * python-mitmrpoxy_rs python part requries python-mitmprox_linux
        * python-mitmproxy_rs rust part requires rust-mitmproxy and rust-mitmproxy-highlight and rust-contentviews
        * python-mitmproxy_linux rust part requires rust-mitmproxy and rust-mitmproxy-linux-ebpf-common
        * python-mitmproxy_linux rust buildscript requires rust-mitmproxy-linux-ebpf
        * rust-mitmproxy-linux-ebpf requires special toolchain, and target, see mitmproxy-linux-ebpf/.cargo/config.toml
        * rust-mitmproxy-linux-ebpf rust buildscript requires bpf-linker binary
        * bpf-linker requires special LLVM version and build method, see bpf-linker/BUILDING.md
        * Fedora eBPF packaging docs: https://fosdem.org/2026/schedule/event/VSXPA8-packaging-ebpf-in-linux-distros/:wq

C/C++
    - KDE/kup
        * GUI frontend for bup/bup
    - [plasma-panel-colorizer](https://github.com/luisbocanegra/plasma-panel-colorizer)
        * Already done in https://build.opensuse.org/package/show/home:luisbocanegra/plasma-panel-colorizer
    - rapier1/hpnssh
        * Already done in copr rapier1/hpnssh
    - cyanreg/cyanrip
        * In Package_maintainers_wishlist
        * Already in openSUSE
    - [Angie](https://github.com/webserver-llc/angie)
        * nginx fork
    - [TuxManager](https://github.com/benapetr/TuxManager)
        * has own rpm build spec, see packaging/package-rpm.sh

Java
    - JADX
        * GUI and CLI
        * take jd-core / java-jd-decompiler as reference (however it don't use gradle, just plain javac in spec)
        * gradle problem
        * dependencies problem

