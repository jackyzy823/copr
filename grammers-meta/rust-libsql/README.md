Problem 1: nothing provides requested (crate(libsql-hrana/default) >= 0.9.30 with crate(libsql-hrana/default) < 0.10.0~)
 Problem 2: nothing provides requested (crate(libsql-sqlite3-parser/default) >= 0.13.0 with crate(libsql-sqlite3-parser/default) < 0.14.0~)
 Problem 3: nothing provides requested (crate(libsql-sys/default) >= 0.9.30 with crate(libsql-sys/default) < 0.10.0~)
 Problem 4: nothing provides requested (crate(libsql_replication/default) >= 0.9.30 with crate(libsql_replication/default) < 0.10.0~)

 Problem 5: nothing provides requested (crate(tonic-web/default) >= 0.11.0 with crate(tonic-web/default) < 0.12.0~)

 Problem 6: nothing provides requested (crate(tonic/default) >= 0.11.0 with crate(tonic/default) < 0.12.0~)

 Fedora has tonic 0.12


 Problem 7: nothing provides requested (crate(tower-http/default) >= 0.4.4 with crate(tower-http/default) < 0.5.0~)
 Problem 8: nothing provides requested (crate(tower-http/set-header) >= 0.4.4 with crate(tower-http/set-header) < 0.5.0~)
 Problem 9: nothing provides requested (crate(tower-http/trace) >= 0.4.4 with crate(tower-http/trace) < 0.5.0~)
 Problem 10: nothing provides requested (crate(tower-http/util) >= 0.4.4 with crate(tower-http/util) < 0.5.0~)

 Fedora has tower-http0.5 so we must downgrade again and again


So i decide to remove this features

    "replication",
    "remote",
    "sync",

and all examples and one test for "replication"


Runtime deps:

Problem 1: conflicting requests
  - nothing provides (crate(worker/default) >= 0.6.7 with crate(worker/default) < 0.7.0~) needed by rust-libsql+cloudflare-devel-0.9.30-1.fc45.noarch from @commandline
 Problem 2: conflicting requests
  - nothing provides (crate(libsql-hrana/default) >= 0.9.30 with crate(libsql-hrana/default) < 0.10.0~) needed by rust-libsql+hrana-devel-0.9.30-1.fc45.noarch from @commandline
 Problem 3: conflicting requests
  - nothing provides (crate(libsql_replication/default) >= 0.9.30 with crate(libsql_replication/default) < 0.10.0~) needed by rust-libsql+libsql_replication-devel-0.9.30-1.fc45.noarch from @commandline
 Problem 4: conflicting requests
  - nothing provides (crate(libsql-sqlite3-parser/default) >= 0.13.0 with crate(libsql-sqlite3-parser/default) < 0.14.0~) needed by rust-libsql+parser-devel-0.9.30-1.fc45.noarch from @commandline
 Problem 5: conflicting requests
  - nothing provides (crate(tonic/default) >= 0.11.0 with crate(tonic/default) < 0.12.0~) needed by rust-libsql+tonic-devel-0.9.30-1.fc45.noarch from @commandline
 Problem 6: conflicting requests
  - nothing provides (crate(tonic-web/default) >= 0.11.0 with crate(tonic-web/default) < 0.12.0~) needed by rust-libsql+tonic-web-devel-0.9.30-1.fc45.noarch from @commandline
 Problem 7: conflicting requests
  - nothing provides (crate(tower-http/default) >= 0.4.4 with crate(tower-http/default) < 0.5.0~) needed by rust-libsql+tower-http-devel-0.9.30-1.fc45.noarch from @commandline
  - nothing provides (crate(tower-http/set-header) >= 0.4.4 with crate(tower-http/set-header) < 0.5.0~) needed by rust-libsql+tower-http-devel-0.9.30-1.fc45.noarch from @commandline
  - nothing provides (crate(tower-http/trace) >= 0.4.4 with crate(tower-http/trace) < 0.5.0~) needed by rust-libsql+tower-http-devel-0.9.30-1.fc45.noarch from @commandline
  - nothing provides (crate(tower-http/util) >= 0.4.4 with crate(tower-http/util) < 0.5.0~) needed by rust-libsql+tower-http-devel-0.9.30-1.fc45.noarch from @commandline
 Problem 8: package rust-libsql+wasm-devel-0.9.30-1.fc45.noarch from @commandline requires crate(libsql/hrana) = 0.9.30, but none of the providers can be installed
  - conflicting requests
  - nothing provides (crate(libsql-hrana/default) >= 0.9.30 with crate(libsql-hrana/default) < 0.10.0~) needed by rust-libsql+hrana-devel-0.9.30-1.fc45.noarch from @commandline

Just skip install 
rm noarch/rust-libsql+tonic-* noarch/rust-libsql+wasm* noarch/rust-libsql+libsql_replication*
noarch/rust-libsql+tower-http* noarch/rust-libsql+cloudflare*
 noarch/rust-libsql+hrana* noarch/rust-libsql+parser*

