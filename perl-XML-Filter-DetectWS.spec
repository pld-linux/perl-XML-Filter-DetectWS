#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	XML
%define		pnam	Filter-DetectWS
Summary:	XML::Filter::DetectWS - a PerlSAX filter that detects ignorable whitespace
Summary(pl.UTF-8):	XML::Filter::DetectWS - filtr PerlSAX wykrywający ignorowalne spacje
Name:		perl-XML-Filter-DetectWS
Version:	0.01
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ebab5b30d80c3fc5a0bee8d3fe8aa477
URL:		http://search.cpan.org/dist/XML-Filter-DetectWS/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-Filter-SAXT
%endif
Obsoletes:	perl-libxml-enno
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This a PerlSAX filter that detects which character data contains
ignorable whitespace and optionally filters it.

%description -l pl.UTF-8
To jest filtr PerlSAX wykrywający dane znakowe zawierające ignorowalne
spacje i opcjonalnie filtrujący je.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/Filter/DetectWS.pm
%{_mandir}/man3/*
