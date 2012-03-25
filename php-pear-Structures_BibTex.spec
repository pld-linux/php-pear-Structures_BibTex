%define		rel		1
%define		subver	RC6
%define		status		beta
%define		pearname	Structures_BibTex
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Handling of BibTex Data
Summary(pl.UTF-8):	%{pearname} - obsługa danych BibTex
Name:		php-pear-%{pearname}
Version:	1.0.0
Release:	%{subver}.%{rel}
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}%{subver}.tgz
# Source0-md5:	55259d5e18e12b3f279a9d3fc58e691d
URL:		http://pear.php.net/package/Structures_BibTex/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
Obsoletes:	php-pear-Structures_BibTex-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parsing BibTex data to an array and converting an array to BibTex
Data.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Pakiet ten umożliwia konwersję danych BibTex do tablicy PHP oraz z
tablicy PHP do danych BibTex.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/Structures_BibTex/README .

# pear/tests/pearname/tests -> pear/tests/pearname
mv ./%{php_pear_dir}/tests/%{pearname}/{tests/*,}
rmdir ./%{php_pear_dir}/tests/%{pearname}/tests

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Structures/BibTex.php
%{php_pear_dir}/Structures/BibTex
