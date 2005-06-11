Summary:	Binary I/O stream class library
Summary(pl):	Biblioteka klas strumieni binarnych
Name:		libbinio
Version:	1.3
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libbinio/%{name}-%{version}.tar.bz2
# Source0-md5:	dea7bd4c2d9d9f5429082448af2aab22
URL:		http://libbinio.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The binary I/O stream class library presents a platform-independent way to
access binary data streams in C++.

%description -l pl
Biblioteka klas dla strumieni binarnych jest niezale¿na od platformy drog±
dostêpu do danych w strumieniach binarnych przy u¿yciu C++.

%package devel
Summary:	Development libraries and header files for termcap library
Summary(pl):	Biblioteki deweloperskie i pliki nag³ówkowe dla libbinio
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the development libaries and header
files for libbinio.

%description -l pl devel
Ten pakiet zawiera pliki nag³ówkowe i biblioteki  deweloperskie dla
libbinio.

%package static
Summary:	Static libbinio library
Summary(pl):	Statyczne biblioteki libbinio
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libbinio library.

%description -l pl static
Statyczne biblioteki libbinio.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig

%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/%{name}.so
%{_libdir}/%{name}.so.1.0.0
%{_libdir}/%{name}.la
%{_infodir}/%{name}*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
