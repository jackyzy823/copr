toml is only used as a dev-dependency for checking DEPS.md listing all dependencies from `Cargo.toml`
see DEPS.md Used to test that this file lists all dependencies from `Cargo.toml`.

tests/deps.rs requires files from mono repo https://github.com/Lonami/grammers/

so remove
1. dev-dependency: toml in Cargo.toml
2. remove [[test]]
name = "deps"
path = "tests/deps.rs" in Cargo.toml

