#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : extra-cmake-modules
Version  : 5.82.0
Release  : 62
URL      : https://download.kde.org/stable/frameworks/5.82/extra-cmake-modules-5.82.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.82/extra-cmake-modules-5.82.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.82/extra-cmake-modules-5.82.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause MIT
Requires: extra-cmake-modules-data = %{version}-%{release}
Requires: extra-cmake-modules-license = %{version}-%{release}
BuildRequires : Sphinx
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : karchive-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(epoxy)
BuildRequires : pkgconfig(exiv2)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(iso-codes)
BuildRequires : pkgconfig(libcanberra)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libpulse-mainloop-glib)
BuildRequires : pkgconfig(libseccomp)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : python3-dev
BuildRequires : qtbase-dev
BuildRequires : qtdeclarative-dev
BuildRequires : qttools-dev
Patch1: better-xdg-dir.patch

%description
# Extra CMake Modules
## Introduction
The Extra CMake Modules package, or ECM, adds to the modules provided by CMake,
including ones used by ``find_package()`` to find common software, ones that
can be used directly in ``CMakeLists.txt`` files to perform common tasks and
toolchain files that must be specified on the commandline by the user.

%package data
Summary: data components for the extra-cmake-modules package.
Group: Data

%description data
data components for the extra-cmake-modules package.


%package license
Summary: license components for the extra-cmake-modules package.
Group: Default

%description license
license components for the extra-cmake-modules package.


%prep
%setup -q -n extra-cmake-modules-5.82.0
cd %{_builddir}/extra-cmake-modules-5.82.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623350898
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake .. -DBUILD_HTML_DOCS=OFF \
-DBUILD_MAN_DOCS=OFF
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :

