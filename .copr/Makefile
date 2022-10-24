srpm:
	dnf install rpmdevtools -y
	spectool -g $(spec) && rpmbuild -bs $(spec)  --define "_topdir ."  --define "_sourcedir ." --define "_srcrpmdir $(outdir)"
