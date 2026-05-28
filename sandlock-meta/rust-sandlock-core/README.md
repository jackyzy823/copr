1. rootfs-helper not found for tests
it is compiled from rootfs-helper.c which is not packaged in crate

---- test_determinism::test_hostname_virtualization stdout ----

thread 'test_determinism::test_hostname_virtualization' (508524) panicked at tests/integration/test_determinism.rs:216:5:
hostname command failed

requires `hostname`
