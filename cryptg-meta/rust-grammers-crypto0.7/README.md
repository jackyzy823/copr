toml is only used as a dev-dependency for checking DEPS.md listing all dependencies from `Cargo.toml`
see DEPS.md Used to test that this file lists all dependencies from `Cargo.toml`.

tests/deps.rs requires files from mono repo https://github.com/Lonami/grammers/

so remove
1. dev-dependency: toml in Cargo.toml
2. (for 0.7) add `autotests = false` in Cargo.toml

Since crytpg requires grammers-crypt@0.7.0, so we downgrade it.
and you need to add `autotests = false` in Cargo.toml, to make rust not run tests from tests/ folder

