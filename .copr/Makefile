srpm:
	dnf install rpmdevtools -y
	spectool -g plasma-breath.spec && rpmbuild -bs plasma-breath.spec  --define "_topdir ."  --define "_sourcedir ." --define "_srcrpmdir $(outdir)"
