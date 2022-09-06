* Prebuilt package

    `dnf copr enable jackyzy823/myown && dnf install plasma-breath`

* Build

    `dnf install fedora-packager`
    `dnf builddep plasma.spec`
    `spectool -g plasma.spec`
    `fedpkg --release=rawhide local` # or  `rpmbuild -ba plasma-breath.spec  --define "_topdir ."  --define "_sourcedir ." --define "_srcrpmdir ."`
