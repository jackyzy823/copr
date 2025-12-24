1. Use /usr/bin/cargo2rpm --path Cargo.toml buildrequires --with-check to generate build requires

Use `cargo vendor` to save all dependes in `vendor` folder

and add
```
[source.crates-io]
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "vendor"
```
to Cargo.toml

Use `cargo tree` to show dependency tree.

TODO: how to exclude optional ??

Refer to cargo2rpm ->  rpm.py semver.py
semver2rpm

1. How to recursively resolve ?



2. How to programatically resolve "(crate(pkg/default) >= ver with crate(pkg/default) < ver+1~)"

import dnf
base = dnf.Base()
base.read_all_repos()
base.fill_sack()
base.sack.query().filter(provides="(crate(pkg/default) >= ver with crate(pkg/default) < ver+1~)").run()

Note: to use dnf under venv, you need to initialize with `--system-site-packages`

TODO:
use libdnf5 (only available with dnf install python3-libdn5)  the one on pypi is just a stub.

see blog "Using DNF5 API after running a transaction" https://jan-kolarik.github.io/posts/dnf5-api-after-transaction
and dnf5 tutorial: language bindings

import libdnf5
base.load_config()
base.setup()
sack = base.get_repo_sack()
sack.create_repos_from_system_configuration()
sack.load_repos()
q = libdnf5.rpm.PackageQuery(base)
q.filter_name("git")
for i in q:
    print(i.get_nevra())


use rust2rpm .... -> then fed prep -> then cargo2rpm ... buildrequire 
--> display 
