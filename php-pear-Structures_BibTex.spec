%include	/usr/lib/rpm/macros.php
%define		_class		Structures
%define		_subclass	BibTex
%define		_status		beta
%define		_pearname	Structures_BibTex

Summary:	%{_pearname} - Handling of BibTex Data
Summary(pl.UTF-8):	%{_pearname} - obsługa danych BibTex
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	65fc18a9d3c9f2c26932d4948bd02ad6
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
