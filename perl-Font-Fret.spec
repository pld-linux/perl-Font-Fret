%include	/usr/lib/rpm/macros.perl
%define	pdir	Font
%define	pnam	Fret
Summary:	Font::Fret perl module
Summary(pl):	Modu³ perla Font::Fret
Name:		perl-Font-Fret
Version:	1.202
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
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
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*.plx
%{perl_sitelib}/Font/Fret.pm
%{_mandir}/man3/*
