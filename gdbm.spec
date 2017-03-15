#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3602B07F55D0C732 (gray@gnu.org)
#
Name     : gdbm
Version  : 1.13
Release  : 19
URL      : ftp://ftp.gnu.org/gnu/gdbm/gdbm-1.13.tar.gz
Source0  : ftp://ftp.gnu.org/gnu/gdbm/gdbm-1.13.tar.gz
Source99 : ftp://ftp.gnu.org/gnu/gdbm/gdbm-1.13.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-3.0 GPL-3.0+
Requires: gdbm-bin
Requires: gdbm-lib
Requires: gdbm-doc
Requires: gdbm-locales
BuildRequires : bison
BuildRequires : flex
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : ncurses-dev
BuildRequires : readline-dev

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


%package dev32
Summary: dev32 components for the gdbm package.
Group: Default
Requires: gdbm-lib32
Requires: gdbm-bin
Requires: gdbm-dev

%description dev32
dev32 components for the gdbm package.


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


%package lib32
Summary: lib32 components for the gdbm package.
Group: Default

%description lib32
lib32 components for the gdbm package.


%package locales
Summary: locales components for the gdbm package.
Group: Default

%description locales
locales components for the gdbm package.


%prep
%setup -q -n gdbm-1.13
pushd ..
cp -a gdbm-1.13 build32
popd

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489584715
%configure --disable-static --enable-libgdbm-compat
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static --enable-libgdbm-compat   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1489584715
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
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
/usr/lib64/libgdbm.so
/usr/lib64/libgdbm_compat.so

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libgdbm.so
/usr/lib32/libgdbm_compat.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgdbm.so.4
/usr/lib64/libgdbm.so.4.0.0
/usr/lib64/libgdbm_compat.so.4
/usr/lib64/libgdbm_compat.so.4.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libgdbm.so.4
/usr/lib32/libgdbm.so.4.0.0
/usr/lib32/libgdbm_compat.so.4
/usr/lib32/libgdbm_compat.so.4.0.0

%files locales -f gdbm.lang
%defattr(-,root,root,-)

