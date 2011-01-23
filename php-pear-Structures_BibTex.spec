%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	Structures_BibTex
%define		subver	RC5
%define		rel		1
Summary:	%{_pearname} - Handling of BibTex Data
Summary(pl.UTF-8):	%{_pearname} - obsługa danych BibTex
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	%{subver}.%{rel}
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	5ee36427873c272dceb0d1563eb04b4e
URL:		http://pear.php.net/package/Structures_BibTex/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
Obsoletes:	%{name}-tests
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parsing BibTex data to an array and converting an array to BibTex
Data.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten umożliwia konwersję danych BibTex do tablicy PHP oraz z
tablicy PHP do danych BibTex.

Ta klasa ma w PEAR status: %{_status}.

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
