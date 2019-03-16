%define __find_provides %{nil}
%define __find_requires %{nil}
%define __strip /bin/true
%define __provides_exclude_from ^/system/.*$
%define __requires_exclude ^.*$
%global debug_package %{nil}

%define family voyager
%define device h3413

Name:          droid-system-vendor-%{family}-%{device}
Summary:       Built from source /vendor for Droid HAL adaptations
Version:       0.0.1
Release:       1
Group:         System
License:       Proprietary
Requires:      droid-system-vendor-%{family}
Source0:       %{name}-%{version}.tgz
Source1:       droid-system-vendor-%{family}-rpmlintrc
URL:           https://github.com/mer-hybris/droid-vendor-sony-nile-voyager

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}

# This section is empty by purpose
%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/vendor
cp %{device}/vendor/build.prop $RPM_BUILD_ROOT/vendor/build.prop

%files
%defattr(-,root,root,-)
/vendor/build.prop
