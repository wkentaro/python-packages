#!/usr/bin/env python
# -*- coding: utf-8 -*-
# draw_triangle.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

from OpenGL.GL import *
from OpenGL.GLUT import *


def draw():
    glClearColor(0.0, 0.5, 0.5, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # drawing triangle
    glBegin(GL_TRIANGLES)
    glVertex(-1, -1) # left down
    glVertex(1, -1)  # right down
    glVertex(0, 1)   # up
    glEnd()

    # OpenGL drawing
    glFlush()
    # glut double buffer exchanging
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