#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : click-log
Version  : 0.3.2
Release  : 18
URL      : https://files.pythonhosted.org/packages/22/44/3d73579b547f0790a2723728088c96189c8b52bd2ee3c3de8040efc3c1b8/click-log-0.3.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/22/44/3d73579b547f0790a2723728088c96189c8b52bd2ee3c3de8040efc3c1b8/click-log-0.3.2.tar.gz
Summary  : Logging integration for Click
Group    : Development/Tools
License  : MIT
Requires: click-log-license = %{version}-%{release}
Requires: click-log-python = %{version}-%{release}
Requires: click-log-python3 = %{version}-%{release}
Requires: click
BuildRequires : buildreq-distutils3
BuildRequires : click

%description
=========

%package license
Summary: license components for the click-log package.
Group: Default

%description license
license components for the click-log package.


%package python
Summary: python components for the click-log package.
Group: Default
Requires: click-log-python3 = %{version}-%{release}

%description python
python components for the click-log package.


%package python3
Summary: python3 components for the click-log package.
Group: Default
Requires: python3-core
Provides: pypi(click_log)
Requires: pypi(click)

%description python3
python3 components for the click-log package.


%prep
%setup -q -n click-log-0.3.2
cd %{_builddir}/click-log-0.3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583532110
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

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/click-log
cp %{_builddir}/click-log-0.3.2/LICENSE %{buildroot}/usr/share/package-licenses/click-log/1b7db61b365ff259f15a33a8123b21e58384a36e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/click-log/1b7db61b365ff259f15a33a8123b21e58384a36e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
