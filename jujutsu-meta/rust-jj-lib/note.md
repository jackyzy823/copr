 RUNTIME DEP for jj-lib
  - nothing provides (crate(watchman_client/default) >= 0.9.0 with crate(watchman_client/default) < 0.10.0~) needed by rust-jj-lib+watchman-devel-0.32.0-1.fc44.noarch from @commandline


Skip tests
due to 
0. it requries criterion
1. failed to compile test (even under an extracted jj-lib.crate folder)
1) missing "tree-editor" feature for gix and it will complains:
error[E0599]: no method named `edit` found for struct `gix::Tree` in the current scope
    --> src/git_backend.rs:1692:57
     |
1692 |         let mut dir_tree_editor = git_repo.empty_tree().edit().unwrap();
     |                                                         ^^^^ method not found in `Tree<'_>`

error[E0599]: no method named `edit` found for struct `gix::Tree` in the current scope
    --> src/git_backend.rs:1700:59
     |
1700 |         let mut root_tree_builder = git_repo.empty_tree().edit().unwrap();
     |                                                           ^^^^ method not found in `Tree<'_>`

error[E0599]: no method named `edit` found for struct `gix::Tree` in the current scope
    --> src/git_backend.rs:2127:58
     |
2127 |             let mut tree_builder = git_repo.empty_tree().edit().unwrap();
     |                                                          ^^^^ method not found in `Tree<'_>`


although we could do -p to add tree-editor to dep gix , but it is only for testing.
https://github.com/rust-lang/cargo/issues/2911#issuecomment-1483256987

2) missing dev-dep testutils (not in Cargo.toml but in Cargo.toml.orig) 
BECAUSE IT IS A INTERNAL LIB!! see jj/lib/testutils "Integration test utils for the jj-lib crate
3) test are gated behind cfg(feature = "testing")
note: the item is gated behind the `testing` feature
   --> /root/pkg/rust-jj-lib/rust-jj-lib-0.32.0-build/jj-lib-0.32.0/src/lib.rs:99:7
    |
99  | #[cfg(feature = "testing")]
    |       ^^^^^^^^^^^^^^^^^^^
