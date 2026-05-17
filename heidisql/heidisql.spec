Name: heidisql
Version: 12.17
Release: %autorelease
Summary: A lightweight client for managing MariaDB, MySQL, SQL Server, PostgreSQL, SQLite, Interbase and Firebird, written in Delphi

#TODO Icons added in January 2019 into a TImageCollection component are copyright by Icons8.
#     This might be a license issue.
#     see source/main.lfm -> ImageListIcon8: TImageList
License: GPL-2.0-only
URL: https://www.heidisql.com
Source: https://github.com/HeidiSQL/HeidiSQL/archive/%{version}/HeidiSQL-%{version}.tar.gz

BuildRequires: lazarus-tools
BuildRequires: lazarus-lcl-gtk2

Requires: libpq
Requires: mariadb-connector-c
Requires: sqlite-libs

# Recommends: Enhances: Suggests: Supplements: mysql-libs or mysql8.4-libs

# not supported yet: libfbclient2
# not supported yet: freetds

%description
%{summary}

%prep
%autosetup -n HeidiSQL-%{version} -p1
## NOTE: failed to compile on rawhide( rpm --eval "%{?fedora}" == 44 on rawhide) due to fpc-3.2.4~rc1
# /builddir/build/BUILD/heidisql-12.12-build/HeidiSQL-12.12-Linux/./source/dbconnection.pas(229,14) Error: (3029) function header doesn't match the previous declaration "Compare(constref TDBObject;constref TDBObject):LongInt;"
# /usr/lib64/fpc/3.2.3/units/x86_64-linux/rtl-generics/generics.defaults.ppu:generics.defaults.pas(55,14) Error: (5088) Found declaration: Compare(const TDBObject;const TDBObject):LongInt;
## See : https://github.com/HeidiSQL/HeidiSQL/blob/12.12-Linux/source/dbconnection.pas#L229
## on fpc-3.2.4~rc1 FPC_FULLVERSION is still 30203, so heidisql require constref , but in generics.defaults.pas it is const 
## fpcsrc/compiler/version.pas:       patch_nr   = '3';
## fpcsrc/compiler/options.pas:  set_system_macro('FPC_FULLVERSION',Format('%d%.02d%.02d',[StrToInt(version_nr),StrToInt(release_nr),StrToInt(patch_nr)]));
## Ref:https://forum.lazarus.freepascal.org/index.php/topic,56864.msg544945.html#msg544945

## More failed: /builddir/build/BUILD/heidisql-12.12-build/HeidiSQL-12.12-Linux/./source/grideditlinks.pas(1844,47) Error: (4001) Incompatible types: got "TFontStyles" expected "Set Of TFontStyle"
## maybe related to lazarus-lcl-gtk2
## components/lazutils/graphtype.pp
##{$if FPC_FULLVERSION>=30203}
##{$define UseSystemUITypes}
##{$endif}

## removing `use System.UITypes` in heidisql helps
## TODO: change this with patch and change autosetup to setup and do patch only fedora > 43

# https://github.com/HeidiSQL/HeidiSQL/issues/2337 freebsd guys find the similar issue, and their fix breaks my sed (no space after comma)
%if 0%{?fedora} > 43
sed -i 's|FPC_FULLVERSION<30204|FPC_FULLVERSION<30203|' source/*.pas
sed -i 's|System.UITypes,||' source/grideditlinks.pas source/table_editor.pas
%endif

# fix rpath issue
# This '@loader_path/../Frameworks' should only be used for mac app.
sed -i '/<LinkerOptions Value="-rpath @loader_path\\..\\Frameworks"\/>/d' heidisql.lpi

%build
# inject version string to lpi file
sed -i "s/<BuildNr Value=\"[0-9]\+\"/<BuildNr Value=\"%{version}\"/g" heidisql.lpi
lazbuild --ws=gtk2 heidisql.lpi
## TODO fetch .po translation file from transifex and compile to .mo
# however po files are downloaded from transifex.com via cli client (tx) and it requires API token.
# we can extract the compiled mo? from  the linux precompiled pacakge from heidisql download page 

%install
install -d -m 0755 %{buildroot}%{_datadir}/heidisql/

#install ini
install -m 0644 extra/ini/*.ini %{buildroot}%{_datadir}/heidisql/

# .mo is included in release tar file now, so we can package it without .tx client (requires internet and account).
# not installing to /usr/share/locale/*/LC_MESSAGES/ so can't use find_lang macro
install -d -m 0755 %{buildroot}%{_datadir}/heidisql/locale
install -m 0644 extra/locale/*.mo %{buildroot}%{_datadir}/heidisql/locale
#install binary file
install -m 0755 out/heidisql %{buildroot}%{_datadir}/heidisql/

install -D -m 0755 package-skeleton/usr/bin/heidisql %{buildroot}%{_bindir}/heidisql

#install -d -m 0755 %{buildroot}%{_datadir}/pixmaps/
install -D -m 0644 res/deb-package-icon.png %{buildroot}%{_datadir}/pixmaps/heidisql.png

install -D -m 0644 package-skeleton/usr/share/applications/heidisql.desktop %{buildroot}%{_datadir}/applications/heidisql.desktop


%files
%license LICENSE package-skeleton/usr/share/doc/heidisql/copyright
%doc README.md
%{_bindir}/heidisql
%{_datadir}/heidisql/
%{_datadir}/applications/heidisql.desktop
%{_datadir}/pixmaps/heidisql.png

%changelog
%autochangelog

