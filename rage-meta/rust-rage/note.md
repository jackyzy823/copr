1 edit devdep trycmd from 0.14 to 0.15
2. edit dep time from range to "0.3.7" the reason for the range is MSRV , but we have the higher Rust version, so the range is not necessary
https://github.com/str4d/rage/blob/v0.11.1/rage/Cargo.toml#L126
3. console f41 has 0.15 (0.16 in testing) f42+ has 0.16 , to build on both platform change conosle from "0.15" to "0.16" (after testing -> stable)
and add features = ["std"]
see changelog https://github.com/console-rs/console/releases/tag/0.16.0 "The 0.16.0 API should be semver-compatible with the 0.15.x API except for the need for the std feature."


add BuildRequires:  pkgconfig(fuse3)
