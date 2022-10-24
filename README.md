* Prebuilt package

    `dnf copr enable jackyzy823/myown && dnf install <package>`

* Build

    `dnf install fedora-packager`
    `cd <subpackage>`
    `dnf builddep <package>.spec`
    `spectool -g <package>.spec`
    `fedpkg --release=rawhide local` # or  `rpmbuild -ba <package>.spec  --define "_topdir ."  --define "_sourcedir ." --define "_srcrpmdir ."`
