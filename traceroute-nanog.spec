Summary:	trace the route ip packets follow going to "host".
Name:		traceroute-nanog
Version:	2.9.3
License:	PSC?
Release:	1
Group:		Applications/Internet
######		/home/lukasz/rpm/groups: no such file
Source:		ftp://ftp.aces.com/pub/software/traceroute/beta/%{name}-%{version}.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix /usr
%description
Extended version of  normal traceroute utility. It can Report AS# at each
hop (from GRR), Report owner at each hop (from DNS) etc.

%description -l pl
Rozszerzona wersja programu traceroute.

%prep
%setup -q
%build
gcc -lresolv -lm -o tracerouten traceroute.c

%install
install -d ${RPM_BUILD_ROOT}%{_sbindir}
install -s tracerouten $RPM_BUILD_ROOT%{_sbindir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc 0_readme.txt
%attr(4755,root,bin) %{_sbindir}/tracerouten
