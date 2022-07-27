Summary:	Library for fast, whole-buffer DEFLATE-based compression and decompression
Summary(pl.UTF-8):	Biblioteka do szybkiej kompresji i dekompresji algorytmem DEFLATE dla całego bufora
Name:		libdeflate
Version:	1.12
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/ebiggers/libdeflate/releases
Source0:	https://github.com/ebiggers/libdeflate/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	038cb9addf76c450115b7de0a6427a84
URL:		https://github.com/ebiggers/libdeflate
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdeflate is a library for fast, whole-buffer DEFLATE-based
compression and decompression.

libdeflate is heavily optimized. It is significantly faster than the
zlib library, both for compression and decompression, and especially
on x86 processors. In addition, libdeflate provides optional high
compression modes that provide a better compression ratio than the
zlib's "level 9".

%description -l pl.UTF-8
libdeflate do biblioteka do szybkiej kompresji i dekompresji na całym
buforze w oparciu o algorytm DEFLATE.

libdeflate jest wydatnie zoptymalizowana; jest znacząco szybsza od
biblioteki zlib, zarówno przy kompresji, jak i dekompresji, w
szczególności na procesorach x86. Ponadto libdeflate zapewnia
opcjonalnie wyższe stopnie kompresji, z lepszym współczynnikiem niż
"poziom 9" zliba.

%package devel
Summary:	Header file for libdeflate library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki libdeflate
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for libdeflate library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki libdeflate.

%package static
Summary:	Static libdeflate library
Summary(pl.UTF-8):	Statyczna biblioteka libdeflate
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libdeflate library.

%description static -l pl.UTF-8
Statyczna biblioteka libdeflate.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	CPPFLAGS="%{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}" \
	V=1

%install
rm -rf $RPM_BUILD_ROOT

# pass also build flags because of .build-config check in Makefile
%{__make} install \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	CPPFLAGS="%{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}" \
	V=1 \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	INCDIR=%{_includedir} \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING NEWS.md README.md
%attr(755,root,root) %{_bindir}/libdeflate-gzip
%attr(755,root,root) %{_bindir}/libdeflate-gunzip
%attr(755,root,root) %{_libdir}/libdeflate.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdeflate.so
%{_includedir}/libdeflate.h
%{_pkgconfigdir}/libdeflate.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libdeflate.a
