Name:       xl2tpd
Summary:    Layer 2 Tunnelling Protocol Daemon (RFC 2661)
Version:    1.3.8
Release:    1
Group:      Applications/Internet
License:    GPLv2+
URL:        https://github.com/xelerance/xl2tpd
Source0:    https://github.com/xelerance/%{name}/archive/%{name}-%{version}.tar.gz
Patch0:     change-default-prefix.patch
BuildRequires:  coreutils
BuildRequires:  sed
BuildRequires:  ppp-devel
BuildRequires:  libpcap-devel

%description
xl2tp Layer 2 Tunnelling Protocol Daemon.


%prep
%setup -q -n %{name}-%{version}/%{name}
%patch0 -p1

%build
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/sbin/xl2tpd
/usr/sbin/xl2tpd-control
%{_bindir}/pfc
%exclude %{_mandir}/man1/pfc.1.gz
%exclude %{_mandir}/man5/xl2tpd.conf.5.gz
%exclude %{_mandir}/man5/l2tp-secrets.5.gz
%exclude %{_mandir}/man8/xl2tpd.8.gz
