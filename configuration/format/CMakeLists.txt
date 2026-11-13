# File: configuration/format/CMakeLists.txt
# Brief: CMake configuration for project code and documentation
# formatting targets.
#
# This file is part of the Harpy project and is licensed under the
# 3-Clause BSD License;
# For more information, see LICENSE.txt.
find_program(CLANG_FORMAT NAMES clang-format)
find_program(NODE_PACKAGE_MANAGER NAMES npm)
find_program(BLACK NAMES black)
find_program(RSTFMT NAMES rstfmt)

if (NOT Python3_FOUND OR
  NOT CLANG_FORMAT OR
  NOT NODE_PACKAGE_MANAGER OR
  NOT BLACK OR
  NOT RSTFMT)
  message(WARNING
    "[WARNING] Clang-Format, NPM, Black, RSTFMT or Python not found.\n"
    "Format targets will not be available.")
  return()
endif()

add_custom_target(format
  COMMAND ${Python3_EXECUTABLE} "${CMAKE_CURRENT_SOURCE_DIR}/format.py"
  --target all
  --root "${HARPY_ROOT_DIRECTORY}"
  WORKING_DIRECTORY "${HARPY_ROOT_DIRECTORY}"
  VERBATIM)
