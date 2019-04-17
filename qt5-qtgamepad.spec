%define major 5
%define libname %mklibname qt5gamepad %{major}
%define devname %mklibname qt5gamepad -d
%define beta %{nil}

Name: qt5-qtgamepad
Version: 5.12.3
%if "%{beta}" != "%{nil}"
%define qttarballdir qtgamepad-everywhere-src-%{version}-%{beta}
Source0: http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%(echo %{beta} |sed -e "s,1$,,")/submodules/%{qttarballdir}.tar.xz
Release: 0.%{beta}.1
%else
%define qttarballdir qtgamepad-everywhere-src-%{version}
Source0: http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
Release: 1
%endif
Summary: Qt gamepad library
URL: https://github.com/qtproject/qtgamepad
License: LGPL-2.1-with-Qt-Company-Qt-exception-1.1 or LGPL-3.0-with-Qt-Company-Qt-exception-1.1
Group: System/Libraries
BuildRequires: qmake5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(sdl2)
BuildRequires: %mklibname -s -d qt5devicediscoverysupport
# For the Provides: generator
BuildRequires: cmake >= 3.11.0-1

%description
The Qt Gamepad module provides a Qt style API to Gamepad controllers.

%package -n %{libname}
Summary: Qt gamepad library
Group: System/Libraries

%description -n %{libname}
Qt gamepad library.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%package examples
Summary: Example code for the %{name} library
Group: Development/C
Requires: %{devname} = %{EVRD}
BuildRequires: pkgconfig(Qt5Widgets)

%description examples
Example code for the %{name} library.

%prep
%autosetup -n %{qttarballdir} -p1
%qmake_qt5 *.pro

%build
%make_build

%install
%make_install install_docs INSTALL_ROOT="%{buildroot}"

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/qt5/qml/QtGamepad
%{_libdir}/qt5/plugins/gamepads

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/Qt5Gamepad
%{_libdir}/qt5/mkspecs/modules/*.pri
%{_libdir}/*.prl

%files examples
%{_libdir}/qt5/examples/gamepad
