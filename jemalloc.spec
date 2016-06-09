#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jemalloc
Version  : 4.2.1
Release  : 20
URL      : http://www.canonware.com/download/jemalloc/jemalloc-4.2.1.tar.bz2
Source0  : http://www.canonware.com/download/jemalloc/jemalloc-4.2.1.tar.bz2
Summary  : A general purpose malloc(3) implementation that emphasizes fragmentation avoidance and scalable concurrency support.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: jemalloc-bin
Requires: jemalloc-lib
Requires: jemalloc-doc

%description
jemalloc is a general purpose malloc(3) implementation that emphasizes
fragmentation avoidance and scalable concurrency support.  jemalloc first came
into use as the FreeBSD libc allocator in 2005, and since then it has found its
way into numerous applications that rely on its predictable behavior.  In 2010
jemalloc development efforts broadened to include developer support features
such as heap profiling, Valgrind integration, and extensive monitoring/tuning
hooks.  Modern jemalloc releases continue to be integrated back into FreeBSD,
and therefore versatility remains critical.  Ongoing development efforts trend
toward making jemalloc among the best allocators for a broad range of demanding
applications, and eliminating/mitigating weaknesses that have practical
repercussions for real world applications.

%package bin
Summary: bin components for the jemalloc package.
Group: Binaries

%description bin
bin components for the jemalloc package.


%package dev
Summary: dev components for the jemalloc package.
Group: Development
Requires: jemalloc-lib
Requires: jemalloc-bin
Provides: jemalloc-devel

%description dev
dev components for the jemalloc package.


%package doc
Summary: doc components for the jemalloc package.
Group: Documentation

%description doc
doc components for the jemalloc package.


%package lib
Summary: lib components for the jemalloc package.
Group: Libraries

%description lib
lib components for the jemalloc package.


%prep
%setup -q -n jemalloc-4.2.1

%build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fno-semantic-interposition -flto -falign-functions=32 "
export FCFLAGS="$CFLAGS -O3 -fno-semantic-interposition -flto -falign-functions=32 "
export FFLAGS="$CFLAGS -O3 -fno-semantic-interposition -flto -falign-functions=32 "
export CXXFLAGS="$CXXFLAGS -O3 -fno-semantic-interposition -flto -falign-functions=32 "
%configure --disable-static
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

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jemalloc-config
/usr/bin/jemalloc.sh
/usr/bin/jeprof

%files dev
%defattr(-,root,root,-)
/usr/include/jemalloc/jemalloc.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/jemalloc/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
