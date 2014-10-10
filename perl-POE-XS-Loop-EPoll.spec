%define upstream_name    POE-XS-Loop-EPoll
%define upstream_version 1.003

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	2

Summary:    An XS implementation of POE::Loop, using Linux` epoll(2)
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/POE/POE-XS-Loop-EPoll-%{upstream_version}.tar.gz

BuildRequires: perl(POE)
BuildRequires: perl(POE::Test::Loops)
BuildRequires: perl-devel

%description
This class is an implementation of the abstract POE::Loop interface written
in C using the Linux epoll(2) family of system calls.

Signals are left to POE::Loop::PerlSignals.

The epoll_ctl() call returns an error when you attempt to poll regular
files, POE::XS::Loop::EPoll emulate's poll(2)'s behaviour with regular
files under Linux - ie. they're always readable/writeable.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%clean

%files
%doc META.yml README Changes
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat Jun 25 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.0-1
+ Revision: 687127
- import perl-POE-XS-Loop-EPoll


