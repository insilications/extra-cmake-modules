#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : extra-cmake-modules
Version  : 5.49.0
Release  : 7
URL      : https://github.com/KDE/extra-cmake-modules/archive/v5.49.0.tar.gz
Source0  : https://github.com/KDE/extra-cmake-modules/archive/v5.49.0.tar.gz
Summary  : KF5CoreAddons3 library.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: extra-cmake-modules-data
Requires: extra-cmake-modules-license
Requires: extra-cmake-modules-man
BuildRequires : Sphinx
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
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
BuildRequires : pkgconfig(libpcre)
BuildRequires : pkgconfig(libpulse-mainloop-glib)
BuildRequires : pkgconfig(libseccomp)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : python3
BuildRequires : qttools-dev
Patch1: better-xdg-dir.patch

%description
Plasma Applet Template
----------------------
-- Build instructions --
cd /where/your/applet/is/generated
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=MYPREFIX ..
make
make install

%package data
Summary: data components for the extra-cmake-modules package.
Group: Data

%description data
data components for the extra-cmake-modules package.


%package doc
Summary: doc components for the extra-cmake-modules package.
Group: Documentation
Requires: extra-cmake-modules-man

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
%setup -q -n extra-cmake-modules-5.49.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535423199
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pushd clr-build ; make test ||: ; popd

