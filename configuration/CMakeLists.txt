# File: configuration/CMakeLists.txt
# Brief: Project configuration and infrastructure management hub.
#
# This file is part of the Harpy project and is licensed under the
# 3-Clause BSD License;
# For more information, see LICENSE.txt.
find_package(Python3 COMPONENTS Interpreter)

add_subdirectory(documentation)
add_subdirectory(toolchain)
add_subdirectory(format)
