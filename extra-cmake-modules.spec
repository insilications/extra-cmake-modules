#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : extra-cmake-modules
Version  : 5.77.0
Release  : 54
URL      : https://download.kde.org/stable/frameworks/5.77/extra-cmake-modules-5.77.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.77/extra-cmake-modules-5.77.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.77/extra-cmake-modules-5.77.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause MIT
Requires: extra-cmake-modules-data = %{version}-%{release}
Requires: extra-cmake-modules-license = %{version}-%{release}
Requires: extra-cmake-modules-man = %{version}-%{release}
BuildRequires : Sphinx
BuildRequires : buildreq-cmake
BuildRequires : doxygen
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
BuildRequires : pkgconfig(libcanberra)
BuildRequires : pkgconfig(libpcre)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libpulse-mainloop-glib)
BuildRequires : pkgconfig(libseccomp)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : qtbase-dev
BuildRequires : qtdeclarative-dev
BuildRequires : qttools-dev
Patch1: better-xdg-dir.patch

%description
these are additional cmake modules required for compiling KDE3 or KDE4
applications with cmake. Some of them are enhanced versions of the files
coming with cmake, some of them are NOT yet part of cmake.
To use them, copy them into the cmake Module directory or
run "cmake ."  followed by "make install"

%package data
Summary: data components for the extra-cmake-modules package.
Group: Data

%description data
data components for the extra-cmake-modules package.


%package doc
Summary: doc components for the extra-cmake-modules package.
Group: Documentation
Requires: extra-cmake-modules-man = %{version}-%{release}

%description doc
doc components for the extra-cmake-modules package.


%package license
Summary: license components for the extra-cmake-modules package.
Group: Default

%description license
license components for the extra-cmake-modules package.


%package man
Summary: man components for the extra-cmake-modules package.
Group: Default

%description man
man components for the extra-cmake-modules package.


%prep
%setup -q -n extra-cmake-modules-5.77.0
cd %{_builddir}/extra-cmake-modules-5.77.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607962212
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
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :

