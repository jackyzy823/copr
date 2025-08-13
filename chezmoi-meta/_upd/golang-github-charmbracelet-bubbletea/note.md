RPM build errors:
    Empty %files file golang-github-charmbracelet-bubbletea/golang-github-charmbracelet-bubbletea-1.3.6-build/bubbletea-1.3.6/debugsourcefiles.list 


golang-github-fogleman-ease is required by examples only

refer to  https://src.fedoraproject.org/rpms/golang-github-charmbracelet-bubbletea
	
# Remove to avoid extra deps
rm -rf examples tutorials
