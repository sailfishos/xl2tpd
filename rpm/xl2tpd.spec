Name:       xl2tpd
Summary:    Layer 2 Tunnelling Protocol Daemon (RFC 2661)
Version:    1.3.16
Release:    1
License:    GPLv2+
URL:        https://github.com/xelerance/xl2tpd
Source0:    %{name}-%{version}.tar.gz
Patch0:     change-default-prefix.patch
BuildRequires:  coreutils
BuildRequires:  sed
BuildRequires:  ppp-devel
BuildRequires:  libpcap-devel
Requires:   ppp
Requires:   ppp-libs

%description
xl2tp Layer 2 Tunnelling Protocol Daemon.


%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%make_build

%install
%make_install

%files
%defattr(-,root,root,-)
%license LICENSE
%{_sbindir}/xl2tpd
%{_sbindir}/xl2tpd-control
%{_bindir}/pfc
%exclude %{_mandir}/man1/pfc.1.gz
%exclude %{_mandir}/man5/xl2tpd.conf.5.gz
%exclude %{_mandir}/man5/l2tp-secrets.5.gz
%exclude %{_mandir}/man8/xl2tpd.8.gz
%exclude %{_mandir}/man8/xl2tpd-control.8.gz
