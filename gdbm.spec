#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3602B07F55D0C732 (gray@gnu.org)
#
Name     : gdbm
Version  : 1.20
Release  : 34
URL      : https://mirrors.kernel.org/gnu/gdbm/gdbm-1.20.tar.gz
Source0  : https://mirrors.kernel.org/gnu/gdbm/gdbm-1.20.tar.gz
Source1  : https://mirrors.kernel.org/gnu/gdbm/gdbm-1.20.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: gdbm-bin = %{version}-%{release}
Requires: gdbm-info = %{version}-%{release}
Requires: gdbm-lib = %{version}-%{release}
Requires: gdbm-license = %{version}-%{release}
Requires: gdbm-locales = %{version}-%{release}
Requires: gdbm-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : dejagnu
BuildRequires : expect
BuildRequires : flex
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : ncurses-dev
BuildRequires : readline-dev
BuildRequires : tcl

%description
See the end of file for copying conditions.
* Note
This is an experimental branch of GNU DBM.  Its goal is to evaluate
possibilities of improving the caching scheme.  Please don't use it
in production.

%package bin
Summary: bin components for the gdbm package.
Group: Binaries
Requires: gdbm-license = %{version}-%{release}

%description bin
bin components for the gdbm package.


%package dev
Summary: dev components for the gdbm package.
Group: Development
Requires: gdbm-lib = %{version}-%{release}
Requires: gdbm-bin = %{version}-%{release}
Provides: gdbm-devel = %{version}-%{release}
Requires: gdbm = %{version}-%{release}

%description dev
dev components for the gdbm package.


%package dev32
Summary: dev32 components for the gdbm package.
Group: Default
Requires: gdbm-lib32 = %{version}-%{release}
Requires: gdbm-bin = %{version}-%{release}
Requires: gdbm-dev = %{version}-%{release}

%description dev32
dev32 components for the gdbm package.


%package info
Summary: info components for the gdbm package.
Group: Default

%description info
info components for the gdbm package.


%package lib
Summary: lib components for the gdbm package.
Group: Libraries
Requires: gdbm-license = %{version}-%{release}

%description lib
lib components for the gdbm package.


%package lib32
Summary: lib32 components for the gdbm package.
Group: Default
Requires: gdbm-license = %{version}-%{release}

%description lib32
lib32 components for the gdbm package.


%package license
Summary: license components for the gdbm package.
Group: Default

%description license
license components for the gdbm package.


%package locales
Summary: locales components for the gdbm package.
Group: Default

%description locales
locales components for the gdbm package.


%package man
Summary: man components for the gdbm package.
Group: Default

%description man
man components for the gdbm package.


%prep
%setup -q -n gdbm-1.20
cd %{_builddir}/gdbm-1.20
pushd ..
cp -a gdbm-1.20 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623944034
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static --disable-libgdbm-compat
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static --disable-libgdbm-compat   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
# Readline 8.1 enables bracketed paste mode by default, which in turn causes
# one of the dejagnu tests to fail: the "version" test expects a string
# matching a regex anchored at the beginning, but bracketed paste mode outputs
# a CSI sequence at the beginning instead, causing the regex match to fail.
# Turn off bracketed paste mode to fix it.
bind "set enable-bracketed-paste off"
echo "set enable-bracketed-paste off" > $HOME/.inputrc
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1623944034
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gdbm
cp %{_builddir}/gdbm-1.20/COPYING %{buildroot}/usr/share/package-licenses/gdbm/70e64fe9090c157e441681779e0f31aad34f35cb
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
/usr/include/gdbm.h
/usr/lib64/libgdbm.so
/usr/share/man/man3/gdbm.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libgdbm.so

%files info
%defattr(0644,root,root,0755)
/usr/share/info/gdbm.info

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgdbm.so.6
/usr/lib64/libgdbm.so.6.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libgdbm.so.6
/usr/lib32/libgdbm.so.6.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gdbm/70e64fe9090c157e441681779e0f31aad34f35cb

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gdbm_dump.1
/usr/share/man/man1/gdbm_load.1
/usr/share/man/man1/gdbmtool.1

%files locales -f gdbm.lang
%defattr(-,root,root,-)

