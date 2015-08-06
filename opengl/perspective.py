#!/usr/bin/env python
# -*- coding: utf-8 -*-
# perspective.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

from OpenGL.GL import *
from OpenGL.GLU import *

import glut_ui
import glbase
import baseview


class PerspectiveView(baseview.BaseView):
    def __init__(self, distance):
        super(PerspectiveView, self).__init__()
        self.head = 0
        self.pitch = 0
        self.distance = distance
        self.aspect = 1
        self.fovy = 30
        self.n = 1
        self.f = 10000

    def onResize(self, w=None, h=None):
        super(PerspectiveView, self).onResize(w, h)
        self.aspect = float(self.w) / float(self.h)

    def onMotion(self, x, y):
        self.head += (x - self.x)
        self.pitch += (y - self.y)
        self.x = x
        self.y = y
        return True

    def updateProjection(self):
        gluPerspective(self.fovy, self.aspect, self.n, self.f)

    def updateView(self):
        glTranslate(0, 0, -self.distance)
        glRotate(self.head, 0, 1, 0)
        glRotate(self.pitch, 1, 0, 0)


if __name__ == '__main__':
    import cube
    glut_ui.run(
        glbase.BaseController(
            PerspectiveView(80),
            cube.createCube(10)))
