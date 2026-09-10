cmake_minimum_required(VERSION 3.12.0)
project(aidl)

#require clang++
#  https://android.googlesource.com/platform/system/logging.git
#  https://android.googlesource.com/platform/system/core.git
#  https://android.googlesource.com/platform/system/base.git

find_package(fmt CONFIG REQUIRED)
find_package(GTest CONFIG REQUIRED)

# required for libbase to compile
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_EXTENSIONS ON)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_library(liblog STATIC
	logging/liblog/log_event_list.cpp
	logging/liblog/log_event_write.cpp
	logging/liblog/logger_name.cpp
	logging/liblog/logger_read.cpp
	logging/liblog/logger_write.cpp
	logging/liblog/properties.cpp
	logging/liblog/logprint.cpp)

target_compile_definitions(liblog PRIVATE
	-DLIBLOG_LOG_TAG=1006 -D_XOPEN_SOURCE=700 -DFAKE_LOG_DEVICE=1)
target_include_directories(liblog PUBLIC
	core/include
	logging/liblog/include
	core/libcutils/include
	libbase/include)


add_library(libbase STATIC
    libbase/chrono_utils.cpp
    libbase/cmsg.cpp
    libbase/file.cpp
    libbase/hex.cpp
    libbase/logging.cpp
    libbase/mapped_file.cpp
    libbase/parsebool.cpp
    libbase/parsenetaddress.cpp
    libbase/posix_strerror_r.cpp
    libbase/process.cpp
    libbase/properties.cpp
    libbase/result.cpp
    libbase/stringprintf.cpp
    libbase/strings.cpp
    libbase/threads.cpp
    libbase/errors_unix.cpp)

#target_include_directories(libbase PUBLIC
#	libbase/include core/include)
target_include_directories(libbase PUBLIC
	libbase/include )
target_link_libraries(libbase PUBLIC fmt::fmt liblog)



find_package(BISON REQUIRED)
find_package(FLEX REQUIRED)

bison_target(aidl_language_y 
	aidl/aidl_language_y.yy
	${CMAKE_CURRENT_BINARY_DIR}/gen/aidl_language_y.cpp
	DEFINES_FILE ${CMAKE_CURRENT_BINARY_DIR}/gen/aidl_language_y.h
)
flex_target(aidl_language_l 
	aidl/aidl_language_l.ll
	${CMAKE_CURRENT_BINARY_DIR}/gen/aidl_language_l.cpp
	DEFINES_FILE ${CMAKE_CURRENT_BINARY_DIR}/gen/aidl_language_l.h
	)

set(libaidl-common_SOURCES 
	aidl/aidl_checkapi.cpp
	aidl/aidl_const_expressions.cpp
	aidl/aidl_dumpapi.cpp
	aidl/aidl_language.cpp
	aidl/aidl_to_common.cpp
	aidl/aidl_to_cpp_common.cpp
	aidl/aidl_to_cpp.cpp
	aidl/aidl_to_java.cpp
	aidl/aidl_to_ndk.cpp
	aidl/aidl_to_rust.cpp
	aidl/aidl_typenames.cpp
	aidl/aidl.cpp
	aidl/ast_java.cpp
	aidl/check_valid.cpp
	aidl/code_writer.cpp
	aidl/comments.cpp
	aidl/diagnostics.cpp
	aidl/generate_aidl_mappings.cpp
	aidl/generate_cpp.cpp
	aidl/generate_cpp_analyzer.cpp
	aidl/generate_java_binder.cpp
	aidl/generate_java.cpp
	aidl/generate_ndk.cpp
	aidl/generate_rust.cpp
	aidl/import_resolver.cpp
	aidl/io_delegate.cpp
	aidl/location.cpp
	aidl/logging.cpp
	aidl/options.cpp
	aidl/parser.cpp
	aidl/permission.cpp
	aidl/preprocess.cpp
	${BISON_aidl_language_y_OUTPUTS}
	${FLEX_aidl_language_l_OUTPUTS}
)

add_library(libaidl-common STATIC ${libaidl-common_SOURCES} )

target_compile_definitions(libaidl-common PRIVATE -D_GNU_SOURCE)
# TODO -DPLATFORM_SDK_VERSION=
target_include_directories(libaidl-common PRIVATE
	# generated aidl_language_y.cpp (in build folder) requires "aidl_language.h" (in source folder)
	${CMAKE_CURRENT_SOURCE_DIR}/aidl
	aidl/include
	# parser.cpp requires aidl_language_y.h which is in build folder
	${CMAKE_CURRENT_BINARY_DIR}/gen
	libbase/include)


#target_link_libraries(libaidl-common PUBLIC libbase)


add_executable(aidl aidl/main.cpp)

target_include_directories(aidl PRIVATE core/include libbase/include aidl/include)
target_link_libraries(aidl
	libaidl-common
	libbase
	liblog
	gtest
)
