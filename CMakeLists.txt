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
