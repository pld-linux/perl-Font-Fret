%include	/usr/lib/rpm/macros.perl
%define	pdir	Font
%define	pnam	Fret
Summary:	Font::Fret perl module
Summary(pl):	Modu³ perla Font::Fret
Name:		perl-Font-Fret
Version:	1.202
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f94065491279e977d45fff46b110e799
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Font-AFM
BuildRequires:	perl-Font-TTF
BuildRequires:	perl-Text-PDF
BuildRequires:	perl-IO-stringy
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Font::Fret - Font REporting Tool.

%description -l pl
Modu³ perla Font::Fret.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*.plx
%{perl_vendorlib}/Font/Fret.pm
%{_mandir}/man3/*
