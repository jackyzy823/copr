remove feature `windows` of dependency `crossterm`.


Some tests failed:


# note session has 1 passed test,

-- -- --skip live_wait_for_next_ignores_history_and_matches_split_future_output \
--skip wait_for_text_observes_rendered_daemon_output \
--skip rmux_sdk_cargo_manifest_does_not_depend_on_internal_crates \
--skip rmux_sdk_cargo_manifest_does_not_redeclare_proto_in_dev_dependencies \
--skip rmux_sdk_tokio_dependency_stays_narrow_async_io_plumbing

and delete this tests in Cargo.toml
layout_builder
lifecycle
pane_input
pane_queries
pane_set
session
smoke_v1
smoke_v1_full
terminal_automation
window 



require self build rmux server

failures:
    live_wait_for_next_ignores_history_and_matches_split_future_output

test result: FAILED. 10 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.08s

error: test failed, to rerun pass `--test armed_wait`
     Running `/pkg/rmux-meta/rust-rmux-sdk/rust-rmux-sdk-0.3.0-build/rmux-sdk-0.3.0/target/rpm/deps/contract-755a5068135e4888`

failures:
    layout_builder_creates_incomplete_grid_with_process_options
    layout_builder_rejects_unsafe_or_invalid_requests

test result: FAILED. 0 passed; 2 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.02s

error: test failed, to rerun pass `--test layout_builder`
     Running `/pkg/rmux-meta/rust-rmux-sdk/rust-rmux-sdk-0.3.0-build/rmux-sdk-0.3.0/target/rpm/deps/lifecycle-5a175255a8958ebb`


failures:
    owned_session_cleanup_kills_session_explicitly
    owned_session_cleanup_updates_lease_state_receiver
    owned_session_owner_exit_lease_renews_and_release_prevents_reaper
    owned_session_preserve_detaches_without_cleanup
    owned_session_rejects_too_short_lease_ttl_before_creation
    owned_session_signal_handlers_are_opt_in_and_unique
    pane_close_and_respawn_preserve_slot_semantics
    spawn_keep_alive_keeps_dead_pane_with_exit_state
    spawn_single_argv_binary_is_direct_and_shell_is_explicit
    split_with_spawn_keep_alive_keeps_dead_child_pane

test result: FAILED. 0 passed; 10 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.02s

error: test failed, to rerun pass `--test lifecycle`
     Running `/pkg/rmux-meta/rust-rmux-sdk/rust-rmux-sdk-0.3.0-build/rmux-sdk-0.3.0/target/rpm/deps/pane_input-173788e68f8cf92e`

failures:
    broadcast_reports_partial_failures_by_pane
    broadcast_sends_text_and_keys_to_multiple_panes
    input_and_resize_return_daemon_errors_for_stale_or_missing_panes
    pane_by_id_survives_index_recompression_for_critical_input_and_snapshot
    render_stream_emits_snapshot_after_output
    resize_updates_geometry_and_emits_window_layout_change
    send_text_is_literal_and_send_key_interprets_key_tokens

test result: FAILED. 0 passed; 7 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.02s

error: test failed, to rerun pass `--test pane_input`
     Running `/pkg/rmux-meta/rust-rmux-sdk/rust-rmux-sdk-0.3.0-build/rmux-sdk-0.3.0/target/rpm/deps/pane_queries-7acc303c2808a0ae`



failures:
    pane_id_info_and_snapshot_resolve_through_daemon_for_live_and_stale_slots
    pane_id_resolves_to_same_identity_through_grouped_session_views
    pane_id_resolves_to_same_identity_through_linked_window_views
    pane_snapshot_revision_changes_after_output_resize_clear_and_exit

test result: FAILED. 0 passed; 4 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.02s

error: test failed, to rerun pass `--test pane_queries`
     Running `/pkg/rmux-meta/rust-rmux-sdk/rust-rmux-sdk-0.3.0-build/rmux-sdk-0.3.0/target/rpm/deps/pane_set-ff6129237a65d438`


failures:
    pane_set_broadcast_snapshot_and_visible_waits
    pane_set_close_all_reports_per_pane_outcomes

test result: FAILED. 0 passed; 2 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.02s

