##Remove examples and autoexamples option in generated cargo.toml
##due to examples build fail (which is caused by using ratatui::terminal which is private)

1. from ratatui 0.28+ https://github.com/ratatui/ratatui/commit/84cb16483a76f1eb28f31f4a99075edfd78635f4
terminal is private

so we force ratatui-image use 0.26 by editing metadata

from
```

[dependencies.ratatui]
version = ">=0.23"
```
to
```
[dependencies.ratatui]
version = ">=0.23,<0.28"
```

2. doctest require assets/Ada.png which is excluded in crates
ignore it like https://src.fedoraproject.org/rpms/rust-tokio/blob/rawhide/f/0001-skip-one-doctest-that-pulls-in-an-additional-depende.patch
