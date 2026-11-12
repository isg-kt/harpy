# File: configuration/documentation/sphinx.cmake
# Brief: Configures Sphinx documentation generation for the Harpy project.
#
# This file is part of the Harpy project and is licensed under the
# 3-Clause BSD License;
# For more information, see LICENSE.txt.
find_program(SPHINX_BUILD NAMES sphinx-build)

if(NOT SPHINX_BUILD)
    message(WARNING
        "[WARNING] Sphinx not found.\n"
        "Documentation targets will not be available.")
    return()
endif()

add_custom_target(docHtml
  COMMAND ${SPHINX_BUILD} -M html "${HARPY_DOCUMENTATION_DIRECTORY}"
    "${HARPY_BUILD_DIRECTORY}"
  VERBATIM)
