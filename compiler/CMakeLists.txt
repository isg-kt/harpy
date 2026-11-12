# File: compiler/CMakeLists.txt
# Brief: Configures the harpyc compiler executable target.
#
# This file is part of the Harpy project and is licensed under the
# 3-Clause BSD License;
# For more information, see LICENSE.txt.
add_executable(harpyc main.cpp)

target_link_libraries(harpyc PRIVATE
  global_configuration)
