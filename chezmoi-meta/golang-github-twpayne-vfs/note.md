1. go2rpm  --download -d -L github.com/twpayne/go-vfs -v 5
2. edit -> no check

upstream test failled too

NOTE: test under root will make (the subfolder still accessible by root even after `chmod 0 subfolder`)
