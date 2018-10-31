%define __noautoprov devel\\(.*\\)
%define __noautoreq ^%{_libdir}/telepathy/.*\\.so$\\|^devel\\(.*\\)

Name:           telepathy-gabble
Version:        0.18.4
Release:        4
Summary:        A Jabber/XMPP connection manager
Group:          Networking/Instant messaging
License:        LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
Source100:	telepathy-gabble.rpmlintrc
BuildRequires:	pkgconfig(dbus-1) >= 1.1.0
BuildRequires:	pkgconfig(dbus-glib-1) >= 0.82
BuildRequires:	pkgconfig(gio-2.0) >= 2.26
BuildRequires:	pkgconfig(glib-2.0) >= 2.24
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires: 	pkgconfig(openssl)
BuildRequires:	pkgconfig(gobject-2.0) >= 2.24
BuildRequires:	pkgconfig(gthread-2.0) >= 2.24
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(nice) >= 0.0.11
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(telepathy-glib) >= 0.17.2
BuildRequires:	rootcerts
BuildRequires:	libxslt-proc
BuildRequires:	python-devel
Requires:	telepathy-filesystem

%description
A Jabber/XMPP connection manager, that handles single and multi-user
chats and voice calls.

%files
%doc NEWS README AUTHORS
%{_bindir}/telepathy-gabble-xmpp-console
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/*.manager
%{_libexecdir}/telepathy-gabble
%{_libdir}/telepathy/gabble-0
%{_mandir}/man*/*.*

#--------------------------------------------------------------------

%prep
%setup -q

%build
export PYTHON=%{__python2}
%configure --with-ca-certificates=%{_sysconfdir}/pki/tls/certs/ca-bundle.crt
%make

%install
%makeinstall_std

# don't ship .la
find %{buildroot} -name '*.la' | xargs rm -f
