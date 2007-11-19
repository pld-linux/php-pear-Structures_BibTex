%include	/usr/lib/rpm/macros.php
%define		_class		Structures
%define		_subclass	BibTex
%define		_status		beta
%define		_pearname	Structures_BibTex

%define		_rc	RC4
Summary:	%{_pearname} - Handling of BibTex Data
Summary(pl.UTF-8):	%{_pearname} - obsługa danych BibTex
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	%{_rc}.1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_rc}.tgz
# Source0-md5:	c49b42b4b38fd2c436420dd4c77ed5bd
URL:		http://pear.php.net/package/Structures_BibTex/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parsing BibTex data to an array and converting an array to BibTex
Data.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten umożliwia konwersję danych BibTex do tablicy PHP oraz z
tablicy PHP do danych BibTex.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

# pear/tests/pearname/tests -> pear/tests/pearname
mv ./%{php_pear_dir}/tests/%{_pearname}/{tests/*,}
rmdir ./%{php_pear_dir}/tests/%{_pearname}/tests

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Structures/BibTex.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
