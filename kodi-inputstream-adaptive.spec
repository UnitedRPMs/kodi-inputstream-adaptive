%global kodi_version 18.0
%global realname inputstream.adaptive
%global _build_id_links none

%global __provides_exclude_from %{_libdir}/kodi/addons/%{realname}
%global __requires_exclude_from %{_libdir}/kodi/addons/%{realname}

%global __provides_exclude_from %{_datadir}/kodi/addons/%{realname}
%global __requires_exclude_from %{_datadir}/kodi/addons/%{realname}

Name:           kodi-inputstream-adaptive
Version:        2.4.4

Release:        7%{?dist}
Summary:        InputStream client for adaptive streams for Kodi 18+

Group:          Applications/Multimedia
License:        GPLv2+
Url:            https://github.com/peak3d/inputstream.adaptive/
Source0:        https://github.com/peak3d/inputstream.adaptive/archive/%{version}-Leia.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  kodi-platform-devel
BuildRequires:  expat-devel

Requires:       kodi >= %{kodi_version}

ExcludeArch:    %{power64} ppc64le

%description
InputStream client for adaptive streams for Kodi 18+.

%prep
%autosetup -n %{realname}-%{version}-Leia 


%build
%cmake .
%make_build

%install
%make_install
sed -i 's|special://home/cdm|%{_libdir}/kodi/addons/inputstream.adaptive|g' "%{buildroot}/%{_datadir}/kodi/addons/inputstream.adaptive/resources/settings.xml"

%files
%defattr(755, root, root)
%doc %{_datadir}/kodi/addons/%{realname}/changelog.txt
%{_libdir}/kodi/addons/%{realname}/
%{_datadir}/kodi/addons/%{realname}/

%changelog

* Thu Apr 09 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2.4.4-7
- Updated to 2.4.4

* Sat Mar 21 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2.4.3-7
- Updated to 2.4.3

* Tue Sep 03 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2.4.2-7
- Updated to 2.4.2

* Sat Jun 22 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2.3.22-7
- Initial build
