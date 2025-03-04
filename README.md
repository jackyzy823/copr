* Prebuilt package

    `dnf copr enable jackyzy823/myown && dnf install <package>`

* Build

    `dnf install fedora-packager`
    `cd <subpackage>`
    `dnf builddep <package>.spec`
    `spectool -g <package>.spec`
    `sha512sum --tag <package> > sources`
    `fedpkg --release=rawhide local` # or  `rpmbuild -ba <package>.spec  --define "_topdir ."  --define "_sourcedir ." --define "_srcrpmdir ."`

* Some tricks for packaging rust dependencies.

    `spectool -g *.spec && dnf builddep -y *.spec && ( fedpkg local || (dnf install -y *.nosrc.rpm && fedpkg local)) && dnf install noarch/*.rpm -y`
