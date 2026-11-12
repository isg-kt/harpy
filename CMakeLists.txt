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
