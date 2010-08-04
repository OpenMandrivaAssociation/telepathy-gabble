Name:           telepathy-gabble
Version:        0.9.13
Release:        %mkrel 1
Summary:        A Jabber/XMPP connection manager

Group:          Networking/Instant messaging
License:        LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:  libxslt-proc
BuildRequires:  python-devel
BuildRequires:  libtelepathy-glib-devel >= 0.7.31
BuildRequires:	libsoup-devel
BuildRequires:	libnice-devel >= 0.0.11
Requires:	telepathy-filesystem
Obsoletes:      tapioca-xmpp
# no longer exist since 0.5.11
Obsoletes:      telepathy-gabble-devel

%description
A Jabber/XMPP connection manager, that handles single and multi-user
chats and voice calls.

%files
%defattr(-,root,root,-)
%doc NEWS README AUTHORS
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/*.manager
%{_libdir}/telepathy-gabble
%{_mandir}/man*/*.lzma
%{_libdir}/telepathy/gabble-0/gateways.la
%{_libdir}/telepathy/gabble-0/gateways.so


#--------------------------------------------------------------------

%prep
%setup -q

%build
CFLAGS="%{optflags} -fPIC" %configure2_5x --enable-olpc --disable-static
%make

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot
