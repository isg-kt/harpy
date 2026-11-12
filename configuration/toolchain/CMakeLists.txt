# File: configuration/toolchain/CMakeLists.txt
# Brief: Configures Clang compilers and the LLD linker toolchain.
#
# This file is part of the Harpy project and is licensed under the
# 3-Clause BSD License;
# For more information, see LICENSE.txt.
set(CMAKE_C_COMPILER clang CACHE STRING "" FORCE)
set(CMAKE_CXX_COMPILER clang++ CACHE STRING "" FORCE)
set(CMAKE_EXE_LINKER_FLAGS
  "${CMAKE_EXE_LINKER_FLAGS} -fuse-ld=lld"
  CACHE STRING "" FORCE)
set(CMAKE_SHARED_LINKER_FLAGS
  "${CMAKE_SHARED_LINKER_FLAGS} -fuse-ld=lld"
  CACHE STRING "" FORCE)
set(CMAKE_MODULE_LINKER_FLAGS
  "${CMAKE_MODULE_LINKER_FLAGS} -fuse-ld=lld"
  CACHE STRING "" FORCE)
