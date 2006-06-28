%include	/usr/lib/rpm/macros.php
%define		_class		Structures
%define		_subclass	BibTex
%define		_status		beta
%define		_pearname	Structures_BibTex

Summary:	%{_pearname} - Handling of BibTex Data
Summary(pl):	%{_pearname} - obs³uga danych BibTex
Name:		php-pear-%{_pearname}
Version:	0.0.1
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0ab919aedf168f43aa9484d9c1a9a68d
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

%description -l pl
Pakiet ten umo¿liwia konwersjê danych BibTex do tablicy PHP oraz z
tablicy PHP do danych BibTex.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/%{_pearname}/examples/Structures_BibTex_example.php
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Structures/BibTex.php
