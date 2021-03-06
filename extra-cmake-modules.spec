#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : extra-cmake-modules
Version  : 5.92.0
Release  : 306
URL      : file:///aot/build/clearlinux/packages/extra-cmake-modules/extra-cmake-modules-v5.92.0.tar.gz
Source0  : file:///aot/build/clearlinux/packages/extra-cmake-modules/extra-cmake-modules-v5.92.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: extra-cmake-modules-data = %{version}-%{release}
Requires: extra-cmake-modules-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : pkg-config
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(epoxy)
BuildRequires : pkgconfig(exiv2)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(iso-codes)
BuildRequires : pkgconfig(libcanberra)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libpulse-mainloop-glib)
BuildRequires : pkgconfig(libseccomp)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(mount)
BuildRequires : pkgconfig(taglib)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : pypi-sphinx
BuildRequires : python3-dev
BuildRequires : qtbase-dev
BuildRequires : qtdeclarative-dev
BuildRequires : qttools-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: better-xdg-dir.patch

%description
No detailed description available

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


%package man
Summary: man components for the extra-cmake-modules package.
Group: Default

%description man
man components for the extra-cmake-modules package.


%prep
%setup -q -n extra-cmake-modules
cd %{_builddir}/extra-cmake-modules
%patch1 -p1

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1647613713
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
## altflags1
unset ASFLAGS
export CFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -pthread -Wl,--build-id=sha1 -Wno-inline"
export ASMFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -pthread -Wl,--build-id=sha1 -Wno-inline"
export CXXFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -pthread -Wl,--build-id=sha1 -Wno-inline"
export FCFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -pthread -Wl,--build-id=sha1 -Wno-inline"
export FFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -pthread -Wl,--build-id=sha1 -Wno-inline"
export LDFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -pthread -Wl,--build-id=sha1 -Wno-inline"
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
export MAKEFLAGS=%{?_smp_mflags}
%global _lto_cflags 1
%global _disable_maintainer_mode 1
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
export LD_LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/local/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
export CPATH="/usr/local/cuda/include"
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH="/usr/share/defaults/fonts"
export GTK_IM_MODULE="xim"
export QT_IM_MODULE="cedilla"
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export NO_AT_BRIDGE=1
export GTK_A11Y=none
export PLASMA_USE_QT_SCALING=1
export QT_AUTO_SCREEN_SCALE_FACTOR=0
export QT_ENABLE_HIGHDPI_SCALING=0
export QT_FONT_DPI=88
export GTK_USE_PORTAL=1
export DESKTOP_SESSION=plasma
## altflags1 end
%cmake .. -DKDE_INSTALL_CONFDIR=/usr/share/xdg \
-DBUILD_TESTING:BOOL=OFF
make  %{?_smp_mflags}    V=1 VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1647613713
rm -rf %{buildroot}
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
## altflags1
unset ASFLAGS
export CFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -pthread -Wl,--build-id=sha1 -Wno-inline"
export ASMFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -pthread -Wl,--build-id=sha1 -Wno-inline"
export CXXFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -pthread -Wl,--build-id=sha1 -Wno-inline"
export FCFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -pthread -Wl,--build-id=sha1 -Wno-inline"
export FFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -pthread -Wl,--build-id=sha1 -Wno-inline"
export LDFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -pthread -Wl,--build-id=sha1 -Wno-inline"
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
export MAKEFLAGS=%{?_smp_mflags}
%global _lto_cflags 1
%global _disable_maintainer_mode 1
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
export LD_LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/local/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
export CPATH="/usr/local/cuda/include"
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH="/usr/share/defaults/fonts"
export GTK_IM_MODULE="xim"
export QT_IM_MODULE="cedilla"
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export NO_AT_BRIDGE=1
export GTK_A11Y=none
export PLASMA_USE_QT_SCALING=1
export QT_AUTO_SCREEN_SCALE_FACTOR=0
export QT_ENABLE_HIGHDPI_SCALING=0
export QT_FONT_DPI=88
export GTK_USE_PORTAL=1
export DESKTOP_SESSION=plasma
## altflags1 end
pushd clr-build
%make_install
popd
## start %find_lang macro

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/ECM/cmake/ECMConfig.cmake
/usr/share/ECM/cmake/ECMConfigVersion.cmake
/usr/share/ECM/find-modules/ECMFindModuleHelpersStub.cmake
/usr/share/ECM/find-modules/Find7z.cmake
/usr/share/ECM/find-modules/FindCanberra.cmake
/usr/share/ECM/find-modules/FindEGL.cmake
/usr/share/ECM/find-modules/FindGLIB2.cmake
/usr/share/ECM/find-modules/FindGperf.cmake
/usr/share/ECM/find-modules/FindGradle.cmake
/usr/share/ECM/find-modules/FindIcoTool.cmake
/usr/share/ECM/find-modules/FindInotify.cmake
/usr/share/ECM/find-modules/FindIsoCodes.cmake
/usr/share/ECM/find-modules/FindKF5.cmake
/usr/share/ECM/find-modules/FindLibExiv2.cmake
/usr/share/ECM/find-modules/FindLibGit2.cmake
/usr/share/ECM/find-modules/FindLibMount.cmake
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
/usr/share/ECM/find-modules/Findgzip.cmake
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
/usr/share/ECM/kde-modules/KDEFrameworkCompilerLegacySettings.cmake
/usr/share/ECM/kde-modules/KDEFrameworkCompilerSettings.cmake
/usr/share/ECM/kde-modules/KDEGitCommitHooks.cmake
/usr/share/ECM/kde-modules/KDEInstallDirs.cmake
/usr/share/ECM/kde-modules/KDEInstallDirs5.cmake
/usr/share/ECM/kde-modules/KDEInstallDirs6.cmake
/usr/share/ECM/kde-modules/KDEInstallDirsCommon.cmake
/usr/share/ECM/kde-modules/KDEMetaInfoPlatformCheck.cmake
/usr/share/ECM/kde-modules/KDEPackageAppTemplates.cmake
/usr/share/ECM/kde-modules/KDESetupPrefixScript.cmake
/usr/share/ECM/kde-modules/appstreamtest.cmake
/usr/share/ECM/kde-modules/clang-format.cmake
/usr/share/ECM/kde-modules/kde-git-commit-hooks/clang-format.sh
/usr/share/ECM/kde-modules/kde-git-commit-hooks/pre-commit.in
/usr/share/ECM/kde-modules/prefix.sh.cmake
/usr/share/ECM/kde-modules/prefix.sh.fish.cmake
/usr/share/ECM/modules/CheckAtomic.cmake
/usr/share/ECM/modules/ECMAddAppIcon.cmake
/usr/share/ECM/modules/ECMAddQch.cmake
/usr/share/ECM/modules/ECMAddQtDesignerPlugin.cmake
/usr/share/ECM/modules/ECMAddTests.cmake
/usr/share/ECM/modules/ECMCheckOutboundLicense.cmake
/usr/share/ECM/modules/ECMConfiguredInstall.cmake
/usr/share/ECM/modules/ECMCoverageOption.cmake
/usr/share/ECM/modules/ECMCreateQmFromPoFiles.cmake
/usr/share/ECM/modules/ECMDeprecationSettings.cmake
/usr/share/ECM/modules/ECMEnableSanitizers.cmake
/usr/share/ECM/modules/ECMFindModuleHelpers.cmake
/usr/share/ECM/modules/ECMFindQmlModule.cmake
/usr/share/ECM/modules/ECMFindQmlModule.cmake.in
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
/usr/share/ECM/modules/ECMQmlModule.cmake
/usr/share/ECM/modules/ECMQmlModule.cpp.in
/usr/share/ECM/modules/ECMQmlModule.cpp.in.license
/usr/share/ECM/modules/ECMQmlModule.h.in
/usr/share/ECM/modules/ECMQmlModule.h.in.license
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
/usr/share/ECM/modules/QtVersionOption.cmake
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
/usr/share/doc/ECM/html/_sources/find-module/Find7z.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindCanberra.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindEGL.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindGLIB2.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindGperf.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindGradle.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindIcoTool.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindInotify.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindIsoCodes.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindKF5.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindLibExiv2.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindLibGit2.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindLibMount.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/FindLibcap.rst.txt
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
/usr/share/doc/ECM/html/_sources/find-module/Findepoxy.rst.txt
/usr/share/doc/ECM/html/_sources/find-module/Findgzip.rst.txt
/usr/share/doc/ECM/html/_sources/index.rst.txt
/usr/share/doc/ECM/html/_sources/kde-module/KDECMakeSettings.rst.txt
/usr/share/doc/ECM/html/_sources/kde-module/KDEClangFormat.rst.txt
/usr/share/doc/ECM/html/_sources/kde-module/KDECompilerSettings.rst.txt
/usr/share/doc/ECM/html/_sources/kde-module/KDEFrameworkCompilerSettings.rst.txt
/usr/share/doc/ECM/html/_sources/kde-module/KDEGitCommitHooks.rst.txt
/usr/share/doc/ECM/html/_sources/kde-module/KDEInstallDirs.rst.txt
/usr/share/doc/ECM/html/_sources/kde-module/KDEInstallDirs5.rst.txt
/usr/share/doc/ECM/html/_sources/kde-module/KDEInstallDirs6.rst.txt
/usr/share/doc/ECM/html/_sources/kde-module/KDEPackageAppTemplates.rst.txt
/usr/share/doc/ECM/html/_sources/manual/ecm-developer.7.rst.txt
/usr/share/doc/ECM/html/_sources/manual/ecm-find-modules.7.rst.txt
/usr/share/doc/ECM/html/_sources/manual/ecm-kde-modules.7.rst.txt
/usr/share/doc/ECM/html/_sources/manual/ecm-modules.7.rst.txt
/usr/share/doc/ECM/html/_sources/manual/ecm-toolchains.7.rst.txt
/usr/share/doc/ECM/html/_sources/manual/ecm.7.rst.txt
/usr/share/doc/ECM/html/_sources/module/CheckAtomic.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMAddAppIcon.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMAddQch.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMAddQtDesignerPlugin.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMAddTests.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMCheckOutboundLicense.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMConfiguredInstall.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMCoverageOption.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMCreateQmFromPoFiles.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMDeprecationSettings.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMEnableSanitizers.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMFindModuleHelpers.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMFindQmlModule.rst.txt
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
/usr/share/doc/ECM/html/_sources/module/ECMQmlModule.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMQtDeclareLoggingCategory.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMSetupQtPluginMacroNames.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMSetupVersion.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMSourceVersionControl.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMUninstallTarget.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMUseFindModules.rst.txt
/usr/share/doc/ECM/html/_sources/module/ECMWinResolveSymlinks.rst.txt
/usr/share/doc/ECM/html/_sources/module/QtVersionOption.rst.txt
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
/usr/share/doc/ECM/html/_static/underscore-1.13.1.js
/usr/share/doc/ECM/html/_static/underscore.js
/usr/share/doc/ECM/html/find-module/Find7z.html
/usr/share/doc/ECM/html/find-module/FindCanberra.html
/usr/share/doc/ECM/html/find-module/FindEGL.html
/usr/share/doc/ECM/html/find-module/FindGLIB2.html
/usr/share/doc/ECM/html/find-module/FindGperf.html
/usr/share/doc/ECM/html/find-module/FindGradle.html
/usr/share/doc/ECM/html/find-module/FindIcoTool.html
/usr/share/doc/ECM/html/find-module/FindInotify.html
/usr/share/doc/ECM/html/find-module/FindIsoCodes.html
/usr/share/doc/ECM/html/find-module/FindKF5.html
/usr/share/doc/ECM/html/find-module/FindLibExiv2.html
/usr/share/doc/ECM/html/find-module/FindLibGit2.html
/usr/share/doc/ECM/html/find-module/FindLibMount.html
/usr/share/doc/ECM/html/find-module/FindLibcap.html
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
/usr/share/doc/ECM/html/find-module/Findepoxy.html
/usr/share/doc/ECM/html/find-module/Findgzip.html
/usr/share/doc/ECM/html/genindex.html
/usr/share/doc/ECM/html/index.html
/usr/share/doc/ECM/html/kde-module/KDECMakeSettings.html
/usr/share/doc/ECM/html/kde-module/KDEClangFormat.html
/usr/share/doc/ECM/html/kde-module/KDECompilerSettings.html
/usr/share/doc/ECM/html/kde-module/KDEFrameworkCompilerSettings.html
/usr/share/doc/ECM/html/kde-module/KDEGitCommitHooks.html
/usr/share/doc/ECM/html/kde-module/KDEInstallDirs.html
/usr/share/doc/ECM/html/kde-module/KDEInstallDirs5.html
/usr/share/doc/ECM/html/kde-module/KDEInstallDirs6.html
/usr/share/doc/ECM/html/kde-module/KDEPackageAppTemplates.html
/usr/share/doc/ECM/html/manual/ecm-developer.7.html
/usr/share/doc/ECM/html/manual/ecm-find-modules.7.html
/usr/share/doc/ECM/html/manual/ecm-kde-modules.7.html
/usr/share/doc/ECM/html/manual/ecm-modules.7.html
/usr/share/doc/ECM/html/manual/ecm-toolchains.7.html
/usr/share/doc/ECM/html/manual/ecm.7.html
/usr/share/doc/ECM/html/module/CheckAtomic.html
/usr/share/doc/ECM/html/module/ECMAddAppIcon.html
/usr/share/doc/ECM/html/module/ECMAddQch.html
/usr/share/doc/ECM/html/module/ECMAddQtDesignerPlugin.html
/usr/share/doc/ECM/html/module/ECMAddTests.html
/usr/share/doc/ECM/html/module/ECMCheckOutboundLicense.html
/usr/share/doc/ECM/html/module/ECMConfiguredInstall.html
/usr/share/doc/ECM/html/module/ECMCoverageOption.html
/usr/share/doc/ECM/html/module/ECMCreateQmFromPoFiles.html
/usr/share/doc/ECM/html/module/ECMDeprecationSettings.html
/usr/share/doc/ECM/html/module/ECMEnableSanitizers.html
/usr/share/doc/ECM/html/module/ECMFindModuleHelpers.html
/usr/share/doc/ECM/html/module/ECMFindQmlModule.html
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
/usr/share/doc/ECM/html/module/ECMQmlModule.html
/usr/share/doc/ECM/html/module/ECMQtDeclareLoggingCategory.html
/usr/share/doc/ECM/html/module/ECMSetupQtPluginMacroNames.html
/usr/share/doc/ECM/html/module/ECMSetupVersion.html
/usr/share/doc/ECM/html/module/ECMSourceVersionControl.html
/usr/share/doc/ECM/html/module/ECMUninstallTarget.html
/usr/share/doc/ECM/html/module/ECMUseFindModules.html
/usr/share/doc/ECM/html/module/ECMWinResolveSymlinks.html
/usr/share/doc/ECM/html/module/QtVersionOption.html
/usr/share/doc/ECM/html/search.html
/usr/share/doc/ECM/html/searchindex.js
/usr/share/doc/ECM/html/toolchain/Android.html

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man7/ecm-developer.7
/usr/share/man/man7/ecm-find-modules.7
/usr/share/man/man7/ecm-kde-modules.7
/usr/share/man/man7/ecm-modules.7
/usr/share/man/man7/ecm-toolchains.7
/usr/share/man/man7/ecm.7
