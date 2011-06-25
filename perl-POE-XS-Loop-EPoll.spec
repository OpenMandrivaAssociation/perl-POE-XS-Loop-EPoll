%define upstream_name    POE-XS-Loop-EPoll
%define upstream_version 1.001

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    An XS implementation of POE::Loop, using Linux` epoll(2)
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(POE)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


