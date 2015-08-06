#!/usr/bin/env python
# -*- coding: utf-8 -*-
# translation.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

from OpenGL.GL import *

import glut_ui
import glbase
import baseview
import triangle


class Translation(baseview.BaseView):
    def __init__(self):
        super(Translation, self).__init__()
        self.pos_x=0
        self.pos_y=0

    def onMotion(self, x, y):
        # マウスカーソルの座標を左右-1〜+1、上下-1〜+1の範囲に変換する
        self.pos_x=float(x)/self.w*2-1
        self.pos_y=-(float(y)/self.h*2-1)
        # 再描画したいのでTrueを返す
        return True

    def updateView(self):
        print("==> Identity")
        print(glGetFloatv(GL_MODELVIEW_MATRIX))

        glTranslate(self.pos_x, self.pos_y, 0)

        print("==> GL_MODELVIEW_MATRIX {0} {1}".format(self.pos_x, self.pos_y))
        print(glGetFloatv(GL_MODELVIEW_MATRIX))


if __name__=="__main__":
    glut_ui.run(glbase.BaseController(
        Translation(),
        triangle.Triangle()))
