#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : jemalloc
Version  : 5.3.0
Release  : 42
URL      : https://github.com/jemalloc/jemalloc/releases/download/5.3.0/jemalloc-5.3.0.tar.bz2
Source0  : https://github.com/jemalloc/jemalloc/releases/download/5.3.0/jemalloc-5.3.0.tar.bz2
Summary  : A general purpose malloc(3) implementation that emphasizes fragmentation avoidance and scalable concurrency support.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: jemalloc-bin = %{version}-%{release}
Requires: jemalloc-lib = %{version}-%{release}
Requires: jemalloc-license = %{version}-%{release}

%description
jemalloc is a general purpose malloc(3) implementation that emphasizes
fragmentation avoidance and scalable concurrency support.  jemalloc first came
into use as the FreeBSD libc allocator in 2005, and since then it has found its
way into numerous applications that rely on its predictable behavior.  In 2010
jemalloc development efforts broadened to include developer support features
such as heap profiling and extensive monitoring/tuning hooks.  Modern jemalloc
releases continue to be integrated back into FreeBSD, and therefore versatility
remains critical.  Ongoing development efforts trend toward making jemalloc
among the best allocators for a broad range of demanding applications, and
eliminating/mitigating weaknesses that have practical repercussions for real
world applications.

%package bin
Summary: bin components for the jemalloc package.
Group: Binaries
Requires: jemalloc-license = %{version}-%{release}

%description bin
bin components for the jemalloc package.


%package dev
Summary: dev components for the jemalloc package.
Group: Development
Requires: jemalloc-lib = %{version}-%{release}
Requires: jemalloc-bin = %{version}-%{release}
Provides: jemalloc-devel = %{version}-%{release}
Requires: jemalloc = %{version}-%{release}

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
Requires: jemalloc-license = %{version}-%{release}

%description lib
lib components for the jemalloc package.


%package license
Summary: license components for the jemalloc package.
Group: Default

%description license
license components for the jemalloc package.


%package staticdev
Summary: staticdev components for the jemalloc package.
Group: Default
Requires: jemalloc-dev = %{version}-%{release}

%description staticdev
staticdev components for the jemalloc package.


%prep
%setup -q -n jemalloc-5.3.0
cd %{_builddir}/jemalloc-5.3.0
pushd ..
cp -a jemalloc-5.3.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656127125
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
%configure  --disable-initial-exec-tls
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure  --disable-initial-exec-tls
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1656127125
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jemalloc
cp %{_builddir}/jemalloc-5.3.0/COPYING %{buildroot}/usr/share/package-licenses/jemalloc/c797cef3f1b13a960a5119a084fb88529a924fd7
pushd ../buildavx2/
%make_install_v3
popd
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/bin/pprof
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/libjemalloc.so
/usr/lib64/pkgconfig/jemalloc.pc
/usr/share/man/man3/jemalloc.3

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/jemalloc/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libjemalloc.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libjemalloc.so.2
/usr/lib64/libjemalloc.so.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jemalloc/c797cef3f1b13a960a5119a084fb88529a924fd7

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libjemalloc.a
/usr/lib64/libjemalloc_pic.a
