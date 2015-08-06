#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

__author__ = "www.kentaro.wada@gmail.com <Kentaro Wada>"

from distutils.core import setup
from Cython.Build import cythonize


setup(
    name='Variables app',
    ext_modules=cythonize('variables.pyx'),
)