%install
export SOURCE_DATE_EPOCH=1607962212
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/extra-cmake-modules
cp %{_builddir}/extra-cmake-modules-5.77.0/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/extra-cmake-modules/ff3ed70db4739b3c6747c7f624fe2bad70802987
cp %{_builddir}/extra-cmake-modules-5.77.0/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/extra-cmake-modules/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
cp %{_builddir}/extra-cmake-modules-5.77.0/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/extra-cmake-modules/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/extra-cmake-modules-5.77.0/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/extra-cmake-modules/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
cp %{_builddir}/extra-cmake-modules-5.77.0/attic/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/extra-cmake-modules/ff3ed70db4739b3c6747c7f624fe2bad70802987
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
/usr/share/ECM/find-modules/FindKF5.cmake
/usr/share/ECM/find-modules/FindLibExiv2.cmake
/usr/share/ECM/find-modules/FindLibGit2.cmake
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
/usr/share/ECM/kde-modules/KDEInstallDirs.cmake
/usr/share/ECM/kde-modules/KDEPackageAppTemplates.cmake
/usr/share/ECM/kde-modules/appstreamtest.cmake
/usr/share/ECM/kde-modules/clang-format.cmake
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

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/ECM/html/_sources/find-module/FindCanberra.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindEGL.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindFontconfig.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindGLIB2.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindGperf.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindGradle.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindIcoTool.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindInotify.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindKF5.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindLibExiv2.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindLibGit2.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindOpenEXR.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindPhoneNumber.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindPoppler.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindPulseAudio.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindQtWaylandScanner.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindSasl2.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindSeccomp.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindSharedMimeInfo.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindTaglib.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindUDev.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindWayland.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindWaylandProtocols.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindWaylandScanner.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindX11_XCB.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindXCB.rst.txt
/usr/share/doc/ECM/html/_sources/index.rst.txt
/usr/share/doc/ECM/html/_sources/kde-module/KDECMakeSettings.rst.txt
/usr/share/doc/ECM/html/_sources/kde-module/KDEClangFormat.rst.txt
/usr/share/doc/ECM/html/_sources/kde-module/KDECompilerSettings.rst.txt
/usr/share/doc/ECM/html/_sources/kde-module/KDEFrameworkCompilerSettings.rst.txt
/usr/share/doc/ECM/html/_sources/kde-module/KDEInstallDirs.rst.txt
/usr/share/doc/ECM/html/_sources/kde-module/KDEPackageAppTemplates.rst.txt
/usr/share/doc/ECM/html/_sources/manual/ecm-developer.7.rst.txt
/usr/share/doc/ECM/html/_sources/manual/ecm-find-modules.7.rst.txt
/usr/share/doc/ECM/html/_sources/manual/ecm-kde-modules.7.rst.txt
/usr/share/doc/ECM/html/_sources/manual/ecm-modules.7.rst.txt
/usr/share/doc/ECM/html/_sources/manual/ecm-toolchains.7.rst.txt
/usr/share/doc/ECM/html/_sources/manual/ecm.7.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMAddAppIcon.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMAddQch.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMAddQtDesignerPlugin.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMAddTests.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMCheckOutboundLicense.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMConfiguredInstall.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMCoverageOption.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMCreateQmFromPoFiles.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMEnableSanitizers.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMFindModuleHelpers.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMGenerateDBusServiceFile.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMGenerateExportHeader.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMGenerateHeaders.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMGeneratePkgConfigFile.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMGeneratePriFile.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMGenerateQmlTypes.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMInstallIcons.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMMarkAsTest.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMMarkNonGuiExecutable.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMOptionalAddSubdirectory.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMPackageConfigHelpers.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMPoQmTools.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMQMLModules.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMQtDeclareLoggingCategory.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMSetupQtPluginMacroNames.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMSetupVersion.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMSourceVersionControl.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMUninstallTarget.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMUseFindModules.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMWinResolveSymlinks.rst.txt
/usr/share/doc/ECM/html/_sources/toolchain/Android.rst.txt
/usr/share/doc/ECM/html/_static/basic.css
/usr/share/doc/ECM/html/_static/classic.css
/usr/share/doc/ECM/html/_static/default.css
/usr/share/doc/ECM/html/_static/doctools.js
/usr/share/doc/ECM/html/_static/documentation_options.js
/usr/share/doc/ECM/html/_static/ecm.css
/usr/share/doc/ECM/html/_static/file.png
/usr/share/doc/ECM/html/_static/jquery-3.5.1.js
/usr/share/doc/ECM/html/_static/jquery.js
/usr/share/doc/ECM/html/_static/kde-favicon.ico
/usr/share/doc/ECM/html/_static/language_data.js
/usr/share/doc/ECM/html/_static/minus.png
/usr/share/doc/ECM/html/_static/plus.png
/usr/share/doc/ECM/html/_static/pygments.css
/usr/share/doc/ECM/html/_static/searchtools.js
/usr/share/doc/ECM/html/_static/sidebar.js
/usr/share/doc/ECM/html/_static/underscore-1.3.1.js
/usr/share/doc/ECM/html/_static/underscore.js
/usr/share/doc/ECM/html/find-module/FindCanberra.html
/usr/share/doc/ECM/html/find-module/FindEGL.html
/usr/share/doc/ECM/html/find-module/FindFontconfig.html
/usr/share/doc/ECM/html/find-module/FindGLIB2.html
/usr/share/doc/ECM/html/find-module/FindGperf.html
/usr/share/doc/ECM/html/find-module/FindGradle.html
/usr/share/doc/ECM/html/find-module/FindIcoTool.html
/usr/share/doc/ECM/html/find-module/FindInotify.html
/usr/share/doc/ECM/html/find-module/FindKF5.html
/usr/share/doc/ECM/html/find-module/FindLibExiv2.html
/usr/share/doc/ECM/html/find-module/FindLibGit2.html
/usr/share/doc/ECM/html/find-module/FindOpenEXR.html
/usr/share/doc/ECM/html/find-module/FindPhoneNumber.html
/usr/share/doc/ECM/html/find-module/FindPoppler.html
/usr/share/doc/ECM/html/find-module/FindPulseAudio.html
/usr/share/doc/ECM/html/find-module/FindQtWaylandScanner.html
/usr/share/doc/ECM/html/find-module/FindSasl2.html
/usr/share/doc/ECM/html/find-module/FindSeccomp.html
/usr/share/doc/ECM/html/find-module/FindSharedMimeInfo.html
/usr/share/doc/ECM/html/find-module/FindTaglib.html
/usr/share/doc/ECM/html/find-module/FindUDev.html
/usr/share/doc/ECM/html/find-module/FindWayland.html
/usr/share/doc/ECM/html/find-module/FindWaylandProtocols.html
/usr/share/doc/ECM/html/find-module/FindWaylandScanner.html
/usr/share/doc/ECM/html/find-module/FindX11_XCB.html
/usr/share/doc/ECM/html/find-module/FindXCB.html
/usr/share/doc/ECM/html/genindex.html
/usr/share/doc/ECM/html/index.html
/usr/share/doc/ECM/html/kde-module/KDECMakeSettings.html
/usr/share/doc/ECM/html/kde-module/KDEClangFormat.html
/usr/share/doc/ECM/html/kde-module/KDECompilerSettings.html
/usr/share/doc/ECM/html/kde-module/KDEFrameworkCompilerSettings.html
/usr/share/doc/ECM/html/kde-module/KDEInstallDirs.html
/usr/share/doc/ECM/html/kde-module/KDEPackageAppTemplates.html
/usr/share/doc/ECM/html/manual/ecm-developer.7.html
/usr/share/doc/ECM/html/manual/ecm-find-modules.7.html
/usr/share/doc/ECM/html/manual/ecm-kde-modules.7.html
/usr/share/doc/ECM/html/manual/ecm-modules.7.html
/usr/share/doc/ECM/html/manual/ecm-toolchains.7.html
/usr/share/doc/ECM/html/manual/ecm.7.html
/usr/share/doc/ECM/html/module/ECMAddAppIcon.html
/usr/share/doc/ECM/html/module/ECMAddQch.html
/usr/share/doc/ECM/html/module/ECMAddQtDesignerPlugin.html
/usr/share/doc/ECM/html/module/ECMAddTests.html
/usr/share/doc/ECM/html/module/ECMCheckOutboundLicense.html
/usr/share/doc/ECM/html/module/ECMConfiguredInstall.html
/usr/share/doc/ECM/html/module/ECMCoverageOption.html
/usr/share/doc/ECM/html/module/ECMCreateQmFromPoFiles.html
/usr/share/doc/ECM/html/module/ECMEnableSanitizers.html
/usr/share/doc/ECM/html/module/ECMFindModuleHelpers.html
/usr/share/doc/ECM/html/module/ECMGenerateDBusServiceFile.html
/usr/share/doc/ECM/html/module/ECMGenerateExportHeader.html
/usr/share/doc/ECM/html/module/ECMGenerateHeaders.html
/usr/share/doc/ECM/html/module/ECMGeneratePkgConfigFile.html
/usr/share/doc/ECM/html/module/ECMGeneratePriFile.html
/usr/share/doc/ECM/html/module/ECMGenerateQmlTypes.html
/usr/share/doc/ECM/html/module/ECMInstallIcons.html
/usr/share/doc/ECM/html/module/ECMMarkAsTest.html
/usr/share/doc/ECM/html/module/ECMMarkNonGuiExecutable.html
/usr/share/doc/ECM/html/module/ECMOptionalAddSubdirectory.html
/usr/share/doc/ECM/html/module/ECMPackageConfigHelpers.html
/usr/share/doc/ECM/html/module/ECMPoQmTools.html
/usr/share/doc/ECM/html/module/ECMQMLModules.html
/usr/share/doc/ECM/html/module/ECMQtDeclareLoggingCategory.html
/usr/share/doc/ECM/html/module/ECMSetupQtPluginMacroNames.html
/usr/share/doc/ECM/html/module/ECMSetupVersion.html
/usr/share/doc/ECM/html/module/ECMSourceVersionControl.html
/usr/share/doc/ECM/html/module/ECMUninstallTarget.html
/usr/share/doc/ECM/html/module/ECMUseFindModules.html
/usr/share/doc/ECM/html/module/ECMWinResolveSymlinks.html
/usr/share/doc/ECM/html/search.html
/usr/share/doc/ECM/html/searchindex.js
/usr/share/doc/ECM/html/toolchain/Android.html

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/extra-cmake-modules/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
/usr/share/package-licenses/extra-cmake-modules/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/extra-cmake-modules/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
/usr/share/package-licenses/extra-cmake-modules/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man7/ecm-developer.7
/usr/share/man/man7/ecm-find-modules.7
/usr/share/man/man7/ecm-kde-modules.7
/usr/share/man/man7/ecm-modules.7
/usr/share/man/man7/ecm-toolchains.7
/usr/share/man/man7/ecm.7
