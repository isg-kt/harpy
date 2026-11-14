##############################
 Compiling Harpy Using Docker
##############################

This document outlines the procedure for building and running the
**Harpy compiler** inside an isolated container environment, enabling
development and testing across diverse operating systems without native
host toolchain requirements.

.. raw:: html

   <br>
   <hr>
   <br>

**************
 Dependencies
**************

Building through containers requires a compatible OCI-compliant
container engine installed on your host system. The most common options
include `Docker <https://www.docker.com/>`_ and `Docker Desktop
<https://www.docker.com/products/docker-desktop/>`_.

For systems where native Docker is not supported, such as **NetBSD**,
where `Podman <https://podman.io/>`_ is the preferred choice and readily
available via `pkgsrc
<https://cdn.netbsd.org/pub/pkgsrc/current/pkgsrc/sysutils/podman/index.html>`_,
any standard OCI-compliant container runtime can be used
interchangeably.

.. raw:: html

   <br>
   <hr>
   <br>

********************
 Building the Image
********************

To compile the compiler with the default **release configuration**, run
the standard build command without additional arguments:

.. code:: shell

   docker build -t harpy-compiler .

If you require a different build profile, specify your desired mode
using the ``TARGET_MODE`` build argument:

.. code:: shell

   docker build --build-arg TARGET_MODE=<target> -t harpy-compiler:<target> .

When ``TARGET_MODE`` is omitted, the build process automatically
defaults to ``release``. Otherwise, you can select from ``debug``,
``valgrind``, ``sanitizer``, ``test``, ``release``, or ``release-test``.
These options map directly to the configurations detailed in the
:ref:`Build Configurations <build-configurations>` section of the local
compilation guide.

.. raw:: html

   <br>
   <hr>
   <br>

************************
 Running and Extraction
************************

Once the image is built, you can launch an interactive shell inside the
container to test and experiment with the compiler directly:

.. code:: shell

   docker run --rm -it harpy-compiler:<target>

If you need to extract the compiled binary out of the container image
for use on your host system, you can copy it by creating a temporary
container instance:

.. code:: shell

   docker create --name temp-harpy harpy-compiler:<target>
   docker cp temp-harpy:/path/to/harpyc ./harpyc
   docker rm temp-harpy
