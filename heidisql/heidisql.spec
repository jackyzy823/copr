Name: heidisql
Version: 12.11.1.167
Release: %autorelease
Summary: A lightweight client for managing MariaDB, MySQL, SQL Server, PostgreSQL, SQLite, Interbase and Firebird, written in Delphi

#TODO Icons added in January 2019 into a TImageCollection component are copyright by Icons8.
#     This might be a license issue.
#     see source/main.lfm -> ImageListIcon8: TImageList
License: GPL-2.0-only
URL: https://github.com/HeidiSQL/HeidiSQL/tree/lazarus
Source: https://github.com/HeidiSQL/HeidiSQL/archive/refs/tags/%{version}.tar.gz

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
install -m 0644 out/*.ini %{buildroot}%{_datadir}/heidisql/
#install binary file
install -m 0755 out/heidisql %{buildroot}%{_datadir}/heidisql/

install -D -m 0755 deb-package-skeleton/usr/bin/heidisql %{buildroot}%{_bindir}/heidisql

#install -d -m 0755 %{buildroot}%{_datadir}/pixmaps/
install -D -m 0644 res/deb-package-icon.png %{buildroot}%{_datadir}/pixmaps/heidisql.png

install -D -m 0644 deb-package-skeleton/usr/share/applications/heidisql.desktop %{buildroot}%{_datadir}/applications/heidisql.desktop

install -D -m 0644 deb-package-skeleton/usr/share/doc/heidisql/copyright %{buildroot}%{_docdir}/heidisql/copyright


%files
%license LICENSE
%{_bindir}/heidisql
%{_datadir}/heidisql/
%{_datadir}/applications/heidisql.desktop 
%{_datadir}/pixmaps/heidisql.png 
%{_docdir}/heidisql/

%changelog
%autochangelog

