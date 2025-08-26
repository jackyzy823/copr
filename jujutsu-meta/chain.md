No match for argument: crate(clap-markdown/default) = 0.1.5 
 DONE
Problem 1: nothing provides requested (crate(crossterm/windows) >= 0.28.0 with crate(crossterm/windows) < 0.29.0~)
 No needed since it is for windows
<!-- Problem 2: nothing provides requested (crate(datatest-stable/default) >= 0.3.2 with crate(datatest-stable/default) < 0.4.0~) -->
<!--   Problem 1: nothing provides requested (crate(camino-tempfile/default) >= 1.1.1 with crate(camino-tempfile/default) < 2.0.0~) -->
<!--    DONE 1.4.1 -->
<!--   Problem 2: nothing provides requested (crate(fancy-regex/default) >= 0.14.0 with crate(fancy-regex/default) < 0.15.0~) -->
<!--    Newest in crate is 0.16 , F42 has 0.13  so upgrade to 0.14 -->
  
Problem 3: nothing provides requested (crate(jj-lib) >= 0.32.0 with crate(jj-lib) < 0.33.0~) Problem 4: nothing provides requested (crate(jj-lib/git) >= 0.32.0 with crate(jj-lib/git) < 0.33.0~) Problem 5: nothing provides requested (crate(jj-lib/testing) >= 0.32.0 with crate(jj-lib/testing) < 0.33.0~) Problem 6: nothing provides requested (crate(jj-lib/watchman) >= 0.32.0 with crate(jj-lib/watchman) < 0.33.0~)


  Problem 1: nothing provides requested (crate(interim/chrono_0_4) >= 0.2.1 with crate(interim/chrono_0_4) < 0.3.0~)
  Problem 2: nothing provides requested (crate(interim/default) >= 0.2.1 with crate(interim/default) < 0.3.0~)
   F42 has 0.1.2 wait until 0.2.1 from testing to
  Problem 3: nothing provides requested (crate(jj-lib-proc-macros/default) >= 0.32.0 with crate(jj-lib-proc-macros/default) < 0.33.0~)
   DONE
  Problem 4: nothing provides requested (crate(pollster/default) >= 0.4.0 with crate(pollster/default) < 0.5.0~)
   F42 has 0.3 DONE
  Problem 5: nothing provides requested (crate(tokio/default) >= 1.47.1 with crate(tokio/default) < 2.0.0~)
  Problem 6: nothing provides requested (crate(tokio/io-util) >= 1.47.1 with crate(tokio/io-util) < 2.0.0~)


 RUNTIME DEP for jj-lib
  - nothing provides (crate(watchman_client/default) >= 0.9.0 with crate(watchman_client/default) < 0.10.0~) needed by rust-jj-lib+watchman-devel-0.32.0-1.fc44.noarch from @commandline
    Problem 1: nothing provides requested (crate(futures/compat) >= 0.3.13 with crate(futures/compat) < 0.4.0~)
     DONE
     compat support was dropped .... try to remove this feature? (and no build error, compat is used for https://docs.rs/futures/latest/futures/compat/index.html)
     so i think it is not a big problem?
     Interesting project for remvoe unused features : https://crates.io/crates/cargo-unused-features
    Problem 2: nothing provides requested (crate(serde_bser/default) >= 0.4.0 with crate(serde_bser/default) < 0.5.0~)
    DONE

Problem 7: nothing provides requested (crate(pollster/default) >= 0.4.0 with crate(pollster/default) < 0.5.0~)
 F42 has 0.3 DONE
<!-- Problem 8: nothing provides requested (crate(proptest-state-machine/default) >= 0.3.1 with crate(proptest-state-machine/default) < 0.4.0~) [REQUIRED FOR TEST] -->
      <!-- drop message-io since it is only used for examples -->
<!--   Problem: nothing provides requested (crate(message-io/default) >= 0.18.0 with crate(message-io/default) < 0.19.0~) -->
<!--     Problem 1: nothing provides requested (crate(integer-encoding/default) >= 3.0.2 with crate(integer-encoding/default) < 4.0.0~) -->
<!--     Problem 2: nothing provides requested (crate(strum/default) >= 0.24.0 with crate(strum/default) < 0.25.0~) -->
<!--     Problem 3: nothing provides requested (crate(strum/derive) >= 0.24.0 with crate(strum/derive) < 0.25.0~) -->
<!--     Problem 4: nothing provides requested (crate(tungstenite/default) >= 0.22.0 with crate(tungstenite/default) < 0.23.0~) -->
<!--     Problem 5: nothing provides requested (crate(tungstenite/url) >= 0.22.0 with crate(tungstenite/url) < 0.23.0~) -->

Problem 9: nothing provides requested (crate(rpassword/default) >= 7.4.0 with crate(rpassword/default) < 8.0.0~)
 F42 has 7.3 DONE
Problem 10: nothing provides requested (crate(sapling-renderdag/default) >= 0.1.0 with crate(sapling-renderdag/default) < 0.2.0~)
 Problem: nothing provides requested (crate(sapling-drawdag/default) >= 0.1.0 with crate(sapling-drawdag/default) < 0.2.0~)
 No match for argument: crate(unicode-width/default) = 0.1.12
  no 0.1.14 .... https://github.com/facebook/sapling/commit/6c23118ed1431c17c4497ac6a4141bbbf71fbe56
  so we must downgrade it manually
   Failed to pass test with dep  unicode-normalization v0.1.24
    so backport unicode-normalization to 0.1.23
Problem 11: nothing provides requested (crate(sapling-streampager/default) >= 0.11.0 with crate(sapling-streampager/default) < 0.12.0~)
 DONE
 No match for argument: crate(lru) = 0.12.4
  Try to ease it with remove "=" may not work , see comment: https://github.com/facebook/sapling/commit/06c6da67b1ad11d137130d561451d10396c20987
    since hashbrown is compilable now ;  `hashbrown 0.15.2`,  which fails to compile until Rust [1.84]
 Problem 1: nothing provides requested (crate(dirs/default) >= 6.0.0 with crate(dirs/default) < 7.0.0~)
 DONE
  Problem: nothing provides requested (crate(dirs-sys/default) >= 0.5.0 with crate(dirs-sys/default) < 0.6.0~)
  DONE
 Problem 2: nothing provides requested (crate(termwiz/default) >= 0.23.0 with crate(termwiz/default) < 0.24.0~)

   Problem 1: nothing provides requested (crate(finl_unicode/default) >= 1.2.0 with crate(finl_unicode/default) < 2.0.0~)
    DONE drop criterion 
   Problem 2: nothing provides requested (crate(vtparse/default) >= 0.6.2 with crate(vtparse/default) < 0.7.0~)
    DONE modify to set k9 from 0.11 to 0.12
    Problem: nothing provides requested (crate(k9/default) >= 0.11.0 with crate(k9/default) < 0.12.0~)
    DONE 
   Problem 3: nothing provides requested (crate(wezterm-bidi/default) >= 0.2.3 with crate(wezterm-bidi/default) < 0.3.0~)
    DONE 
        (crate(wezterm-dynamic/default) >= 0.2.0 with crate(wezterm-dynamic/default) < 0.3.0~) is needed by rust-wezterm-bidi-0.2.3-1.fc44.x86_64
   Problem 4: nothing provides requested (crate(wezterm-blob-leases/default) >= 0.1.1 with crate(wezterm-blob-leases/default) < 0.2.0~)
    DONE
   Problem 5: nothing provides requested (crate(wezterm-color-types/default) >= 0.3.0 with crate(wezterm-color-types/default) < 0.4.0~)
     DONE
     Problem 1: nothing provides requested (crate(deltae/default) >= 0.3.0 with crate(deltae/default) < 0.4.0~)
      DONE
     Problem 2: nothing provides requested (crate(wezterm-dynamic/default) >= 0.2.0 with crate(wezterm-dynamic/default) < 0.3.0~)
   Problem 6: nothing provides requested (crate(wezterm-dynamic/default) >= 0.2.1 with crate(wezterm-dynamic/default) < 0.3.0~)
      DONE
      Problem: nothing provides requested (crate(wezterm-dynamic-derive/default) >= 0.1.1 with crate(wezterm-dynamic-derive/default) < 0.2.0~)
       DONE
   Problem 7: nothing provides requested (crate(wezterm-input-types/default) >= 0.1.0 with crate(wezterm-input-types/default) < 0.2.0~)
     DONE
     Problem: nothing provides requested (crate(wezterm-dynamic/default) >= 0.2.0 with crate(wezterm-dynamic/default) < 0.3.0~)

   Problem 1: nothing provides requested (crate(criterion/default) >= 0.5.0 with crate(criterion/default) < 0.6.0~)
   Problem 2: nothing provides requested (crate(k9/default) >= 0.12.0 with crate(k9/default) < 0.13.0~)
   Problem 3: nothing provides requested (crate(varbincode/default) >= 0.1.0 with crate(varbincode/default) < 0.2.0~)

Problem 12: nothing provides requested (crate(scm-record/default) >= 0.8.0 with crate(scm-record/default) < 0.9.0~)
 DONE skip criterion
Problem 13: nothing provides requested (crate(tokio/default) >= 1.47.1 with crate(tokio/default) < 2.0.0~)
 F42 have 1.47.0 wait until 1.47.1 from testing to ...
Problem 14: nothing provides requested (crate(tokio/io-util) >= 1.47.1 with crate(tokio/io-util) < 2.0.0~)
 F42 have 1.47.0
