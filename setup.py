#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
setup.py

Created by Stephan Hügel on 2016-07-25
"""

import sys
from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy


# # Set dynamic RPATH differently, depending on platform
ldirs = []
ddirs = []
if "linux" in sys.platform:
    # from http://stackoverflow.com/a/10252190/416626
    # the $ORIGIN trick is not perfect, though
    ldirs = ["-Wl,-rpath", "-Wl,$ORIGIN"]
    platform_lib = "liblonlat_bng.so"
if sys.platform == "darwin":
    # You must compile your binary with rpath support for this to work
    # RUSTFLAGS="-C rpath" cargo build --release
    platform_lib = "liblonlat_bng.dylib"
    ldirs = ["-Wl,-rpath", "-Wl,@loader_path/"]
if sys.platform == "win32":
    ddirs = ["convertbng/header.h"]
    platform_lib = "lonlat_bng.dll"


extensions = Extension(
    "convertbng.cutil",
    sources=["convertbng/cutil.pyx"],
    libraries=["lonlat_bng"],
    depends=ddirs,
    language="c",
    include_dirs=["convertbng", numpy.get_include()],
    library_dirs=["convertbng"],
    extra_compile_args=["-O3"],
    extra_link_args=ldirs,
)

extensions = cythonize(
    [
        extensions,
    ],
    compiler_directives={"language_level": "3"},
)


setup(
    package_data={
        "convertbng": [platform_lib],
    },
    ext_modules=extensions,
)
