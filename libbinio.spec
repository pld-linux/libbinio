#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Binary I/O stream class library
Summary(pl):	Biblioteka klas C++ dla strumieniowych binarnych operacji I/O
Name:		libbinio
Version:	1.4
Release:	1
License:	GPL/LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libbinio/%{name}-%{version}.tar.bz2
# Source0-md5:	517ded8c7ce9b3de0f84b1db74a2ebda
Patch0:		%{name}-infopage.patch
URL:		http://libbinio.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The binary I/O stream class library presents a platform-independent
way to access binary data streams in C++. The library is hardware
independent in the form that it transparently converts between the
different forms of machine-internal binary data representation. It
further employs no special I/O protocol and can be used on arbitrary
binary data sources.

%description -l pl
Biblioteka klas strumieniowych binarnych operacji wej¶cia/wyj¶cia
prezentuje niezale¿ny od platformy sposób dostêpu do binarnych
strumieni danych w C++. Biblioteka jest niezale¿na od sprzêtu dziêki
temu, ¿e w przezroczysty sposób wykonuje konwersjê pomiêdzy ró¿nymi
postaciami reprezentacji danych binarnych w wewnêtrznym formacie
maszyny. Co wiêcej, nie wykorzystuje ¿adnego specjalnego protoko³u
wej¶cia/wyj¶cia i mo¿e byæ u¿ywana na dowolnych ¼ród³ach danych
binarnych.

%package devel
Summary:	Header files for libbinio library
Summary(pl):	Pliki nag³ówkowe biblioteki libbinio
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for libbinio library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libbinio.

%package static
Summary:	Static libbinio library
Summary(pl):	Statyczna biblioteka libbinio
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libbinio library.

%description static -l pl
Statyczna biblioteka libbinio.

%prep
%setup -q
%patch0 -p1

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc
%{_infodir}/*.info*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
