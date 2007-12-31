Summary:	Trace the route of IP packets going to "host"
Summary(pl.UTF-8):	Program do śledzenia ścieżki pakietów IP
Name:		traceroute-nanog
Version:	6.4.2
Release:	1
License:	distributable
Group:		Applications/Networking
# original URL - but there is only vulnerable 6.3.0 here
#Source0:	ftp://ftp.login.com/pub/software/traceroute/dist/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.debian.org/debian/pool/main/t/traceroute-nanog/%{name}_%{version}.orig.tar.gz
# Source0-md5:	cd737165e6ab62fef83de1227ae6804b
Patch0:		%{name}-debian.patch
Obsoletes:	traceroute
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extended version of normal traceroute utility. It can report AS# at
each hop (from GRR), report owner at each hop (from DNS) etc.

%description -l pl.UTF-8
Rozszerzona wersja programu traceroute. Potrafi raportować AS# (z
GRR), właściciela (z DNS) itp. na każdym kroku.

%prep
%setup -q -n %{name}-%{version}.orig
%patch0 -p1

# remember to update numbers on earch upgrade!
tail -n +232 traceroute.c | head -n 311 > ChangeLog

%build
%{__cc} %{rpmldflags} %{rpmcflags} -Wall -DSTRING -o tracerouten traceroute.c -lm -lresolv

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man8}

install tracerouten $RPM_BUILD_ROOT%{_bindir}/traceroute
ln -s %{_bindir}/traceroute $RPM_BUILD_ROOT%{_sbindir}
install debian/traceroute.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc 0_readme.txt faq.txt ChangeLog
%attr(4754,root,adm) %{_bindir}/*
%{_sbindir}/traceroute
%{_mandir}/man8/traceroute.8*
