Runtime deps:
  - nothing provides (crate(libsql-rusqlite) >= 0.9.30 with crate(libsql-rusqlite) < 0.10.0~) needed by rust-libsql-sys+rusqlite-devel-0.9.30-1.fc45.noarch from @commandline
  - nothing provides (crate(libsql-rusqlite/column_decltype) >= 0.9.30 with crate(libsql-rusqlite/column_decltype) < 0.10.0~) needed by rust-libsql-sys+rusqlite-devel-0.9.30-1.fc45.noarch from @commandline
  - nothing provides (crate(libsql-rusqlite/functions) >= 0.9.30 with crate(libsql-rusqlite/functions) < 0.10.0~) needed by rust-libsql-sys+rusqlite-devel-0.9.30-1.fc45.noarch from @commandline
  - nothing provides (crate(libsql-rusqlite/hooks) >= 0.9.30 with crate(libsql-rusqlite/hooks) < 0.10.0~) needed by rust-libsql-sys+rusqlite-devel-0.9.30-1.fc45.noarch from @commandline
  - nothing provides (crate(libsql-rusqlite/libsql-experimental) >= 0.9.30 with crate(libsql-rusqlite/libsql-experimental) < 0.10.0~) needed by rust-libsql-sys+rusqlite-devel-0.9.30-1.fc45.noarch from @commandline
  - nothing provides (crate(libsql-rusqlite/limits) >= 0.9.30 with crate(libsql-rusqlite/limits) < 0.10.0~) needed by rust-libsql-sys+rusqlite-devel-0.9.30-1.fc45.noarch from @commandline
  - nothing provides (crate(libsql-rusqlite/load_extension) >= 0.9.30 with crate(libsql-rusqlite/load_extension) < 0.10.0~) needed by rust-libsql-sys+rusqlite-devel-0.9.30-1.fc45.noarch from @commandline
  - nothing provides (crate(libsql-rusqlite/modern_sqlite) >= 0.9.30 with crate(libsql-rusqlite/modern_sqlite) < 0.10.0~) needed by rust-libsql-sys+rusqlite-devel-0.9.30-1.fc45.noarch from @commandline
  - nothing provides (crate(libsql-rusqlite/trace) >= 0.9.30 with crate(libsql-rusqlite/trace) < 0.10.0~) needed by rust-libsql-sys+rusqlite-devel-0.9.30-1.fc45.noarch from @commandline
 Problem 2: conflicting requests
  - nothing provides (crate(libsql-ffi/wasmtime-bindings) >= 0.9.30 with crate(libsql-ffi/wasmtime-bindings) < 0.10.0~) needed by rust-libsql-sys+wasmtime-bindings-devel-0.9.30-1.fc45.noarch from @commandline


just remove *+wasm* and *+rusqlite*
