Summary:	trace the route ip packets follow going to "host"
Name:		traceroute-nanog
Version:	2.9.3
Release:	1
License:	distributable
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Source:		ftp://ftp.aces.com/pub/software/traceroute/beta/%{name}-%{version}.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Extended version of normal traceroute utility. It can Report AS# at each
hop (from GRR), Report owner at each hop (from DNS) etc.

%description -l pl
Rozszerzona wersja programu traceroute.

%prep
%setup -q
%build
gcc $RPM_OPT_FLAGS -lresolv -lm -o tracerouten traceroute.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install -s tracerouten $RPM_BUILD_ROOT%{_sbindir}

gzip -9nf 0_readme.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(4755,root,bin) %{_sbindir}/tracerouten
