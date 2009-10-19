Name:           telepathy-gabble
Version:        0.8.7
Release:        %mkrel 1
Summary:        A Jabber/XMPP connection manager

Group:          Networking/Instant messaging
License:        LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
# Upstream fix from darcs repository, fixes telepathy-gabble with
# glib 2.17
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	loudmouth-devel
BuildRequires:  libxslt-proc
BuildRequires:  python-devel
BuildRequires:  libtelepathy-glib-devel >= 0.7.31
BuildRequires:	libsoup-devel
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

#--------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x --disable-loudmouth-versioning --enable-olpc
%make

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot
