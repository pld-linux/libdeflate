Summary:	Library for fast, whole-buffer DEFLATE-based compression and decompression
Summary(pl.UTF-8):	Biblioteka do szybkiej kompresji i dekompresji algorytmem DEFLATE dla całego bufora
Name:		libdeflate
Version:	0.6
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/ebiggers/libdeflate/releases
Source0:	https://github.com/ebiggers/libdeflate/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fd0e3b8bc7e0486e218b67d982f2fa99
Patch0:		%{name}-soname.patch
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
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	V=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

install gzip $RPM_BUILD_ROOT%{_bindir}/libdeflate-gzip
install gunzip $RPM_BUILD_ROOT%{_bindir}/libdeflate-gunzip
install libdeflate.so $RPM_BUILD_ROOT%{_libdir}/libdeflate.so.0
ln -sf libdeflate.so.0 $RPM_BUILD_ROOT%{_libdir}/libdeflate.so
cp -p libdeflate.a $RPM_BUILD_ROOT%{_libdir}
cp -p libdeflate.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README.md
%attr(755,root,root) %{_bindir}/libdeflate-gzip
%attr(755,root,root) %{_bindir}/libdeflate-gunzip
%attr(755,root,root) %{_libdir}/libdeflate.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdeflate.so
%{_includedir}/libdeflate.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libdeflate.a
