Rust
    - llmfit
    - trougnouf/cfait
        * winresouce could be removed, since it is used when building and CARGO_CFG_TARGET_OS==windows
        * uniffi is used for ANDROID / INTEROP

Python
    - [bup](https://github.com/bup/bup)
        * Not in PyPI (don't confused with the PyPI one, it is another package)
    - mitmproxy
        * https://rathann.fedorapeople.org/review/mitmproxy/mitmproxy.spec
        * https://bugzilla.redhat.com/show_bug.cgi?id=2109939
        * https://build.opensuse.org/projects/openSUSE:Factory/packages/python-mitmproxy/files/python-mitmproxy.spec
        * it requires https://github.com/mitmproxy/mitmproxy_rs, which is not in crates.io

C++
    - KDE/kup
        * GUI frontend for bup/bup

Java
    - JADX
        * GUI and CLI
        * take jd-core / java-jd-decompiler as reference (however it don't use gradle, just plain javac in spec)
        * gradle problem
        * dependencies problem

