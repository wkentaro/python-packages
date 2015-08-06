#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ortho.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

from OpenGL.GL import *

import glut_ui
import glbase
import baseview


class OrthogonalView(baseview.BaseView):
    def __init__(self, distance):
        super(OrthogonalView, self).__init__()
        self.head = 0
        self.pitch = 0
        self.distance = distance

    def onMotion(self, x, y):
        self.head += (x - self.x)
        self.pitch += (y - self.y)
        self.x = x
        self.y = y
        # return True for redrawing
        return True

    def updateProjection(self):
        l = -self.w / 2
        r = -l
        b = -self.h / 2
        t = -b
        n = 0
        f = 1000
        glOrtho(l, r, b, t, n, f)

    def updateView(self):
        glTranslate(0, 0, -self.distance)
        glRotate(self.head, 0, 1, 0)
        glRotate(self.pitch, 1, 0, 0)


if __name__ == '__main__':
    import cube
    glut_ui.run(
        glbase.BaseController(
            OrthogonalView(200),
            cube.createCube(100)))