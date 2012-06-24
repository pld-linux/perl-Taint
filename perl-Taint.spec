#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Taint
Summary:	Taint - Perl utility extensions for tainted data
Summary(pl):	Taint - rozszerzenia narz�dziowe Perla dla napi�tnowanych danych
Name:		perl-Taint
Version:	0.09
Release:	0.1
License:	not distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# NoSource0-md5:	e9b23bec1f15ee2f1e1d7309eb04ef92
NoSource:	0
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl has the ability to mark data as 'tainted', as described in
perlsec(1). Perl will prevent tainted data from being used for some
operations, and you may wish to add such caution to your own code. The
routines in this module provide convenient ways to taint data and to
check data for taint. To remove the taint from data, use the method
described in perlsec(1), or use the make_extractor routine.

%description -l pl
Perl ma mo�liwo�� oznaczenia danych jako "napi�tnowane" zgodznie z
opisem w perlsec(1). Interpreter nie pozwala na u�ywanie
napi�tnowanych danych w niekt�rych operacjach, a mo�emy chcie� doda�
taki warunek w swoim kodzie. Funkcje z tego modu�u udost�pniaj�
wygodne metody do pi�tnowania danych oraz sprawdzania danych pod tym
k�tem. Aby usun�� pi�tno z danych mo�na u�y� metody opisanej w
perlsec(1) lub wywo�a� funkcj� make_extractor.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

# some tests fail - check again
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Taint.pm
%{_mandir}/man3/*
