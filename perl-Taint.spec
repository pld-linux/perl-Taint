#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Taint
Summary:	Taint
Name:		perl-Taint
Version:	0.07
Release:	0.1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
URL:		-
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	"perl(anything_fake_or_conditional)"

%description

%description -l de

%description -l es

%description -l fr

%description -l pl

%description -l ru

%prep
%setup -q -n %{pdir}-%{version}

%build
# Don't use pipes here: they generally don't work. Apply a patch.
%{__perl} Makefile.PL
%{__make}
# if module isn't noarch, use:
# %{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
# use macros:
#%{perl_sitelib}/Taint*
%{perl_sitearch}/Taint*
%{perl_sitearch}/auto/Taint/*
%{_mandir}/man3/*
