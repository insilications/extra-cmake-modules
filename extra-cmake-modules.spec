#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : extra-cmake-modules
Version  : 5.52.0
Release  : 16
URL      : https://download.kde.org/stable/frameworks/5.52/extra-cmake-modules-5.52.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.52/extra-cmake-modules-5.52.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.52/extra-cmake-modules-5.52.0.tar.xz.sig
Summary  : KF5CoreAddons test
Group    : Development/Tools
License  : BSD-3-Clause
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : doxygen
BuildRequires : extra-cmake-modules pkgconfig(egl)
BuildRequires : extra-cmake-modules qttools-dev
BuildRequires : extra-cmake-modules wayland
BuildRequires : glibc-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(bluez)
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(enchant)
BuildRequires : pkgconfig(exiv2)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(libpcre)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libpulse-mainloop-glib)
BuildRequires : pkgconfig(libseccomp)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : python3
BuildRequires : qttools-dev
Patch1: better-xdg-dir.patch

%description
these are additional cmake modules required for compiling KDE3 or KDE4
applications with cmake. Some of them are enhanced versions of the files
coming with cmake, some of them are NOT yet part of cmake.
To use them, copy them into the cmake Module directory or
run "cmake ."  followed by "make install"

%prep
%setup -q -n extra-cmake-modules-5.52.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541863579
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :

%install
export SOURCE_DATE_EPOCH=1541863579
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/extra-cmake-modules
cp COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/extra-cmake-modules/COPYING-CMAKE-SCRIPTS
cp attic/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/extra-cmake-modules/attic_modules_COPYING-CMAKE-SCRIPTS
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
