# File: configuration/documentation/sphinx.cmake
# Brief: Configures Sphinx documentation generation for the Harpy project.
#
# This file is part of the Harpy project and is licensed under the
# 3-Clause BSD License;
# For more information, see LICENSE.txt.
find_package(Python3 COMPONENTS Interpreter)
find_program(SPHINX_BUILD NAMES sphinx-build)

if(NOT SPHINX_BUILD)
    message(WARNING
        "[WARNING] Sphinx not found.\n"
        "Documentation targets will not be available.")
    return()
endif()

set(HARPY_SPHINX_SOURCE_DIRECTORY "${HARPY_ROOT_DIRECTORY}/documentation")
set(HARPY_SPHINX_BUILD_DIRECTORY
  "${HARPY_ROOT_DIRECTORY}/build/documentation")

add_custom_target(docHtml
  COMMAND ${SPHINX_BUILD} -M html "${HARPY_SPHINX_SOURCE_DIRECTORY}"
    "${HARPY_SPHINX_BUILD_DIRECTORY}"
  VERBATIM)

add_custom_target(docClean
  COMMAND ${CMAKE_COMMAND} -E remove_directory
    "${HARPY_SPHINX_BUILD_DIRECTORY}"
  VERBATIM)
