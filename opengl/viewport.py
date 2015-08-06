#!/usr/bin/env python
# -*- coding: utf-8 -*-
# viewport.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

from OpenGL.GL import *
from OpenGL.GLUT import *


def resize(w, h):
    print("resize", w, h)
    # Windowの左から100, 下から100, 幅w/2, 高さh/2をビューポートにする
    glViewport(50, 150, w/2, h/2)

def draw():
    # OpenGLバッファのクリア
    glClearColor(0.0, 0.5, 0.5, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # 三角形描画開始
    glBegin(GL_TRIANGLES)
    # 左下
    glVertex(-1, -1)
    # 右下
    glVertex(1, -1)
    # 上
    glVertex(0, 1)
    # 三角形描画終了
    glEnd()

    # 枠
    glBegin(GL_LINES)
    glVertex(-1, -1); glVertex(1, -1)
    glVertex(1, -1); glVertex(1, 1)
    glVertex(1, 1); glVertex(-1, 1)
    glVertex(-1, 1); glVertex(-1, -1)
    glEnd()

    # OpenGL描画実行
    glFlush()
    # glutダブルバッファ交換
    glutSwapBuffers()


def setup():
    glutInit(sys.argv)
    # RGBAモード、ダブルバッファリング有効、Zバッファ有効で初期化
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutCreateWindow("glut sample")
    # Windowのサイズが変わった時に呼ばれる関数を登録
    glutReshapeFunc(resize)
    # 描画時に呼ばれる関数を登録
    glutDisplayFunc(draw)


if __name__=="__main__":
    setup()
    glutMainLoop()