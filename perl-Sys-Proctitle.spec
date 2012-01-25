%define upstream_name    Sys-Proctitle
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:	Sys::Proctitle - modify proctitle on Linux
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/O/OP/OPI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Class::Member)
BuildRequires:	perl-devel

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
"Sys::Proctitle" provides an interface for setting the process title
shown by "ps", "top" or similar tools on Linux. Why do we need this? One
could simply change $0 to achieve the same result. Well, first setting
$0 did not work with 5.8.0. Further, setting $0 won't work with
mod_perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%dir %{perl_vendorlib}/*/auto/Sys/Proctitle
%{perl_vendorlib}/*/Sys/Proctitle.pm
%{perl_vendorlib}/*/auto/Sys/Proctitle/Proctitle.so
%{perl_vendorlib}/*/auto/Sys/Proctitle/setproctitle.so
%{_mandir}/*/*
