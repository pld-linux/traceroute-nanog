Summary:	Trace the route of IP packets going to "host"
Summary(pl):	Program do ¶ledzenia ¶cie¿ki pakietów IP
Name:		traceroute-nanog
Version:	6.3.9
Release:	1
License:	distributable
Group:		Applications/Networking
# original URL - but there is only vulnerable 6.3.0 here
#Source0:	ftp://ftp.login.com/pub/software/traceroute/dist/%{name}-%{version}.tar.gz
# ...or latest version, but only source code, without other files
#Source0:	ftp://ftp.login.com/pub/software/traceroute/beta/traceroute.c
Source0:	ftp://ftp.debian.org/debian/pool/main/t/traceroute-nanog/%{name}_%{version}.orig.tar.gz
# Source0-md5:	3e663d4053da5230e0f0df69e59717a7
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

# remember to update numbers on earch upgrade!
tail +229 traceroute.c | head -n 309 > ChangeLog

%build
%{__cc} %{rpmldflags} %{rpmcflags} -o tracerouten traceroute.c -lm -lresolv

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install tracerouten $RPM_BUILD_ROOT%{_sbindir}/traceroute
install traceroute.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc 0_readme.txt faq.txt ChangeLog
%attr(4754,root,adm) %{_sbindir}/traceroute
%{_mandir}/man8/traceroute.8*
