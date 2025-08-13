 go2rpm  --download -d -L github.com/zricethezav/gitleaks -v 8 -a github.com/zricethezav/gitleaks/v8

bootstrap 1
cannot find package "github.com/zricethezav/gitleaks/cmd/detect.go" in any of:                                                                                                                                             /usr/lib/golang/src/github.com/zricethezav/gitleaks/cmd/detect.go (from $GOROOT)                                                                                                                                   /root/pkg/golang-github-zricethezav-gitleaks/golang-github-zricethezav-gitleaks-8.28.0-build/gitleaks-8.28.0/_build/src/github.com/zricethezav/gitleaks/cmd/detect.go (from $GOPATH)                               /usr/share/gocode/src/github.com/zricethezav/gitleaks/cmd/detect.go


https://github.com/gitleaks/gitleaks/blob/master/cmd/detect.go is deprecated, consider not bootstrap 



it requires config/gitleaks.toml since it go embed it 


// so set global env gosupfiles
