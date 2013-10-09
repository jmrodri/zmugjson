%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           zmugjson
Version:        0.2
Release:        1
Summary:        FUSE-based filesystem Smugmug client
Group:          Applications/Multimedia
License:        GPL
URL:            https://github.com/jmrodri/zmugjson
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python
BuildRequires:  python-simplejson
Requires:       python >= 2.3
Requires:       python-simplejson

%description
FUSE-based filesystem to access Smugmug

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}
#install -d -m 755 %{buildroot}%{_usr}/share/%{name}/
#install -d -m 755 %{buildroot}%{_usr}/share/doc/%{name}-%{version}/
#install -d -m 755 %{buildroot}%{_usr}/bin/
#install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}/
#install -m 644 LICENSE.TXT %{buildroot}%{_usr}/share/doc/%{name}-%{version}/
#install -m 644 smugmugrc %{buildroot}%{_usr}/share/doc/%{name}-%{version}/
#install -m 755 sm-photo-tool.py %{buildroot}%{_usr}/bin/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/zmugjson.*py*
%{python_sitelib}/config.*py*
%attr(644, root, root) /etc/%{name}/logger.conf
#%attr(755, root, root) %{_usr}/bin/%{name}
%{_usr}/share/doc/%{name}-%{version}/LICENSE.TXT
#%{_usr}/share/doc/%{name}-%{version}/smugmugrc

%changelog
* Tue Oct 08 2013 jesus m. rodriguez <jmrodri@gmail.com> 0.2-1
- new package built with tito

* Tue Oct 30 2007 Jesus Rodriguez <jmrodri at gmail dot com> 0.1-1
- initial rpm release
