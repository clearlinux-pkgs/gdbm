#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gdbm
Version  : 1.12
Release  : 15
URL      : ftp://ftp.gnu.org/gnu/gdbm/gdbm-1.12.tar.gz
Source0  : ftp://ftp.gnu.org/gnu/gdbm/gdbm-1.12.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-3.0 GPL-3.0+
Requires: gdbm-bin
Requires: gdbm-lib
Requires: gdbm-doc
Requires: gdbm-locales
BuildRequires : bison
BuildRequires : flex

%description
See the end of file for copying conditions.
* Introduction
This file contains brief information about configuring, testing
and using GNU dbm.  It is *not* intended as a replacement
for the documentation, instead it is provided as a brief reference
only. The complete documentation is available in doc/ subdirectory.
To read the manpage without installing the package use `man
doc/gdbm.3'.  To read texinfo documentation without installing the
package, run `info -f doc/gdbm.info'.  After the package is installed
the documentation can be accessed by running `man gdbm' and
`info gdbm'.

%package bin
Summary: bin components for the gdbm package.
Group: Binaries

%description bin
bin components for the gdbm package.


%package dev
Summary: dev components for the gdbm package.
Group: Development
Requires: gdbm-lib
Requires: gdbm-bin
Provides: gdbm-devel

%description dev
dev components for the gdbm package.


%package doc
Summary: doc components for the gdbm package.
Group: Documentation

%description doc
doc components for the gdbm package.


%package lib
Summary: lib components for the gdbm package.
Group: Libraries

%description lib
lib components for the gdbm package.


%package locales
Summary: locales components for the gdbm package.
Group: Default

%description locales
locales components for the gdbm package.


%prep
%setup -q -n gdbm-1.12

%build
export LANG=C
%configure --disable-static --enable-libgdbm-compat
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang gdbm

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gdbm_dump
/usr/bin/gdbm_load
/usr/bin/gdbmtool

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*

%files locales -f gdbm.lang 
%defattr(-,root,root,-)

