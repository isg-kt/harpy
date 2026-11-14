#################
 Compiling Harpy
#################

.. toctree::
   :maxdepth: 1
   :caption: Contents:
   :hidden:

   compiling_locally
   compiling_using_docker

Building the Harpy compiler can be done either **natively** on your host
system or inside an **isolated container environment**, depending on
your operating system and development setup.

**Local compilation** is designed for Linux environments on AMD64
architectures, providing full toolchain integration for general source
development and native workflows.

**Containerized compilation** through ``Docker``, ``Docker Desktop``, or
``Podman`` allows you to build and run the compiler across different
operating systems—including **Windows**, **macOS**, and **BSD
variants**, without requiring a native local toolchain or dealing with
architecture limitations. This approach is ideal for testing the
compiler or experimenting with the language codebases on host platforms
where *native builds are not supported*.
