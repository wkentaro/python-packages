#!/usr/bin/env python
# -*- coding: utf-8 -*-
# setup.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("helloworld.pyx")
)