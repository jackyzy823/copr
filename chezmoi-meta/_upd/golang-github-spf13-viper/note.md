Why upgrade this

golang-github-spf13-viper 1.19 requires golang(github.com/sagikazarmark/crypt/config)  --->  golang(github.com/hashicorp/consul/api)  -->  golang(github.com/hashicorp/serf/serf)·

 golang(github.com/hashicorp/consul/api)   Orphaned from f43
f43    golang(github.com/hashicorp/serf/serf)·  switch to go vendor
https://src.fedoraproject.org/rpms/golang-github-hashicorp-serf/c/36e5eef86a3094c2997169536c83e4abd5175baf?branch=rawhide

which do not provide
    No match for argument: golang(github.com/hashicorp/serf/coordinate)
    No match for argument: golang(github.com/hashicorp/serf/serf) 



upgrade olang-github-spf13-viper to 1.20+ to avoid   golang(github.com/sagikazarmark/crypt)
!!! and !!! you need to remove `remote` folder since it is not default !!!

as said in README.md
```
To enable remote support in Viper, do a blank import of the `viper/remote` 
package:

`import _ "github.com/spf13/viper/remote"`
```