%install
export SOURCE_DATE_EPOCH=1535423199
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/extra-cmake-modules
cp COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/doc/extra-cmake-modules/COPYING-CMAKE-SCRIPTS
cp attic/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/doc/extra-cmake-modules/attic_modules_COPYING-CMAKE-SCRIPTS
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
/usr/share/ECM/find-modules/FindEGL.cmake
/usr/share/ECM/find-modules/FindGLIB2.cmake
/usr/share/ECM/find-modules/FindGperf.cmake
/usr/share/ECM/find-modules/FindIcoTool.cmake
/usr/share/ECM/find-modules/FindInotify.cmake
/usr/share/ECM/find-modules/FindKF5.cmake
/usr/share/ECM/find-modules/FindLibGit2.cmake
/usr/share/ECM/find-modules/FindOpenEXR.cmake
/usr/share/ECM/find-modules/FindPng2Ico.cmake
/usr/share/ECM/find-modules/FindPoppler.cmake
/usr/share/ECM/find-modules/FindPulseAudio.cmake
/usr/share/ECM/find-modules/FindPythonModuleGeneration.cmake
/usr/share/ECM/find-modules/FindQHelpGenerator.cmake
/usr/share/ECM/find-modules/FindQtWaylandScanner.cmake
/usr/share/ECM/find-modules/FindSasl2.cmake
/usr/share/ECM/find-modules/FindSeccomp.cmake
/usr/share/ECM/find-modules/FindSharedMimeInfo.cmake
/usr/share/ECM/find-modules/FindWayland.cmake
/usr/share/ECM/find-modules/FindWaylandScanner.cmake
/usr/share/ECM/find-modules/FindX11_XCB.cmake
/usr/share/ECM/find-modules/FindXCB.cmake
/usr/share/ECM/find-modules/GeneratePythonBindingUmbrellaModule.cmake
/usr/share/ECM/find-modules/Qt5Ruleset.py
/usr/share/ECM/find-modules/rules_engine.py
/usr/share/ECM/find-modules/run-sip.py
/usr/share/ECM/find-modules/sip_generator.py
/usr/share/ECM/kde-modules/KDECMakeSettings.cmake
/usr/share/ECM/kde-modules/KDECompilerSettings.cmake
/usr/share/ECM/kde-modules/KDEFrameworkCompilerSettings.cmake
/usr/share/ECM/kde-modules/KDEInstallDirs.cmake
/usr/share/ECM/kde-modules/KDEPackageAppTemplates.cmake
/usr/share/ECM/kde-modules/appstreamtest.cmake
/usr/share/ECM/kde-modules/prefix.sh.cmake
/usr/share/ECM/modules/ECMAddAppIcon.cmake
/usr/share/ECM/modules/ECMAddQch.cmake
/usr/share/ECM/modules/ECMAddTests.cmake
/usr/share/ECM/modules/ECMCoverageOption.cmake
/usr/share/ECM/modules/ECMCreateQmFromPoFiles.cmake
/usr/share/ECM/modules/ECMEnableSanitizers.cmake
/usr/share/ECM/modules/ECMFindModuleHelpers.cmake
/usr/share/ECM/modules/ECMFindQMLModule.cmake.in
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
/usr/share/ECM/modules/ECMUninstallTarget.cmake
/usr/share/ECM/modules/ECMUseFindModules.cmake
/usr/share/ECM/modules/ECMVersionHeader.h.in
/usr/share/ECM/modules/ECMWinResolveSymlinks.cmake
/usr/share/ECM/modules/ecm_uninstall.cmake.in
/usr/share/ECM/test-modules/test_execute_and_compare.cmake
/usr/share/ECM/toolchain/Android.cmake
/usr/share/ECM/toolchain/ECMAndroidDeployQt.cmake
/usr/share/ECM/toolchain/deployment-file.json.in
/usr/share/ECM/toolchain/hasMainSymbol.cmake
/usr/share/ECM/toolchain/specifydependencies.cmake

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/ECM/html/_sources/find-module/FindEGL.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindGLIB2.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindIcoTool.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindKF5.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindLibGit2.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindOpenEXR.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindPng2Ico.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindPoppler.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindPulseAudio.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindQtWaylandScanner.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindSasl2.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindSharedMimeInfo.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindWayland.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindWaylandScanner.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindX11_XCB.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindXCB.rst.txt
/usr/share/doc/ECM/html/_sources/index.rst.txt
/usr/share/doc/ECM/html/_sources/kde-module/KDECMakeSettings.rst.txt
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
/usr/share/doc/ECM/html/_sources/module/ECMAddTests.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMCoverageOption.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMCreateQmFromPoFiles.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMEnableSanitizers.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMFindModuleHelpers.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMGenerateHeaders.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMGeneratePkgConfigFile.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMGeneratePriFile.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMInstallIcons.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMMarkAsTest.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMMarkNonGuiExecutable.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMOptionalAddSubdirectory.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMPackageConfigHelpers.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMPoQmTools.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMQtDeclareLoggingCategory.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMSetupQtPluginMacroNames.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMSetupVersion.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMUninstallTarget.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMUseFindModules.rst.txt
/usr/share/doc/ECM/html/_sources/toolchain/Android.rst.txt
/usr/share/doc/ECM/html/_static/ajax-loader.gif
/usr/share/doc/ECM/html/_static/basic.css
/usr/share/doc/ECM/html/_static/classic.css
/usr/share/doc/ECM/html/_static/comment-bright.png
/usr/share/doc/ECM/html/_static/comment-close.png
/usr/share/doc/ECM/html/_static/comment.png
/usr/share/doc/ECM/html/_static/default.css
/usr/share/doc/ECM/html/_static/doctools.js
/usr/share/doc/ECM/html/_static/documentation_options.js
/usr/share/doc/ECM/html/_static/down-pressed.png
/usr/share/doc/ECM/html/_static/down.png
/usr/share/doc/ECM/html/_static/ecm.css
/usr/share/doc/ECM/html/_static/file.png
/usr/share/doc/ECM/html/_static/jquery-3.2.1.js
/usr/share/doc/ECM/html/_static/jquery.js
/usr/share/doc/ECM/html/_static/kde-favicon.ico
/usr/share/doc/ECM/html/_static/minus.png
/usr/share/doc/ECM/html/_static/plus.png
/usr/share/doc/ECM/html/_static/pygments.css
/usr/share/doc/ECM/html/_static/searchtools.js
/usr/share/doc/ECM/html/_static/sidebar.js
/usr/share/doc/ECM/html/_static/underscore-1.3.1.js
/usr/share/doc/ECM/html/_static/underscore.js
/usr/share/doc/ECM/html/_static/up-pressed.png
/usr/share/doc/ECM/html/_static/up.png
/usr/share/doc/ECM/html/_static/websupport.js
/usr/share/doc/ECM/html/find-module/FindEGL.html
/usr/share/doc/ECM/html/find-module/FindGLIB2.html
/usr/share/doc/ECM/html/find-module/FindIcoTool.html
/usr/share/doc/ECM/html/find-module/FindKF5.html
/usr/share/doc/ECM/html/find-module/FindLibGit2.html
/usr/share/doc/ECM/html/find-module/FindOpenEXR.html
/usr/share/doc/ECM/html/find-module/FindPng2Ico.html
/usr/share/doc/ECM/html/find-module/FindPoppler.html
/usr/share/doc/ECM/html/find-module/FindPulseAudio.html
/usr/share/doc/ECM/html/find-module/FindQtWaylandScanner.html
/usr/share/doc/ECM/html/find-module/FindSasl2.html
/usr/share/doc/ECM/html/find-module/FindSharedMimeInfo.html
/usr/share/doc/ECM/html/find-module/FindWayland.html
/usr/share/doc/ECM/html/find-module/FindWaylandScanner.html
/usr/share/doc/ECM/html/find-module/FindX11_XCB.html
/usr/share/doc/ECM/html/find-module/FindXCB.html
/usr/share/doc/ECM/html/genindex.html
/usr/share/doc/ECM/html/index.html
/usr/share/doc/ECM/html/kde-module/KDECMakeSettings.html
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
/usr/share/doc/ECM/html/module/ECMAddTests.html
/usr/share/doc/ECM/html/module/ECMCoverageOption.html
/usr/share/doc/ECM/html/module/ECMCreateQmFromPoFiles.html
/usr/share/doc/ECM/html/module/ECMEnableSanitizers.html
/usr/share/doc/ECM/html/module/ECMFindModuleHelpers.html
/usr/share/doc/ECM/html/module/ECMGenerateHeaders.html
/usr/share/doc/ECM/html/module/ECMGeneratePkgConfigFile.html
/usr/share/doc/ECM/html/module/ECMGeneratePriFile.html
/usr/share/doc/ECM/html/module/ECMInstallIcons.html
/usr/share/doc/ECM/html/module/ECMMarkAsTest.html
/usr/share/doc/ECM/html/module/ECMMarkNonGuiExecutable.html
/usr/share/doc/ECM/html/module/ECMOptionalAddSubdirectory.html
/usr/share/doc/ECM/html/module/ECMPackageConfigHelpers.html
/usr/share/doc/ECM/html/module/ECMPoQmTools.html
/usr/share/doc/ECM/html/module/ECMQtDeclareLoggingCategory.html
/usr/share/doc/ECM/html/module/ECMSetupQtPluginMacroNames.html
/usr/share/doc/ECM/html/module/ECMSetupVersion.html
/usr/share/doc/ECM/html/module/ECMUninstallTarget.html
/usr/share/doc/ECM/html/module/ECMUseFindModules.html
/usr/share/doc/ECM/html/search.html
/usr/share/doc/ECM/html/searchindex.js
/usr/share/doc/ECM/html/toolchain/Android.html

%files license
%defattr(-,root,root,-)
/usr/share/doc/extra-cmake-modules/COPYING-CMAKE-SCRIPTS
/usr/share/doc/extra-cmake-modules/attic_modules_COPYING-CMAKE-SCRIPTS

%files man
%defattr(-,root,root,-)
/usr/share/man/man7/ecm-developer.7
/usr/share/man/man7/ecm-find-modules.7
/usr/share/man/man7/ecm-kde-modules.7
/usr/share/man/man7/ecm-modules.7
/usr/share/man/man7/ecm-toolchains.7
/usr/share/man/man7/ecm.7
