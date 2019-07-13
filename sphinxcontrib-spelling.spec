#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3B6D06A0C428437A (doug@doughellmann.com)
#
Name     : sphinxcontrib-spelling
Version  : 4.3.0
Release  : 6
URL      : https://files.pythonhosted.org/packages/85/49/2e4089102078c181280f1a465e8e6c6f51f7fb96d4095bd43bb4825a703f/sphinxcontrib-spelling-4.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/85/49/2e4089102078c181280f1a465e8e6c6f51f7fb96d4095bd43bb4825a703f/sphinxcontrib-spelling-4.3.0.tar.gz
Source99 : https://files.pythonhosted.org/packages/85/49/2e4089102078c181280f1a465e8e6c6f51f7fb96d4095bd43bb4825a703f/sphinxcontrib-spelling-4.3.0.tar.gz.asc
Summary  : Sphinx spelling extension
Group    : Development/Tools
License  : BSD-2-Clause
Requires: sphinxcontrib-spelling-license = %{version}-%{release}
Requires: sphinxcontrib-spelling-python = %{version}-%{release}
Requires: sphinxcontrib-spelling-python3 = %{version}-%{release}
Requires: Sphinx
Requires: flake8
Requires: six
BuildRequires : Sphinx
BuildRequires : buildreq-distutils3
BuildRequires : flake8
BuildRequires : pbr
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyenchant
BuildRequires : pytest
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
=========================
sphinxcontrib-spelling
=========================
This package contains sphinxcontrb.spelling, a spelling checker for
Sphinx-based documentation.  It uses PyEnchant_ to produce a report
showing misspelled words.  Note: PyEnchant is now unmaintained.

%package license
Summary: license components for the sphinxcontrib-spelling package.
Group: Default

%description license
license components for the sphinxcontrib-spelling package.


%package python
Summary: python components for the sphinxcontrib-spelling package.
Group: Default
Requires: sphinxcontrib-spelling-python3 = %{version}-%{release}

%description python
python components for the sphinxcontrib-spelling package.


%package python3
Summary: python3 components for the sphinxcontrib-spelling package.
Group: Default
Requires: python3-core

%description python3
python3 components for the sphinxcontrib-spelling package.


%prep
%setup -q -n sphinxcontrib-spelling-4.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1560781911
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sphinxcontrib-spelling
cp LICENSE %{buildroot}/usr/share/package-licenses/sphinxcontrib-spelling/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sphinxcontrib-spelling/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
