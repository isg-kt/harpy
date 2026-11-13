# File: Dockerfile
# Brief: Containerized build environment for the Harpy project.
#
# This file is part of the Harpy project and is licensed under the
# 3-Clause BSD License;
# For more information, see LICENSE.txt.
FROM alpine:latest

ARG TARGET_MODE=release

RUN apk update && apk add --no-cache                                     \
  build-base                                                             \
  clang                                                                  \
  lld                                                                    \
  compiler-rt                                                            \
  ninja                                                                  \
  cmake                                                                  \
  valgrind                                                               \
  valgrind-dev                                                           \
  pkgconf

WORKDIR /compiler
COPY . /compiler/

RUN cmake --preset linux-amd64-${TARGET_MODE}
RUN cmake --build --preset linux-amd64-${TARGET_MODE}
