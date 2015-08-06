#!/usr/bin/env python
# -*- coding: utf-8 -*-
# rotation.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

from OpenGL.GL import *

import glut_ui
import glbase
import baseview


class Rotation(baseview.BaseView):
    def __init__(self):
        super(Rotation, self).__init__()
        self.head_x = 0
        self.head_y = 0

    def onMotion(self, x, y):
        # 回転角度
        self.head_x += (x - self.x)
        self.head_y += (y - self.y)
        self.x = x
        self.y = y
        # 再描画したいのでTrueを返す
        return True

    def updateView(self):
        glRotate(self.head_x, 0, 1, 0)
        glRotate(self.head_y, 1, 0, 0)
        print("==> GL_MODELVIEW_MATRIX {0} {1}".format(self.head_x, self.head_y))
        print(glGetFloatv(GL_MODELVIEW_MATRIX))


if __name__=="__main__":
    import triangle
    glut_ui.run(glbase.BaseController(Rotation(), triangle.Triangle()))