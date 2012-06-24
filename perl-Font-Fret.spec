%include	/usr/lib/rpm/macros.perl
%define		__find_requires	%{_builddir}/Font-Fret-%{version}/find-perl-requires
Summary:	Font-Fret perl module
Summary(pl):	Modu� perla Font-Fret
Name:		perl-Font-Fret
Version:	1.003
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Font/Font-Fret-%{version}.tar.gz
Patch:		perl-Font-Fret-dep.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Font-AFM
BuildRequires:	perl-Font-TTF
BuildRequires:	perl-Text-PDF
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Font-Fret - Font REporting Tool.

%description -l pl
Modu� perla Font-Fret.

%prep
%setup -q -n Font-Fret-%{version}
%patch -p1

chmod +x find-perl-requires

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Font/Fret
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*.plx

%{perl_sitelib}/Font/Fret.pm
%{perl_sitearch}/auto/Font/Fret

%{_mandir}/man3/*
