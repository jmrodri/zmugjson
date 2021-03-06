%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           zmugjson
Version:        0.1.2
Release:        1.git.9.9bcd42c
Summary:        zmugjson a smugmug.com JSON api
Group:          Applications/Multimedia
License:        GPL
URL:            https://github.com/jmrodri/zmugjson
Source0:        zmugjson-git-9.9bcd42c.tar.gz
BuildRoot:      %{_tmppath}/%{name}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python
BuildRequires:  python-simplejson
BuildRequires:  python-setuptools
Requires:       python >= 2.3
Requires:       python-simplejson

%description
A JSON-based api wrapper used to connect to smugmug.com

%prep
%setup -q -n zmugjson-git-9.9bcd42c

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
#install -d -m 755 %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

install -d -m 755 %{buildroot}%{_usr}/share/doc/%{name}-%{version}/
install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}/
install -m 644 LICENSE.TXT %{buildroot}%{_usr}/share/doc/%{name}-%{version}/
install -m 644 logger.conf %{buildroot}%{_sysconfdir}/%{name}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/%{name}/zmugjson.py*
%{python_sitelib}/%{name}/__init__.py*
%{python_sitelib}/%{name}/config.py*
%{python_sitelib}/zmugjson-*.egg-info
%{_usr}/share/doc/%{name}-%{version}/LICENSE.TXT
%config %{_sysconfdir}/%{name}/logger.conf

%changelog
* Tue Oct 08 2013 jesus m. rodriguez <jmrodri@gmail.com> 0.1.2-1
- Changed version (jmrodri@gmail.com)

* Tue Oct 08 2013 jesus m. rodriguez <jmrodri@gmail.com> 0.1.1-1
- new package built with tito

* Tue Oct 30 2007 Jesus Rodriguez <jmrodri at gmail dot com> 0.1-1
- initial rpm release
