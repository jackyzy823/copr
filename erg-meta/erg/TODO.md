erg-common
    erg-proc_macros
linter
compiler
parser


---- test_vm_embedding stdout ----
Starting the REPL server...
Connecting to the REPL server...
Retrying to connect to the REPL server...
thread 'test_vm_embedding' panicked at /usr/share/cargo/registry/erg_common-0.6.53/serialize.rs:37:14:                                                      unknown magic number (unsupported Python version)                                                                                                           note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace                                                                               The REPL server is closed.

failures:
    test_vm_embedding

test result: FAILED. 5 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.51s

error: test failed, to rerun pass `--test embed`
     Running `/data/erg/erg-0.6.53-build/erg-0.6.53/target/rpm/deps/eval_tests-43aa3e2cc1241aa2`


See `get_ver_from_magic_num`, erg only support python <3.12

1) add requires: python3.11
2) skip test_vm_embedding
