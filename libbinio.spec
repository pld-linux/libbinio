#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Binary I/O stream class library
Summary(pl.UTF-8):	Biblioteka klas C++ dla strumieniowych binarnych operacji I/O
Name:		libbinio
Version:	1.5
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/adplug/libbinio/releases
Source0:	https://github.com/adplug/libbinio/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	261046e16f74d1cdbf9aa6c78fa264e4
Patch0:		%{name}-infopage.patch
Patch1:		gcc4.patch
URL:		http://adplug.github.io/libbinio/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libstdc++-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The binary I/O stream class library presents a platform-independent
way to access binary data streams in C++. The library is hardware
independent in the form that it transparently converts between the
different forms of machine-internal binary data representation. It
further employs no special I/O protocol and can be used on arbitrary
binary data sources.

%description -l pl.UTF-8
Biblioteka klas strumieniowych binarnych operacji wejścia/wyjścia
prezentuje niezależny od platformy sposób dostępu do binarnych
strumieni danych w C++. Biblioteka jest niezależna od sprzętu dzięki
temu, że w przezroczysty sposób wykonuje konwersję pomiędzy różnymi
postaciami reprezentacji danych binarnych w wewnętrznym formacie
maszyny. Co więcej, nie wykorzystuje żadnego specjalnego protokołu
wejścia/wyjścia i może być używana na dowolnych źródłach danych
binarnych.

%package devel
Summary:	Header files for libbinio library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libbinio
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for libbinio library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libbinio.

%package static
Summary:	Static libbinio library
Summary(pl.UTF-8):	Statyczna biblioteka libbinio
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libbinio library.

%description static -l pl.UTF-8
Statyczna biblioteka libbinio.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libbinio.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libbinio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbinio.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbinio.so
%{_includedir}/libbinio
%{_pkgconfigdir}/libbinio.pc
%{_infodir}/libbinio.info*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libbinio.a
%endif
