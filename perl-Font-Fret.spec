%include	/usr/lib/rpm/macros.perl
%define		pdir	Font
%define		pnam	Fret
Summary:	Font::Fret - Font REporting Tool
Summary(pl.UTF-8):	Font::Fret - narzędzie raportujące o fontach
Name:		perl-Font-Fret
Version:	1.202
Release:	6
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f94065491279e977d45fff46b110e799
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Font-AFM
BuildRequires:	perl-Font-TTF
BuildRequires:	perl-Text-PDF
BuildRequires:	perl-IO-stringy
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Font::Fret is a font reporting tool system which allows for different
reports to be written.  A report is a package on which calls are made
to give specific information for a specific report.  The rest of Fret
does the housekeeping of generating the report in PDF format.

%description -l pl.UTF-8
Font::Fret jest systemem narzędzi raportujących o fontach, który
umożliwia wypisywanie różnych raportów. Raport jest pakietem, na
którym są wykonywane wywołania w celu uzyskania konkretnej informacji
do konkretnego raportu. Reszta Fret-a zajmuje się generacją nadaniem
generowanemu raportowi formatu PDF.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*.plx
%{perl_vendorlib}/Font/Fret.pm
%{_mandir}/man3/*