%install
export SOURCE_DATE_EPOCH=1623350898
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/extra-cmake-modules
cp %{_builddir}/extra-cmake-modules-5.82.0/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/extra-cmake-modules/ff3ed70db4739b3c6747c7f624fe2bad70802987
cp %{_builddir}/extra-cmake-modules-5.82.0/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/extra-cmake-modules/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
cp %{_builddir}/extra-cmake-modules-5.82.0/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/extra-cmake-modules/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/extra-cmake-modules-5.82.0/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/extra-cmake-modules/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/ECM/cmake/ECMConfig.cmake
/usr/share/ECM/cmake/ECMConfigVersion.cmake
/usr/share/ECM/find-modules/ECMFindModuleHelpersStub.cmake
/usr/share/ECM/find-modules/FindCanberra.cmake
/usr/share/ECM/find-modules/FindEGL.cmake
/usr/share/ECM/find-modules/FindFontconfig.cmake
/usr/share/ECM/find-modules/FindGLIB2.cmake
/usr/share/ECM/find-modules/FindGperf.cmake
/usr/share/ECM/find-modules/FindGradle.cmake
/usr/share/ECM/find-modules/FindIcoTool.cmake
/usr/share/ECM/find-modules/FindInotify.cmake
/usr/share/ECM/find-modules/FindIsoCodes.cmake
/usr/share/ECM/find-modules/FindKF5.cmake
/usr/share/ECM/find-modules/FindLibExiv2.cmake
/usr/share/ECM/find-modules/FindLibGit2.cmake
/usr/share/ECM/find-modules/FindLibcap.cmake
/usr/share/ECM/find-modules/FindOpenEXR.cmake
/usr/share/ECM/find-modules/FindPhoneNumber.cmake
/usr/share/ECM/find-modules/FindPoppler.cmake
/usr/share/ECM/find-modules/FindPulseAudio.cmake
/usr/share/ECM/find-modules/FindPythonModuleGeneration.cmake
/usr/share/ECM/find-modules/FindQHelpGenerator.cmake
/usr/share/ECM/find-modules/FindQtWaylandScanner.cmake
/usr/share/ECM/find-modules/FindReuseTool.cmake
/usr/share/ECM/find-modules/FindSasl2.cmake
/usr/share/ECM/find-modules/FindSeccomp.cmake
/usr/share/ECM/find-modules/FindSharedMimeInfo.cmake
/usr/share/ECM/find-modules/FindTaglib.cmake
/usr/share/ECM/find-modules/FindUDev.cmake
/usr/share/ECM/find-modules/FindWayland.cmake
/usr/share/ECM/find-modules/FindWaylandProtocols.cmake
/usr/share/ECM/find-modules/FindWaylandScanner.cmake
/usr/share/ECM/find-modules/FindX11_XCB.cmake
/usr/share/ECM/find-modules/FindXCB.cmake
/usr/share/ECM/find-modules/Findepoxy.cmake
/usr/share/ECM/find-modules/GeneratePythonBindingUmbrellaModule.cmake
/usr/share/ECM/find-modules/Qt5Ruleset.py
/usr/share/ECM/find-modules/local.properties.cmake
/usr/share/ECM/find-modules/rules_engine.py
/usr/share/ECM/find-modules/run-sip.py
/usr/share/ECM/find-modules/settings.gradle.cmake
/usr/share/ECM/find-modules/sip_generator.py
/usr/share/ECM/kde-modules/KDECMakeSettings.cmake
/usr/share/ECM/kde-modules/KDEClangFormat.cmake
/usr/share/ECM/kde-modules/KDECompilerSettings.cmake
/usr/share/ECM/kde-modules/KDEFrameworkCompilerSettings.cmake
/usr/share/ECM/kde-modules/KDEGitCommitHooks.cmake
/usr/share/ECM/kde-modules/KDEInstallDirs.cmake
/usr/share/ECM/kde-modules/KDEPackageAppTemplates.cmake
/usr/share/ECM/kde-modules/appstreamtest.cmake
/usr/share/ECM/kde-modules/clang-format.cmake
/usr/share/ECM/kde-modules/kde-git-commit-hooks/clang-format.sh
/usr/share/ECM/kde-modules/kde-git-commit-hooks/pre-commit.in
/usr/share/ECM/kde-modules/prefix.sh.cmake
/usr/share/ECM/modules/CheckAtomic.cmake
/usr/share/ECM/modules/ECMAddAppIcon.cmake
/usr/share/ECM/modules/ECMAddQch.cmake
/usr/share/ECM/modules/ECMAddQtDesignerPlugin.cmake
/usr/share/ECM/modules/ECMAddTests.cmake
/usr/share/ECM/modules/ECMCheckOutboundLicense.cmake
/usr/share/ECM/modules/ECMConfiguredInstall.cmake
/usr/share/ECM/modules/ECMCoverageOption.cmake
/usr/share/ECM/modules/ECMCreateQmFromPoFiles.cmake
/usr/share/ECM/modules/ECMEnableSanitizers.cmake
/usr/share/ECM/modules/ECMFindModuleHelpers.cmake
/usr/share/ECM/modules/ECMFindQMLModule.cmake.in
/usr/share/ECM/modules/ECMGenerateDBusServiceFile.cmake
/usr/share/ECM/modules/ECMGenerateExportHeader.cmake
/usr/share/ECM/modules/ECMGenerateHeaders.cmake
/usr/share/ECM/modules/ECMGeneratePkgConfigFile.cmake
/usr/share/ECM/modules/ECMGeneratePriFile.cmake
/usr/share/ECM/modules/ECMGenerateQmlTypes.cmake
/usr/share/ECM/modules/ECMInstallIcons.cmake
/usr/share/ECM/modules/ECMMarkAsTest.cmake
/usr/share/ECM/modules/ECMMarkNonGuiExecutable.cmake
/usr/share/ECM/modules/ECMOptionalAddSubdirectory.cmake
/usr/share/ECM/modules/ECMPackageConfigHelpers.cmake
/usr/share/ECM/modules/ECMPoQmTools.cmake
/usr/share/ECM/modules/ECMQMLModules.cmake
/usr/share/ECM/modules/ECMQchDoxygen.config.in
/usr/share/ECM/modules/ECMQchDoxygenLayout.xml
/usr/share/ECM/modules/ECMQmLoader.cpp.in
/usr/share/ECM/modules/ECMQtDeclareLoggingCategory.cmake
/usr/share/ECM/modules/ECMQtDeclareLoggingCategory.cpp.in
/usr/share/ECM/modules/ECMQtDeclareLoggingCategory.h.in
/usr/share/ECM/modules/ECMQueryQmake.cmake
/usr/share/ECM/modules/ECMSetupQtPluginMacroNames.cmake
/usr/share/ECM/modules/ECMSetupVersion.cmake
/usr/share/ECM/modules/ECMSourceVersionControl.cmake
/usr/share/ECM/modules/ECMUninstallTarget.cmake
/usr/share/ECM/modules/ECMUseFindModules.cmake
/usr/share/ECM/modules/ECMVersionHeader.h.in
/usr/share/ECM/modules/ECMWinResolveSymlinks.cmake
/usr/share/ECM/modules/check-outbound-license.py
/usr/share/ECM/modules/ecm_uninstall.cmake.in
/usr/share/ECM/test-modules/test_execute_and_compare.cmake
/usr/share/ECM/toolchain/Android.cmake
/usr/share/ECM/toolchain/ECMAndroidDeployQt.cmake
/usr/share/ECM/toolchain/deployment-file-qt514.json.in
/usr/share/ECM/toolchain/deployment-file.json.in
/usr/share/ECM/toolchain/generate-fastlane-metadata.py
/usr/share/ECM/toolchain/hasMainSymbol.cmake
/usr/share/ECM/toolchain/specifydependencies.cmake

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/extra-cmake-modules/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
/usr/share/package-licenses/extra-cmake-modules/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/extra-cmake-modules/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
/usr/share/package-licenses/extra-cmake-modules/ff3ed70db4739b3c6747c7f624fe2bad70802987
