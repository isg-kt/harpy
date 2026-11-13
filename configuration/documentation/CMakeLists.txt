# File: configuration/documentation/CMakeLists.txt
# Brief: Orchestrates project documentation generation subsystems.
#
# This file is part of the Harpy project and is licensed under the
# 3-Clause BSD License;
# For more information, see LICENSE.txt.
set(HARPY_DOCUMENTATION_DIRECTORY "${HARPY_ROOT_DIRECTORY}/documentation")

include(sphinx.cmake)
include(doxygen.cmake)

if (Python3_FOUND AND Doxygen_FOUND AND SPHINX_BUILD)
  add_custom_target(docGen
    DEPENDS docXml docHtml)

  add_custom_target(docClean
    COMMAND ${CMAKE_COMMAND} -E remove_directory
      "${HARPY_BUILD_DIRECTORY}/documentation"
    VERBATIM)
endif()
