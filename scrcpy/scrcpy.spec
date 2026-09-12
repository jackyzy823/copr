# based on https://github.com/useidel/scrcpy-fedora/blob/main/scrcpy.spec
Name:           scrcpy
Version:        4.1
Release:        %autorelease
Summary:        Display and control your Android device
License:        ASL 2.0 AND Apache-2.0

%global         forgeurl        https://github.com/Genymobile/%{name}
%forgemeta -i

URL:            %{forgeurl}
Source0:        %{forgesource}

# Patch generated from https://github.com/jackyzy823/scrcpy/tree/v4.1_desugar
Patch0:         0001-Desugar-lambda-function-and-method-reference.patch
Patch1:         0002-Optionally-Desugar-static-methods-in-interface.patch
Patch2:         0003-Force-InvokeVirtual-instead-of-InvokeInterface.patch

# android stub file for sdk 37 not yet available
%global 	sdk_version 36
%global		android_version android-17.0.0_r1
## Tools to build scrcpy-server
## To build aidl
Source1:	https://android.googlesource.com/platform/system/tools/aidl/+archive/%{android_version}.tar.gz#/aidl.tar.gz
Source2:	https://android.googlesource.com/platform/system/libbase/+archive/%{android_version}.tar.gz#/libbase.tar.gz
Source3:	https://android.googlesource.com/platform/system/logging/+archive/%{android_version}.tar.gz#/logging.tar.gz
Source4:    https://android.googlesource.com/platform/system/core/+archive/%{android_version}.tar.gz#/core.tar.gz
# cmake file for aidl
Source5:	CMakeLists.txt

## To build d8
Source6:	https://android.googlesource.com/platform/dalvik/+archive/%{android_version}.tar.gz#/dalvik.tar.gz
## build core-lambda-stubs.jar

## To build android.jar
## noramlly we should use metalava on source files to generate signature files and stub java class.
## however it's not possbile to build metalava

## this jar is a zip of stub java file. (not compiled class file)
## to download single file "?format=TEXT" is required, however it is base64 encoded
## could download folder as a tar.gz, however other files may have license issue, like android.jar
## or the last way we manually craft all missing stub dependencies for scrcpy-server (about 3.2M / 8M of original stub.jar) (1.7M/4.9M of compiled)
Source7:	https://android.googlesource.com/platform/prebuilts/fullsdk/platforms/+/refs/heads/main/android-%{sdk_version}/android-stubs-src.jar?format=TEXT#/android-stubs-src.jar.b64

## framework.aidl
## https://android.googlesource.com/platform/prebuilts/fullsdk/platforms/+/refs/heads/main/android-36.tar.gz 
## however this contains properietry assets 
## The link is not downloadable
## https://android.googlesource.com/platform/prebuilts/fullsdk/platforms/+/refs/heads/main/android-36/framework.aidl
## The links' content is base64 encoded
## https://android.googlesource.com/platform/prebuilts/fullsdk/platforms/+/refs/heads/main/android-36/framework.aidl?format=text
## so we just craft our own framework.aidl with necessary imports in prep step.


BuildRequires:  meson
BuildRequires:  cmake

BuildRequires:  java-devel
BuildRequires:  libusb1-devel 
BuildRequires:  pkgconfig(libavdevice)
#BuildRequires:  pkgconfig(ffmpeg)

BuildRequires:  pkgconfig(sdl3)
BuildRequires:  pkgconfig(ffms2)
BuildRequires:  pkgconfig(libusb-1.0)


## Build `aidl`
# aidl requires clang to build, so we make scrcpy use clang too
BuildRequires:	clang
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	pkgconfig(fmt)
BuildRequires:	pkgconfig(gtest)


Requires:       adb
# otherwise use --video-codec=vp9
Requires:       openh264

# https://github.com/Genymobile/scrcpy/blob/master/FAQ.md#issue-with-wayland
Recommends:       libdecor

%description
This application provides display and control of Android devices
connected on USB (or over TCP/IP).

%prep
%forgesetup
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

mkdir -p server/deps && cp %{SOURCE5} server/deps
(mkdir -p server/deps/aidl && tar zxf %{SOURCE1} -C server/deps/aidl)
(mkdir -p server/deps/libbase && tar zxf %{SOURCE2} -C server/deps/libbase)
(mkdir -p server/deps/logging && tar zxf %{SOURCE3} -C server/deps/logging)
(mkdir -p server/deps/core && tar zxf %{SOURCE4} -C server/deps/core)
(mkdir -p server/deps/dx && tar zxf %{SOURCE6} -C server/deps/dx)
(mkdir -p server/deps/android && cd server/deps/android && base64 -d %{SOURCE7} | jar -x)
# `| -x -C target` doesn't work on jar from JDK < 25
%dnl (mkdir -p server/deps/android && base64 -d %{SOURCE7} | jar -x -C server/deps/android)

