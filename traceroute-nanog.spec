Summary:	Trace the route of IP packets going to "host"
Summary(pl):	Program do ¶ledzenia ¶cie¿ki pakietów IP
Name:		traceroute-nanog
Version:	6.1.1
Release:	1
License:	distributable
Group:		Applications/Networking
# original URL - but there is only vulnerable 6.1.3 here
#Source0:	ftp://ftp.login.com/pub/software/traceroute/dist/%{name}-%{version}.tar.gz
# ...or latest version (6.2.0 at the moment), but only code, without other files :/
#Source0:	ftp://ftp.login.com/pub/software/traceroute/beta/traceroute.c
Source0:	ftp://ftp.debian.org/debian/pool/main/t/traceroute-nanog/traceroute-nanog_6.1.1.orig.tar.gz
# Source0-md5:	493e77d8cf0e86744668e3efd4622378
Patch0:		%{name}-debian.patch
Obsoletes:	traceroute
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extended version of normal traceroute utility. It can report AS# at
each hop (from GRR), report owner at each hop (from DNS) etc.

%description -l pl
Rozszerzona wersja programu traceroute. Potrafi raportowaæ AS# (z
GRR), w³a¶ciciela (z DNS) itp. na ka¿dym kroku.

%prep
%setup -q
%patch -p1

%build
%{__cc} %{rpmcflags} -o tracerouten traceroute.c -lm -lresolv

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install tracerouten $RPM_BUILD_ROOT%{_sbindir}/traceroute
install traceroute.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc 0_readme.txt faq.txt
%attr(4754,root,adm) %{_sbindir}/traceroute
%{_mandir}/man8/traceroute.8*
