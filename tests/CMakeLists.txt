# File: tests/CMakeLists.txt
# Brief: Configures the testRunner executable target.
#
# This file is part of the Harpy project and is licensed under the
# 3-Clause BSD License;
# For more information, see LICENSE.txt.
add_executable(testRunner main.cpp)

target_link_libraries(testRunner PRIVATE
  global_configuration)
