# File: CMakeLists.txt
# Brief: Main entry point for the Harpy project CMake build system.
#
# This file is part of the Harpy project and is licensed under the
# 3-Clause BSD License;
# For more information, see LICENSE.txt.
cmake_minimum_required(VERSION 3.31)
project(Harpy
  LANGUAGES CXX
  VERSION 0.0.0
  DESCRIPTION "The Harpy Programming Language Compiler and Linker"
  HOMEPAGE_URL "https://github.com/isg-kt/harpy")

set(HARPY_ROOT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}")

add_subdirectory(configuration)
