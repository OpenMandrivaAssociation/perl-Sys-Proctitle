%define real_name Sys-Proctitle

Summary:	Sys::Proctitle - modify proctitle on Linux
Name:		perl-%{real_name}
Version:	0.02
Release:	%mkrel 6
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/O/OP/OPI/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-Class-Member
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
"Sys::Proctitle" provides an interface for setting the process title
shown by "ps", "top" or similar tools on Linux. Why do we need this? One
could simply change $0 to achieve the same result. Well, first setting
$0 did not work with 5.8.0. Further, setting $0 won't work with
mod_perl.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

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

