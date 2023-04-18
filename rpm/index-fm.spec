%{!?_metainfodir: %global _metainfodir %{_datadir}/metainfo}

%global qt5_min_version 5.15.0
%global kf5_min_version 5.77.0

Name:       index-fm
Version:    2.2.1
Release:    1
Summary:    Maui File manager
License:    LGPL-3.0
URL:        https://mauikit.org/apps/index/
Source:     %{name}-%{version}.tar.xz
Patch0:     0001-Remove-uses-of-KIO-and-KConfig.patch
Requires:   opt-kf5-karchive >= %{kf5_min_version}
Requires:   opt-kf5-kconfig >= %{kf5_min_version}
Requires:   opt-kf5-kcoreaddons >= %{kf5_min_version}
Requires:   opt-kf5-ki18n >= %{kf5_min_version}
Requires:   opt-maui-mauikit
Requires:   opt-maui-mauikit-filebrowsing
Requires:   opt-qt5-qtbase >= %{qt5_min_version}
Requires:   opt-qt5-qtbase-gui >= %{qt5_min_version}
Requires:   opt-qt5-qtdeclarative >= %{qt5_min_version}
Requires:   opt-qt5-qtquickcontrols2 >= %{qt5_min_version}
BuildRequires:  cmake
BuildRequires:  opt-extra-cmake-modules >= %{kf5_min_version}
BuildRequires:  opt-kf5-karchive-devel >= %{kf5_min_version}
BuildRequires:  opt-kf5-kconfig-devel >= %{kf5_min_version}
BuildRequires:  opt-kf5-kcoreaddons-devel >= %{kf5_min_version}
BuildRequires:  opt-kf5-ki18n-devel >= %{kf5_min_version}
BuildRequires:  opt-kf5-rpm-macros
BuildRequires:  opt-maui-mauikit-devel
BuildRequires:  opt-maui-mauikit-filebrowsing-devel
BuildRequires:  opt-qt5-qtbase-devel >= %{qt5_min_version}
BuildRequires:  opt-qt5-qtdeclarative-devel >= %{qt5_min_version}
BuildRequires:  opt-qt5-qtquickcontrols2-devel >= %{qt5_min_version}
%{?opt_kf5_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^libMauiKit.*$

%description
The Index file manager lets you browse your system files and applications,
preview your music, text, image, and video files, and share them with
external applications.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
export QTDIR=%{_opt_qt5_prefix}

mkdir -p build
pushd build

%_opt_cmake_kf5 .. \
    -DKDE_INSTALL_BINDIR:PATH=/usr/bin \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -DQUICK_COMPILER=OFF
%make_build

popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%files
%{_bindir}/index
%{_datadir}/applications/org.kde.index.desktop
%{_datadir}/icons/hicolor/scalable/apps/index.svg
%{_datadir}/knotifications5/org.kde.index.notifyrc
%{_metainfodir}/org.kde.index.appdata.xml
%{_datadir}/locale/*/*/%{name}.mo
