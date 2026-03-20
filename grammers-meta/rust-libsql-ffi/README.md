Fedora don't have bindgen0.66 (but have 0.63 , 0.68 ), since it is just a build dep, a minor bump do no harm

Runtime dep: just rm +wasm*.rpm and install
  - nothing provides (crate(libsql-wasmtime-bindings/default) >= 0.2.1 with crate(libsql-wasmtime-bindings/default) < 0.3.0~) needed by rust-libsql-ffi+wasmtime-bindings-devel-0.9.30-1.fc45.noarch from @commandline
