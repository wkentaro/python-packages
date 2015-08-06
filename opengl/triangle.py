#!/usr/bin/env python
# -*- coding: utf-8 -*-
# triangle.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

from OpenGL.GL import *


# drawing triangle
class Triangle(object):
    def __init__(self):
        pass

    def draw(self):
        glBegin(GL_TRIANGLES)
        glVertex(-1, -1) # left down
        glVertex(1, -1)  # right down
        glVertex(0, 1)   # up
        glEnd()

