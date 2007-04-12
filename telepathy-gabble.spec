Name:           telepathy-gabble
Version:        0.5.4
Release:        %mkrel 1
Summary:        A Jabber/XMPP connection manager

Group:          Networking/Instant messaging
License:        LGPL
URL:            http://telepathy.freedesktop.org/wiki/
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	loudmouth-devel
BuildRequires:  libxslt-proc
BuildRequires:  python-devel

Requires:	telepathy-filesystem


%description
A Jabber/XMPP connection manager, that handles single and multi-user
chats and voice calls.

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS
%{_bindir}/%{name}
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/*.manager

#--------------------------------------------------------------------
%package        devel
Group:          System/Libraries
Summary:        Libraries for %{name}

Requires:       %name = %version
Provides:       lib%name-devel

%description    devel
The libraries from %{name} package

%files devel
%defattr(-,root,root,-)
%{_includedir}/telepathy-1.0/telepathy-glib/_gen/*.h
%{_includedir}/telepathy-1.0/telepathy-glib/*.h
%{_libdir}/pkgconfig/telepathy-glib.pc
%{_libdir}/*.a
%{_libdir}/*.la

#--------------------------------------------------------------------

%prep
%setup -q


%build
%configure --disable-loudmouth-versioning
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


