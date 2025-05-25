#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define major 6
%define libname %mklibname KF6IdentityManagement
%define devname %mklibname KF6IdentityManagement -d

Name: kidentitymanagement
Version:	25.04.1
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/kidentitymanagement/-/archive/%{gitbranch}/kidentitymanagement-%{gitbranchd}.tar.bz2#/kidentitymanagement-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/kidentitymanagement-%{version}.tar.xz
%endif
Summary: KDE library for mail transport
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(KPim6Akonadi)
BuildRequires: cmake(KPim6Mime)
BuildRequires: cmake(KPim6TextEdit)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant
# Renamed 2025-05-25 after 6.0
%rename plasma6-kidentitymanagement

%description
KDE library for mail transport.

%package -n %{libname}
Summary: KDE library for mail transport
Group: System/Libraries
Requires: %{name} = %{EVRD}
# Not a 1:1 replacement, but we need to get rid of old cruft
Obsoletes: %{mklibname KF5IdentityManagement 5}

%description -n %{libname}
KDE library for mail transport.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
# Not a 1:1 replacement, but we need to get rid of old cruft
Obsoletes: %{mklibname -d KF5IdentityManagement}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1 -n kidentitymanagement-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libkpimidentities6

%files -f libkpimidentities6.lang
%{_datadir}/qlogging-categories6/kidentitymanagement.categories
%{_datadir}/qlogging-categories6/kidentitymanagement.renamecategories
%{_datadir}/dbus-1/interfaces/*.xml

%files -n %{libname}
%{_libdir}/*.so*
%{_qtdir}/qml/org/kde/kidentitymanagement

%files -n %{devname}
%{_includedir}/*
%{_libdir}/cmake/*
