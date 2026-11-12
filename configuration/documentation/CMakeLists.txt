# File: configuration/documentation/CMakeLists.txt
# Brief: Orchestrates project documentation generation subsystems.
#
# This file is part of the Harpy project and is licensed under the
# 3-Clause BSD License;
# For more information, see LICENSE.txt.
find_package(Python3 COMPONENTS Interpreter)

set(HARPY_DOCUMENTATION_DIRECTORY "${HARPY_ROOT_DIRECTORY}/documentation")

include(sphinx.cmake)

add_custom_target(docClean
  COMMAND ${CMAKE_COMMAND} -E remove_directory
    "${HARPY_SPHINX_BUILD_DIRECTORY}"
  VERBATIM)
