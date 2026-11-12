# File: configuration/documentation/doxygen.cmake
# Brief: Configures Doxygen XML generation.
#
# This file is part of the Harpy project and is licensed under the
# 3-Clause BSD License;
# For more information, see LICENSE.txt.
find_package(Doxygen)

if(NOT Doxygen_FOUND)
    message(WARNING
        "[WARNING] Doxygen not found.\n"
        "Documentation targets will not be available.")
    return()
endif()

set(HARPY_DOXYFILE_SCRIPT "${CMAKE_CURRENT_LIST_DIR}/doxyfile.py")

add_custom_target(docXml
  COMMAND ${Python3_EXECUTABLE} "${HARPY_DOXYFILE_SCRIPT}"
    --root "${HARPY_ROOT_DIRECTORY}"
    --build "${HARPY_BUILD_DIRECTORY}"
  COMMAND ${DOXYGEN_EXECUTABLE} "${HARPY_BUILD_DIRECTORY}/Doxyfile"
  WORKING_DIRECTORY "${HARPY_ROOT_DIRECTORY}"
  VERBATIM)
