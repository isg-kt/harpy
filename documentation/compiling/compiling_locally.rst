#########################
 Compiling Harpy Locally
#########################

This document outlines the procedure for building the **Harpy compiler**
from source, covering required toolchain dependencies, build
configurations, and compilation steps for *supported host environments*.

.. raw:: html

   <br>
   <hr>
   <br>

**************
 Dependencies
**************

Building locally requires the following toolchain components installed
on your host system:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   -  -  Dependency
      -  Minimum Required Version
   -  -  `CMake <https://cmake.org/>`_
      -  >= 3.31
   -  -  `Clang <https://clang.llvm.org/>`_
      -  >= 17
   -  -  `LLD <https://lld.llvm.org/>`_
      -  >= 17
   -  -  `Ninja <https://ninja-build.org/>`_
      -  >= 1.12

.. note::

   If you're compiling with the valgrind target, you'll also need the
   `Valgrind <https://valgrind.org/>`_ >= 3.24 dependency.

.. note::

   If your distribution uses a ``musl`` libc and you plan to build with
   sanitizer targets, you will also need the `compiler-rt
   <https://compiler-rt.llvm.org/>`_ runtime library installed.

.. raw:: html

   <br>
   <hr>
   <br>

**********************
 Build Configurations
**********************

If your objective is simply to *use the compiler*, you can proceed
directly with the release preset. For **development and contributions**,
understanding the alternative build configurations is essential.

.. list-table::
   :header-rows: 1
   :widths: 45 55

   -  -  Target Preset
      -  Intended Purpose
   -  -  ``linux-amd64-release``
      -  Production and general usage
   -  -  ``linux-amd64-debug``
      -  Local debugging and strict static diagnostics
   -  -  ``linux-amd64-sanitizer``
      -  Runtime memory and undefined behavior detection
   -  -  ``linux-amd64-valgrind``
      -  External profiling and memory leak analysis
   -  -  ``linux-amd64-test``
      -  Unoptimized test suite execution
   -  -  ``linux-amd64-release-test``
      -  Optimized test suite execution

The **release configuration** serves as the default production mode,
applying aggressive optimizations like *link-time optimization* and
*dead code elimination* to maximize execution performance.

The **debug configuration** turns off optimizations and enables
extensive diagnostic warnings, *stack protection mechanisms*, and debug
definitions to assist with local troubleshooting. For advanced memory
analysis, the **sanitizer configuration** instruments the binary with
address and undefined behavior sanitizers, while the **valgrind
configuration** integrates specific debugging headers and symbols for
external analysis tools.

Finally, the **test** and **release-test** configurations enforce strict
*error-on-warning* policies and activate internal test hooks, operating
under unoptimized or fully optimized compilation profiles respectively.

.. raw:: html

   <br>
   <hr>
   <br>

***********************
 Building the Compiler
***********************

After identifying your target preset identifier, execute ``CMake`` to
configure and trigger the build step:

.. code:: shell

   cmake --preset <triple> && cmake --build --preset <triple>

Upon completion, the generated compiler binary is located at:

.. code:: shell

   ls build/<triple>/compiler/harpyc
