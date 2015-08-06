#!/usr/bin/env python
# -*- coding: utf-8 -*-
# checker_board.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut

import random

def init_fun():
    gl.glClearColor(1., 1., 1., 0.)
    gl.glColor3f(0., 0., 0.)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluOrtho2D(0., 640., 0., 480.)

def display_fun():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    for i in range(0, 259):
            gray = idx = random.randint(0, 25) / 25.