#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	25.08.0
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kpublictransport
Summary:	A library for accessing realtime public transport data
Name:		ka6-%{kaname}
Version:	25.08.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	b52690c92486127fb17db4618122d73e
URL:		https://community.kde.org/KDE_PIM/KDE_Itinerary
BuildRequires:	Qt6Core-devel >= 5.15.2
BuildRequires:	Qt6Gui-devel >= 5.15.2
BuildRequires:	Qt6Network-devel >= 5.15.2
BuildRequires:	Qt6Qml-devel >= 5.15.2
BuildRequires:	Qt6Quick-devel
BuildRequires:	kf6-extra-cmake-modules >= 5.91
BuildRequires:	ninja
BuildRequires:	polyclipping-devel
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for accessing realtime public transport data and for
performing public transport journey queries.

This includes:
- Finding bus stops or train stations, departures/arrivals from there,
  and journeys between those.
- Path and routing information for individual transport sections of a
  journey.
- Information about train coach and train station platform layouts.
- Information about rental vehicle positions and availability, such as
  shared bikes or scooters.
- Realtime information about the operational status of elevators or
  escalators.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ka5-%{kaname}-devel < %{version}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%doc README.md
%ghost %{_libdir}/libKPublicTransport.so.1
%attr(755,root,root) %{_libdir}/libKPublicTransport.so.*.*
%ghost %{_libdir}/libKPublicTransportOnboard.so.1
%attr(755,root,root) %{_libdir}/libKPublicTransportOnboard.so.*.*
%dir %{_libdir}/qt6/qml/org/kde/kpublictransport
%{_libdir}/qt6/qml/org/kde/kpublictransport/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/kpublictransport/kpublictransportqmlplugin.qmltypes
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kpublictransport/libkpublictransportqmlplugin.so
%dir %{_libdir}/qt6/qml/org/kde/kpublictransport/onboard
%{_libdir}/qt6/qml/org/kde/kpublictransport/onboard/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/kpublictransport/onboard/kpublictransportonboardqmlplugin.qmltypes
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kpublictransport/onboard/libkpublictransportonboardqmlplugin.so
%{_libdir}/qt6/qml/org/kde/kpublictransport/onboard/qmldir
%{_libdir}/qt6/qml/org/kde/kpublictransport/qmldir
%dir %{_libdir}/qt6/qml/org/kde/kpublictransport/ui
%{_libdir}/qt6/qml/org/kde/kpublictransport/ui/VehicleSectionItem.qml
%{_libdir}/qt6/qml/org/kde/kpublictransport/ui/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/kpublictransport/ui/kpublictransportquickplugin.qmltypes
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kpublictransport/ui/libkpublictransportquickplugin.so
%{_libdir}/qt6/qml/org/kde/kpublictransport/ui/qmldir
%{_datadir}/qlogging-categories6/org_kde_kpublictransport.categories
%{_datadir}/qlogging-categories6/org_kde_kpublictransport_onboard.categories
%{_libdir}/qt6/qml/org/kde/kpublictransport/ui/FeatureIcon.qml
%{_libdir}/qt6/qml/org/kde/kpublictransport/ui/OccupancyIndicator.qml
%{_libdir}/qt6/qml/org/kde/kpublictransport/ui/JourneyHorizontalBar.qml
%{_libdir}/qt6/qml/org/kde/kpublictransport/ui/TransportIcon.qml
%{_libdir}/qt6/qml/org/kde/kpublictransport/ui/TransportNameControl.qml
%{_libdir}/qt6/qml/org/kde/kpublictransport/ui/BackendPage.qml
%{_libdir}/qt6/qml/org/kde/kpublictransport/ui/ExpectedTimeLabel.qml
%{_libdir}/qt6/qml/org/kde/kpublictransport/ui/FeatureDelegate.qml
%{_libdir}/qt6/qml/org/kde/kpublictransport/ui/OccupancyDelegate.qml
%{_libdir}/qt6/qml/org/kde/kpublictransport/ui/StopPickerPage.qml
%{_libdir}/qt6/qml/org/kde/kpublictransport/ui/StopoverInformationView.qml
%{_libdir}/qt6/qml/org/kde/kpublictransport/ui/VehicleLayoutView.qml
%{_libdir}/qt6/qml/org/kde/kpublictransport/ui/VehicleSectionDelegate.qml
%dir %{_libdir}/qt6/qml/org/kde/kpublictransport/ui/private
%{_libdir}/qt6/qml/org/kde/kpublictransport/ui/private/CountryComboBox.qml

%files devel
%defattr(644,root,root,755)
%{_includedir}/KPublicTransport
%{_libdir}/cmake/KPublicTransport
%{_libdir}/libKPublicTransport.so
%{_libdir}/libKPublicTransportOnboard.so
