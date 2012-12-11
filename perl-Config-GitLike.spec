%define upstream_name    Config-GitLike
%define upstream_version 1.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Git-like config file parsing with cascaded inheritance
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Any::Moose)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This module handles interaction with configuration files of the style used
by the version control system Git. It can both parse and modify these
files, as well as create entirely new ones.

You only need to know a few things about the configuration format in order
to use this module. First, a configuration file is made up of key/value
pairs. Every key must be contained in a section. Sections can have
subsections, but they don't have to. For the purposes of setting and
getting configuration variables, we join the section name, subsection name,
and variable name together with dots to get a key name that looks like
"section.subsection.variable". These are the strings that you'll be passing
in to 'key' arguments.

Configuration files inherit from each other. By default, 'Config::GitLike'
loads data from a system-wide configuration file, a per-user configuration
file, and a per-directory configuration file, but by subclassing and
overriding methods you can obtain any combination of configuration files.
By default, configuration files that don't exist are just skipped.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Config/

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.50.0-2mdv2011.0
+ Revision: 680840
- mass rebuild

* Fri Jan 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.50.0-1mdv2011.0
+ Revision: 629480
- update to new version 1.05

* Fri Apr 30 2010 Michael Scherer <misc@mandriva.org> 1.40.0-1mdv2011.0
+ Revision: 541093
- import perl-Config-GitLike


* Fri Apr 30 2010 cpan2dist 1.04-1mdv
- initial mdv release, generated with cpan2dist
