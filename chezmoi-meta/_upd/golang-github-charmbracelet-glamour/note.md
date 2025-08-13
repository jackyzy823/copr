no check

--- FAIL: TestRenderer (0.01s)                                                                                                                                                                                                                                                
    --- FAIL: TestRenderer/table_align (0.00s)

--- FAIL: TestRendererIssues (0.02s)                                                                                                                                                                                                                                          
    --- FAIL: TestRendererIssues/316 (0.00s)                                                                                                                                                                                                                                          renderer_test.go:146: output does not match, expected:

error due to lipgloss not the latest
 
 lipgloss 1.1.1 no bug (but not released yet)
 lipgloss 1.1.0 has bug.


 update to 1.1.1 requires
 No match for argument: golang(github.com/charmbracelet/ssh)
No match for argument: golang(github.com/charmbracelet/wish)
No match for argument: golang(github.com/charmbracelet/wish/logging)
Package "golang-github-charmbracelet-x-ansi-devel-0.8.0-1.fc44.noarch" is already installed.
Package "golang-github-charmbracelet-x-cellbuf-devel-0.0.13-1.fc44.noarch" is already installed.
Package "golang-github-charmbracelet-x-exp-golden-devel-0-1.fc43.noarch" is already installed.
Package "golang-github-creack-pty-devel-1.1.24-1.fc43.noarch" is already installed.
Package "golang-github-lucasb-eyer-colorful-devel-1.2.0-12.fc42.noarch" is already installed.
No match for argument: golang(github.com/muesli/gamut)
Package "golang-github-muesli-termenv-devel-0.15.2-6.fc42.noarch" is already installed.
Package "golang-github-rivo-uniseg-devel-0.4.7-3.fc42.noarch" is already installed.
Package "golang-x-term-devel-0.26.0-2.fc42.noarch" is already installed.
Problem: cannot install both golang-github-creack-pty-devel-1.1.24-2.fc42.noarch from fedora and golang-github-creack-pty-devel-1.1.24-1.fc43.noarch from @System
  - installed package compat-golang-github-creack-pty2-devel-1.1.24-1.fc43.noarch requires golang-ipath(github.com/creack/pty) = 1.1.24-1.fc43, but none of the providers can be installed
  - cannot install the best candidate for the job
  - problem with installed package
You can try to add to command line:
  --skip-unavailable to skip unavailable packages



So we bypass the test for ansi/render_test via `gocheck -d ansi` for now
since it is just a style problem
