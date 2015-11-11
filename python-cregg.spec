%global modname cregg
%global commit d0ada477c5b2189f0f4ee1f28eb3cd7507ecd9a6
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Upstream hasn't ported to python3 yet
# https://github.com/mwaskom/cregg/issues/1
%global with_python3 0

Name:		python-cregg
Version:	0.1
Release:	1.dev.git%{shortcommit}%{?dist}
Summary:	Utilities for running psychology experiments
License:	BSD
URL:		https://github.com/mwaskom/cregg/
Source0:	https://github.com/mwaskom/cregg/archive/%{commit}/%{modname}-%{shortcommit}.tar.gz
BuildArch:      noarch

%description
Tools for Psychology Experiments
Contains a set of reusable classes and functions that
support the collection of data from experimental subjects.
Some of these tools assume a tightly integrated design
ecosystem; others will be more generally useful. At the
moment these are not separated out very well.

%prep
%autosetup -n %{modname}-%{commit}

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
BuildRequires:  python-nose
BuildRequires:  numpy
BuildRequires:  python-pandas
BuildRequires:  python2-psychopy
BuildRequires:  python-pyglet

%description -n python2-%{modname}
Tools for Psychology Experiments
Contains a set of reusable classes and functions that
support the collection of data from experimental subjects.
Some of these tools assume a tightly integrated design
ecosystem; others will be more generally useful. At the
moment these are not separated out very well.

Python 2 version.

%if %{with_python3}
%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-nose
BuildRequires:  python3-numpy
BuildRequires:  python3-pandas
BuildRequires:  python3-psychopy
BuildRequires:  python3-pyglet


%description -n python3-%{modname}
Tools for Psychology Experiments
Contains a set of reusable classes and functions that
support the collection of data from experimental subjects.
Some of these tools assume a tightly integrated design
ecosystem; others will be more generally useful. At the
moment these are not separated out very well.

Python 3 version.
%endif

%build
%py2_build

%if %{with_python3}
%py3_build
%endif

%install
%py2_install

%if %{with_python3}
%py3_install
%endif

%check
nosetests-%{python2_version} -v

%if %{with_python3}
nosetests-%{python3_version} -v
%endif

%files -n python2-%{modname}
%license LICENSE
%doc README.md
%{python2_sitelib}/%{modname}*

%if %{with_python3}
%files -n python3-%{modname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{modname}*
%endif 

%changelog
* Tue Nov 10 2015 Adrian Alves <alvesadrian@fedoraporject.org> - 0.1-1
- Initial package