error: test failed, to rerun pass `--test pane_set`
     Running `/pkg/rmux-meta/rust-rmux-sdk/rust-rmux-sdk-0.3.0-build/rmux-sdk-0.3.0/target/rpm/deps/session-03d42f900df458ae`



failures:
    create_only_builds_live_session_and_hides_process_environment
    create_only_duplicate_is_error_but_attach_if_exists_reuses
    ensure_session_command_preserves_legacy_and_explicit_modes_are_clear
    explicit_endpoint_timeout_and_empty_tag_semantics_are_preserved
    invalid_environment_override_diagnostic_is_redacted
    reuse_only_policy_never_creates_sessions

test result: FAILED. 1 passed; 6 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.02s

error: test failed, to rerun pass `--test session`


failures:
    daemon_backed_sdk_happy_path_cleans_tmp_socket_lock_daemon_and_child

test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.02s

error: test failed, to rerun pass `--test smoke_v1`
     Running `/pkg/rmux-meta/rust-rmux-sdk/rust-rmux-sdk-0.3.0-build/rmux-sdk-0.3.0/target/rpm/deps/smoke_v1_full-b2fcb8940ef1ced3`


failures:
    ci_runner_collects_command_output_and_exit
    ci_runner_collects_immediate_burst_output_oldest_without_keepalive
    ci_runner_collects_initial_process_burst_oldest_without_keepalive
    ci_runner_streams_immediate_burst_output_without_keepalive
    dashboard_snapshot_updates_are_revision_gated
    failure_cleanup_uses_existing_typed_diagnostics
    interactive_repl_waits_for_prompt_and_interrupts
    rust_app_autostarts_and_drives_a_session
    sdk_autostarted_daemon_detaches_and_survives_terminal_signals
    sdk_daemon_continues_stopped_initial_pane_process
    sdk_daemon_recreates_removed_socket_on_sigusr1
    warm_reconnect_keeps_existing_runtime

test result: FAILED. 0 passed; 12 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.02s

error: test failed, to rerun pass `--test smoke_v1_full`
     Running `/pkg/rmux-meta/rust-rmux-sdk/rust-rmux-sdk-0.3.0-build/rmux-sdk-0.3.0/target/rpm/deps/smoke_v1_full_windows-cc3bf5fb1a74ac0c`


failures:
    terminal_automation_layer_drives_the_p3_user_flow

test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.02s

error: test failed, to rerun pass `--test terminal_automation`
     Running `/pkg/rmux-meta/rust-rmux-sdk/rust-rmux-sdk-0.3.0-build/rmux-sdk-0.3.0/target/rpm/deps/value_objects-d274ecc152759ff8`

failures:
    wait_for_text_observes_rendered_daemon_output

test result: FAILED. 14 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.05s

error: test failed, to rerun pass `--test wait`
     Running `/pkg/rmux-meta/rust-rmux-sdk/rust-rmux-sdk-0.3.0-build/rmux-sdk-0.3.0/target/rpm/deps/window-17d19664c6dbe0e2`

failures:
    window_close_removes_linked_window_from_every_affected_listing
    window_close_synchronizes_grouped_session_listings
    window_split_info_pane_listing_ids_and_idempotent_close_use_daemon_paths
    window_split_through_linked_target_updates_every_linked_view

test result: FAILED. 0 passed; 4 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.02s

error: test failed, to rerun pass `--test window`




requrie rmux-sdk Cargo.toml must declare a [dependencies] section


rmux_sdk_cargo_manifest_does_not_depend_on_internal_crates
rmux_sdk_cargo_manifest_does_not_redeclare_proto_in_dev_dependencies
rmux_sdk_tokio_dependency_stays_narrow_async_io_plumbing


failures:
    rmux_sdk_cargo_manifest_does_not_depend_on_internal_crates
    rmux_sdk_cargo_manifest_does_not_redeclare_proto_in_dev_dependencies
    rmux_sdk_tokio_dependency_stays_narrow_async_io_plumbing

test result: FAILED. 10 passed; 3 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

error: test failed, to rerun pass `--test identity`
     Running `/pkg/rmux-meta/rust-rmux-sdk/rust-rmux-sdk-0.3.0-build/rmux-sdk-0.3.0/target/rpm/deps/info-7ca9fc49b0feb693`


