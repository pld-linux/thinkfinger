# NOTE: dead package, use fprint instead
# see http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=546005
Summary:	Driver for SGS Thomson fingerprint reader
Summary(pl.UTF-8):	Sterownik do czytników linii papilarnych SGS Thomson
Name:		thinkfinger
Version:	0.3
Release:	4
License:	GPL
Group:		Base
Source0:	http://dl.sourceforge.net/thinkfinger/%{name}-%{version}.tar.gz
# Source0-md5:	588565233bcbea5ff0a7f5314361c380
URL:		http://thinkfinger.sourceforge.net
Patch0:		%{name}-timeout.patch
Patch1:		%{name}-syncevent.patch
BuildRequires:	libusb-devel
BuildRequires:	pam-devel >= 0.99.1.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ThinkFinger is a driver for the SGS Thomson Microelectronics
fingerprint reader found in most IBM/Lenovo ThinkPads.

%description -l pl.UTF-8
ThinkFinger to sterownik do czytników linii papilarnych SGS Thomson
Microelectronics, jakie można znaleźć w większości ThinkPadów
IBM/Lenovo.

%package devel
Summary:	Header files for thinkfinger
Summary(pl.UTF-8):	Pliki nagłówkowe thinkfinger
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for thinkfinger.

%description devel -l pl.UTF-8
Pliki nagłówkowe thinkfinger.

%package static
Summary:	Static thinkfinger libraries
Summary(pl.UTF-8):	Statyczne biblioteki thinkfinger
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static thinkfinger libraries.

%description static -l pl.UTF-8
Statyczne biblioteki thinkfinger.

%package -n pam-pam_thinkfinger
Summary:	A PAM module - thinkfinger
Summary(pl.UTF-8):	Moduł PAM thinkfinger
Group:		Base
Requires:	%{name} = %{version}-%{release}
Requires:	pam-libs >= 0.99.1.0

%description -n pam-pam_thinkfinger
A PAM module - thinkfinger.

%description -n pam-pam_thinkfinger -l pl.UTF-8
Moduł PAM thinkfinger.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
%configure \
	--enable-pam \
	--with-securedir=/%{_lib}/security

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/pam_thinkfinger

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_sbindir}/tf-tool
%attr(755,root,root) %{_libdir}/libthinkfinger.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libthinkfinger.so.0
%dir %{_sysconfdir}/pam_thinkfinger
%{_mandir}/man1/tf-tool.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libthinkfinger.so
%{_libdir}/libthinkfinger.la
%{_includedir}/libthinkfinger.h
%{_pkgconfigdir}/libthinkfinger.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libthinkfinger.a

%files -n pam-pam_thinkfinger
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/security/pam_thinkfinger.so
%{_mandir}/man8/pam_thinkfinger.8*
