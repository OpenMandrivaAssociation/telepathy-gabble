Name:           telepathy-gabble
Version:        0.5.13
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
BuildRequires:  telepathy-glib
Requires:	telepathy-filesystem
Obsoletes:      tapioca-xmpp
# no longer exist since 0.5.11
Obsoletes:      telepathy-gabble-devel

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

%prep
%setup -q


%build
%configure --disable-loudmouth-versioning
%make 


%install
rm -rf %buildroot
make install DESTDIR=%buildroot


%clean
rm -rf %buildroot
