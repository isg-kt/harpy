# File: CMakeLists.txt
# Brief: Main entry point for the Harpy project CMake build system.
#
# This file is part of the Harpy project and is licensed under the
# 3-Clause BSD License;
# For more information, see LICENSE.txt.
cmake_minimum_required(VERSION 3.31)

set(HARPY_ROOT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}")
set(HARPY_BUILD_DIRECTORY "${HARPY_ROOT_DIRECTORY}/build")

add_subdirectory(configuration)

project(Harpy
  LANGUAGES CXX
  VERSION 0.0.0
  DESCRIPTION "The Harpy Programming Language Compiler and Linker"
  HOMEPAGE_URL "https://github.com/isg-kt/harpy")

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

if(NOT CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  message(FATAL_ERROR
    "Critical error: Invalid C++ Compiler: ${CMAKE_CXX_COMPILER_ID}.\n"
    "The Harpy Compiler is strictly dependent on the Clang++ compiler.")
endif()

add_library(global_configuration INTERFACE)

target_compile_options(global_configuration INTERFACE
  -Wall -Wextra -Wpedantic -fno-exceptions -fno-rtti
  -fno-omit-frame-pointer -nostdinc++ -fno-common
  -DHarpyIsOnLinux -DHarpyIsOnAmd64)
target_link_options(global_configuration INTERFACE
  -Wl,--fatal-warnings
  -Wl,--as-needed)

if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  set(CMAKE_BUILD_TYPE "release"
    CACHE STRING "Choose the type of build."
    FORCE)
endif()

string(TOLOWER "${CMAKE_BUILD_TYPE}" build_type)

if(build_type MATCHES "^debug")
  target_compile_options(global_configuration INTERFACE
    -O0 -g3 -Wshadow -Wconversion -Wsign-conversion -Wcast-align
    -Wnull-dereference -Wdouble-promotion -Wformat=2
    -Wimplicit-fallthrough -Wvla -Woverloaded-virtual -Wnon-virtual-dtor
    -Wold-style-cast -fstack-protector-all -fstack-clash-protection
    -fcf-protection=full -ftrivial-auto-var-init=pattern
    -DHarpyIsInDebugMode)

  get_target_property(actual_configuration global_configuration
    INTERFACE_COMPILE_OPTIONS)
  message("Message: Selected Flags: ${actual_configuration}")

elseif(build_type MATCHES "^sanitizer")
  target_compile_options(global_configuration INTERFACE
    -O1 -g3 -fsanitize=address,undefined -fno-sanitize-recover=all
    -fno-omit-frame-pointer -DHarpyIsInDebugMode)
  target_link_options(global_configuration INTERFACE
    -fsanitize=address,undefined)

  get_target_property(actual_configuration global_configuration
    INTERFACE_COMPILE_OPTIONS)
  message("Message: Selected Flags: ${actual_configuration}")

elseif(build_type MATCHES "^valgrind")
  find_package(PkgConfig REQUIRED)
  pkg_check_modules(VALGRIND
    REQUIRED valgrind
    IMPORTED_TARGET valgrind)

  if(VALGRIND_LIBRARY_DIRS)
    target_link_directories(global_configuration INTERFACE
      ${VALGRIND_LIBRARY_DIRS})
  endif()

  target_link_libraries(global_configuration INTERFACE
    PkgConfig::VALGRIND)
  target_compile_options(global_configuration INTERFACE
    -Og -g3 -fno-omit-frame-pointer -DHarpyIsInDebugMode
    -DValgrindIsActive)

  get_target_property(actual_configuration global_configuration
    INTERFACE_COMPILE_OPTIONS)
  message("Message: Selected Flags: ${actual_configuration}")

elseif(build_type MATCHES "^test")
  target_compile_options(global_configuration INTERFACE
    -O0 -g3 -Werror -fstack-protector-all -DHarpyIsInDebugMode
    -DHarpyIsInTestMode)

  get_target_property(actual_configuration global_configuration
    INTERFACE_COMPILE_OPTIONS)
  message("Message: Selected Flags: ${actual_configuration}")

elseif(build_type MATCHES "^release-test")
  target_compile_options(global_configuration INTERFACE
    -O3 -flto -Werror -fno-semantic-interposition
    -DHarpyIsInTestMode)
  target_link_options(global_configuration INTERFACE
    -flto -Wl,--gc-sections)

  get_target_property(actual_configuration global_configuration
    INTERFACE_COMPILE_OPTIONS)
  message("Message: Selected Flags: ${actual_configuration}")

elseif(build_type MATCHES "^release" OR "${CMAKE_BUILD_TYPE}" STREQUAL "")
  target_compile_options(global_configuration INTERFACE
    -O3 -flto -Werror -fno-semantic-interposition)
  target_link_options(global_configuration INTERFACE
    -flto -Wl,--gc-sections)

  get_target_property(actual_configuration global_configuration
    INTERFACE_COMPILE_OPTIONS)
  message("Message: Selected Flags: ${actual_configuration}")

else()
  message(FATAL_ERROR
    "Critical error: Invalid build type: ${CMAKE_BUILD_TYPE}.\n"
    "Help:\n"
    "\t-DCMAKE_BUILD_TYPE=debug\n"
    "\t-DCMAKE_BUILD_TYPE=valgrind\n"
    "\t-DCMAKE_BUILD_TYPE=sanitizer\n"
    "\t-DCMAKE_BUILD_TYPE=test\n"
    "\t-DCMAKE_BUILD_TYPE=release-test\n"
    "\t-DCMAKE_BUILD_TYPE=release")
endif()

message("Message: Build Type Detected: ${build_type}")
