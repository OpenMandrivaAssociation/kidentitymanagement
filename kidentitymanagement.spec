%define major 5
%define libname %mklibname KF5IdentityManagement %{major}
%define devname %mklibname KF5IdentityManagement -d

Name: kidentitymanagement
Version:	22.12.1
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Summary: KDE library for mail transport
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Akonadi)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5PimTextEdit) >= 5.8.2
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Mime)
BuildRequires: cmake(KF5Wallet)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Test)
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
Conflicts:	kde-l10n < 17.04.0

%description
KDE library for mail transport.

%package -n %{libname}
Summary: KDE library for mail transport
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE library for mail transport.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libkpimidentities5

%files -f libkpimidentities5.lang
%{_datadir}/qlogging-categories5/kidentitymanagement.categories
%{_datadir}/qlogging-categories5/kidentitymanagement.renamecategories
%{_datadir}/dbus-1/interfaces/*.xml

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
%doc %{_docdir}/qt5/*.{qch,tags}
