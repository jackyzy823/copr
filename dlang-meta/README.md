1. About debug info for package's dub.json targetType executable 

debug info seem not works with D compiler from https://src.fedoraproject.org/rpms/gtkd

However if you read dub's document carefully, there's a solution: To include debug info , use --build=release-debug in dub build

## see https://dub.pm/dub-reference/build_settings/#buildoptions
## and https://dub.pm/dub-reference/buildtypes/#-buildrelease-debug

Or if you don't care about debug info
add %global debug_package %{nil} in spec file

2. About source:

# Reference:    https://github.com/dlang/dub/blob/0030b9af02481fb518419bb4e13dd18731a9fd4f/source/dub/packagesuppliers/registry.d#L65

# or https://codemirror.dlang.org

and

https://github.com/dlang/dub-registry

# since code.dlang.org url is just a 302 redirect to github/gitlab , so we could use github/gitlab directly.

3. About dubhash
for the package use dubhash to calculate version.
we must craft a build dir like <version>/<packagename>-<version>/<source code> to make dubhash happy
so
`%setup -C -n %{_version}/%{name}-%{_version}` is the solution


4. Aout d-rpm-macros desgin
a) create a dub2rpm for fetching the init one and create .spec -> add BuildRequries: ldc/dub/d-rpm-macros
dub2rpm xxxx -> find the latest version (use dub registry api https://code.dlang.org/api/packages/<packagename>/info) and download
use ninja2 and template ....
use dub convert to convenrt dub.sdl to dub.json for read

b) create a d-rpm-macros and (d-srpm-macros if we decide use /usr/share/dub/packages/....)


