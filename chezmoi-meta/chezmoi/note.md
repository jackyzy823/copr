
github.com/charmbracelet/bubbletea have 0.24.2 but require 1.3.6

github.com/twpayne/chezmoi/internal/chezmoibubbles
--- FAIL: TestIntInputModel (0.00s)
    --- FAIL: TestIntInputModel/one_invalid_enter (0.00s)
        intinputmodel_test.go:57: Expected values to be equal:
            -0
            +1
FAIL
exit status 1

--> 1 should be the right value ?? i think
upgrade https://github.com/charmbracelet/bubbles from 0.16 to 0.20 to pass the testhttps://github.com/charmbracelet/bubbles?tab=readme-ov-file

ldflags?
%global goldflags "-X main.version=%{version} -X main.builtBy=Copr" %{goldflags} 
This not work

failed to run internal/cmd/main_test.go 
testscript not found in "github.com/rogpeppe/go-internal/testscript" maybe version mismatch

require 1.14.1 , have 1.12.0
update to finish test


some test require internet , so we should skip tests. 
so should we update github.com/rogpeppe/go-internal/testscript (or just no?)


f43+ do not have golang-github-hashicorp-consul anymore , but it is required by golang-github-sagikazarmark-crypt

f41's github.com/goccy/go-yaml too old 1.11.3-2.fc41 which causing

            # test that the last operation broke chezmoi (0.023s)
            > ! exec chezmoi --config=$HOME/.chezmoi/athome.yaml status
            [stderr]
            chezmoi: invalid config: $WORK/home2/user/.chezmoi/athome.yaml: [1:1] sequence was used where mapping is expected
                >  1 | [data]
                       ^
                   2 |   email = "mail3@example.com"
            [exit status 1]
            > ! stdout .
            > cmpenv stderr golden/error2.log
            diff stderr golden/error2.log
            --- stderr
            +++ golden/error2.log
            @@ -1,4 +1,5 @@
            -chezmoi: invalid config: $WORK/home2/user/.chezmoi/athome.yaml: [1:1] sequence was used where mapping is expected
            -    >  1 | [data]
            -           ^
            -       2 |   email = "mail3@example.com"
            +chezmoi: invalid config: $WORK/home2/user/.chezmoi/athome.yaml: [2:3] value is not allowed in this context
            +   1 | [data]
            +>  2 |   email = "mail3@example.com"
            +         ^
            +
            
            FAIL: testdata/scripts/initconfig.txtar:59: stderr and golden/error2.log differ

fedora 42 have 0.15 -> but chezmoi require 0.18 , so we update it for both releases (f41,f42)
fedora 43+ has 0.18

--------------


It looks like tty not work correctly. input prompt has a single char .   use `--no-tty` (maybe docker issue?)


The original one 
show
Enter pwd:<the gray hint>

But we only show the first char of the hint and it is not gray.....

This may releated to $TERM, add $TERM to docker -e , copr one will have a gray "first char" ,  but the prebuilt one do not have this issue.

so may not related to lipgloss

it looks like bubble 0.21.0 if m.Width + 1 of model is used to calcute placeholder ( so 1 for width unset) , but bubble 0.20.0 (chezmoi exact dep) not do so
so downgrade bubble to 0.20.0

(tested downgrade works) the chars show fully

but color still not right under docker env
may be https://github.com/muesli/termenv/pull/171
(yes ,tested upgrade to termenv from 0.15.2 to 0.16 works)

====================
in f43+ 
age use go vendor (and for gopass..)
gojq use go vendor
ov use go vendor (for gopass)

so we create own golang-xxxx-age/gojq/ov-devel from f41 ....
age-1.2.1 could use https://src.fedoraproject.org/rpms/age/c/065a1cbe1e5099b21aeab15e1dc802b1d5fb81fa?branch=rawhide as  a refer version same and the latest non-vendor one
ov@v0.40.1 create own --> use 0.41.0 to avoid 0.40.0 build fail due to test fail due to tcellansi use 0.1.0 instead of v0.0.0-20250320075053-376e9cb3c42b 
gojq@v0.12.17 use https://src.fedoraproject.org/rpms/gojq/c/2226a5d2b626b9ac4d1cf72bcd71400d922a5971?branch=rawhide as a ref
