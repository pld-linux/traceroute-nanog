Summary:	Trace the route of IP packets going to "host"
Summary(pl):	Program do ¶ledzenia ¶cie¿ki pakietów IP
Name:		traceroute-nanog
Version:	2.9.3
Release:	3
License:	distributable
Group:		Applications/Networking
Source0:	ftp://ftp.aces.com/pub/software/traceroute/beta/%{name}-%{version}.tar.gz
Obsoletes:	traceroute
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extended version of normal traceroute utility. It can Report AS# at
each hop (from GRR), Report owner at each hop (from DNS) etc.

%description -l pl
Rozszerzona wersja programu traceroute.

%prep
%setup -q
%build
%{__cc} %{rpmcflags} -lresolv -lm -o tracerouten traceroute.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install tracerouten $RPM_BUILD_ROOT%{_sbindir}/traceroute

gzip -9nf 0_readme.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(4754,root,adm) %{_sbindir}/traceroute
