sapling-drawdag use pinned unicode-width==0.1.12

due to https://github.com/facebook/sapling/commit/6c23118ed1431c17c4497ac6a4141bbbf71fbe56
  so we must downgrade it manually


however it Failed to pass test with dep  unicode-normalization v0.1.24
    so backport unicode-normalization to 0.1.23
   and use "=" to pin 0.1.23 in unicode-width Cargo.toml
