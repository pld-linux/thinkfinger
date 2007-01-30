Summary:	Driver for SGS Thomson fingerprint reader
Name:		thinkfinger
Version:	0.2.1
Release:	0.1
License:	GPL
Group:		Base
Source0:	http://dl.sourceforge.net/thinkfinger/%{name}-%{version}.tar.gz
# Source0-md5:	d6d9771faf8c6b768449e0b415be2dde
URL:		http://thinkfinger.sourceforge.net
BuildRequires:	libusb-devel
BuildRequires:	pam-devel >= 0.99.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ThinkFinger is a driver for the SGS Thomson Microelectronics
fingerprint reader found in most IBM/Lenovo ThinkPads.

%package devel
Summary:	Header files for thinkfinger
Summary(pl):	Pliki nag³ówkowe thinkfinger
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for thinkfinger.

%description devel -l pl
Pliki nag³ówkowe thinkfinger.

%package static
Summary:	Static thinkfinger libraries
Summary(pl):	Statyczne biblioteki thinkfinger
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static thinkfinger libraries.

%description static -l pl
Statyczne biblioteki thinkfinger.

%package -n pam-pam_thinkfinger
Summary:	A PAM module - thinkfinger
Group:		Base
Requires:	%{name} = %{version}-%{release}

%description -n pam-pam_thinkfinger
A PAM module - thinkfinger.

%prep
%setup -q

%build
%configure \
	--enable-pam \
	--with-securedir=/%{_lib}/security

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/pam_thinkfinger

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/*.so.*
%dir %{_sysconfdir}/pam_thinkfinger

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*.pc
%{_libdir}/*.la
%{_includedir}/%{name}
%attr(755,root,root) %{_libdir}/*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/*.la

%files -n pam-pam_thinkfinger
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/security/*.so
