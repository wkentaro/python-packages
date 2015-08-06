#!/usr/bin/env python
# -*- coding: utf-8 -*-
# create_window.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import sys

from OpenGL.GL import *
from OpenGL.GLUT import *


def draw():
    # Clear OpenGL's buffer
    glClearColor(.0, .5, .5, .0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # Execute OpenGL drawing
    glFlush()
    # glut buffer exchange
    glutSwapBuffers()


def setup():
    glutInit(sys.argv)
    # initializing
    # RGBA mode, Double buffering is valid, Z buffer is valid
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutCreateWindow("glut sample")
    # register function which is called when drawing
    glutDisplayFunc(draw)


if __name__ == '__main__':
    setup()
    glutMainLoop()