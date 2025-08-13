Fix check:
update brotli from 1.1 to 1.2 (also brotli requires new dependency:   golang-github-xyproto-randomstring)

Ref:
https://github.com/mholt/archives/issues/29
https://github.com/andybalholm/brotli/issues/58


--------------------

golang-github-nwaples-rardecode2 is not included in f41
so build https://src.fedoraproject.org/rpms/golang-github-nwaples-rardecode2/ with `copr-cli -r fedora-41-x86_64`
