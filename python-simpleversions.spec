%define unmangled_name simpleversions

Name: python-%{unmangled_name}
Version: 0.1.4
Release: 1
Summary: Library for sorting versions using a simple versioning scheme
License: MIT
Group: Development/Libraries
Url: https://github.com/amplify-education/simpleversions
Source0: %{unmangled_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

BuildRequires: python
BuildRequires: python-setuptools
# RHEL 5 and 6 ship with sphinx 0.6, but sphinx 1.0 is available with
# a different package name in EPEL.
%if "%{_vendor}" == "redhat" && 0%{?rhel} <= 6 && 0%{?fedora} == 0
BuildRequires:    python-sphinx10
# python-sphinx10 doesn't set sys.path correctly; do it for them
%global pythonpath %(find %{python_sitelib} -name Sphinx*.egg)
%else
BuildRequires:    python-sphinx >= 1.0
%endif

%description
Library for sorting versions using a simple versioning scheme.

%prep
%setup -qn %{unmangled_name}-%{version}

%build
%{__python} setup.py build
%{?pythonpath: PYTHONPATH="%{pythonpath}"} \
    %{__python} setup.py build_sphinx

%install
%{__python} setup.py install -O1 --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README.rst
%doc build/sphinx/html/*

%changelog
* Wed Oct 09 2013 Chris St. Pierre <chris.a.st.pierre@gmail.com>
- 

