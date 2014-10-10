%define upstream_name    Sys-Proctitle
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.40.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 556153
- rebuild for perl 5.12

* Thu Mar 11 2010 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.1
+ Revision: 518087
- update to 0.04

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 404433
- rebuild using %%perl_convert_version

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2009.1
+ Revision: 292352
- update to new version 0.03

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.02-6mdv2009.0
+ Revision: 258425
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.02-5mdv2009.0
+ Revision: 246491
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.02-3mdv2008.1
+ Revision: 151408
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-2mdv2008.0
+ Revision: 86924
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.02-1mdv2007.0
- rebuild

* Sat Jul 16 2005 Oden Eriksson <oeriksson@mandriva.com> 0.02-1mdk
- initial Mandriva package