## add all `import` found in scrcpy/server/src/main/aidl/
cat <<EOF > server/deps/framework.aidl
@JavaOnlyStableParcelable parcelable android.graphics.Rect;
@JavaOnlyStableParcelable parcelable android.content.res.Configuration;
EOF

## (Currently in build stage) sed annontation in android-stubs-src.jar to pass compile

%build
echo %{_builddir}
# build aidl (aidl requires clang to compile)
pushd server/deps
%cmake -DCMAKE_CXX_COMPILER=clang++
%cmake_build
popd

# build d8
pushd server/deps/dx
find dx/src -iname *.java > dx.txt
javac --source 1.8 --target 1.8 @dx.txt -d bin
jar --create --file dx.jar --manifest dx/etc/manifest.txt   -C bin .
popd

# build android.jar
pushd server/deps/android
# remove missing annotation (TODO move to prep?)
find -iname *.java -exec sed -i 's/@android.annotation.NonNull//g' {} \;
find -iname *.java -exec sed -i 's/@android.annotation.Nullable//g' {} \;
find -iname *.java -exec sed -i 's/@androidx.annotation.RecentlyNonNull//g' {} \;
find -iname *.java -exec sed -i 's/@androidx.annotation.RecentlyNullable//g' {} \;
find -iname *.java -exec sed -i -E 's/@android.annotation.SdkConstant\(.*?\)//g' {} \;
find -iname *.java > android.txt
javac --target 1.8 --source 1.8   @android.txt -d bin
jar --create --file android.jar  -C bin .
popd

# build server
pushd server
mkdir build
mkdir -p build/classes
mkdir -p build/gen/com/genymobile/scrcpy

cat <<EOF > build/gen/com/genymobile/scrcpy/BuildConfig.java
package com.genymobile.scrcpy;

public final class BuildConfig {
  public static final boolean DEBUG = false;
  public static final String VERSION_NAME = "%{version}";
}
EOF
popd

# use aidl generate java file
pushd server/src/main/aidl
../../../deps/%{__cmake_builddir}/aidl -o ../../../build/gen -I. android/content/IOnPrimaryClipChangedListener.aidl
../../../deps/%{__cmake_builddir}/aidl -o ../../../build/gen -I. -p ../../../deps/framework.aidl android/view/IDisplayWindowListener.aidl
popd


FAKE_SRC=( \
    android/content/*java \
)

SRC=( \
    com/genymobile/scrcpy/*.java \
    com/genymobile/scrcpy/audio/*.java \
    com/genymobile/scrcpy/control/*.java \
    com/genymobile/scrcpy/device/*.java \
    com/genymobile/scrcpy/display/*.java \
    com/genymobile/scrcpy/model/*.java \
    com/genymobile/scrcpy/opengl/*.java \
    com/genymobile/scrcpy/util/*.java \
    com/genymobile/scrcpy/video/*.java \
    com/genymobile/scrcpy/wrappers/*.java \
)

CLASSES=()
for src in "${SRC[@]}"
do
    CLASSES+=("${src%.java}.class")
done


# compile server with android.jar
pushd server/src/main/java

javac -encoding UTF-8 -bootclasspath ../../../deps/android/android.jar \
    -cp "../../../build/gen" \
    -d "../../../build/classes" \
    -source 1.8 -target 1.8 \
    ${FAKE_SRC[@]} \
    ${SRC[@]}


popd

# convert jar to dex with d8
pushd server/build/classes
# Current min-sdk-version is 13 (dx default)
java -jar ../../deps/dx/dx.jar --dex --output ../../build/classes.dex android/view/*.class android/content/*.class ${CLASSES[@]}
# If you skip patch1 0002-Optionally-Desugar-static-methods-in-interface.patch, then you could use following cmdline args to pass the convert.
# java -jar ../../deps/dx/dx.jar --allow-all-interface-method-invokes --min-sdk-version=21 --dex --output ../../build/classes.dex android/view/*.class android/content/*.class ${CLASSES[@]}
popd


pushd server/build
jar cvf scrcpy-server classes.dex
popd


# build client part
%meson -Db_lto=true -Dprebuilt_server='server/build/scrcpy-server'
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md FAQ.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/applications/%{name}*.desktop


%changelog
%autochangelog
