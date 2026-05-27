Build dependency `embed-manifest` is used for windows build

ease `clap` version restriction

remove build="build.rs"

add `rm build.rs` in %prep

new_session_trailing_shell_command_spawns_initial_pane_command may failed on copr may be due to heavy load
`sleep 30` is done and the next line check instruction still not be executed.

since rmux is binary, must pin deps rust-* version exactly , otherwise build will failed

ie build rmux 0.3.0 with deps rmux-* 0.3.1

```
error[E0061]: this method takes 4 arguments but 3 arguments were supplied
   --> src/cli/config_commands.rs:102:10
    |
102 |         .show_options(scope, args.name, args.value_only)
    |          ^^^^^^^^^^^^----------------------------------- argument #4 of type `bool` is missing
    |
note: method defined here
   --> /usr/share/cargo/registry/rmux-client-0.3.1/src/commands/config.rs:129:12
    |
129 |     pub fn show_options(
    |            ^^^^^^^^^^^^
help: provide the argument
    |
102 |         .show_options(scope, args.name, args.value_only, /* bool */)
    |                                                        ++++++++++++

error[E0063]: missing field `client_environment` in initializer of `NewSessionExtRequest`
  --> src/cli/session_commands.rs:33:31
   |
33 |         .new_session_extended(NewSessionExtRequest {
   |                               ^^^^^^^^^^^^^^^^^^^^ missing `client_environment`
```
