#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cube.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

from OpenGL.GL import *

import glut_ui
import glbase
import vertexarray


def createCube(size):
    return vertexarray.IndexedVertexArrayWithColor(
            vertices=[
                -size, -size, -size, # v0
                size, -size, -size, # v1
                size,  size, -size, # v2
                -size,  size, -size, # v3
                -size, -size,  size, # v4
                size, -size,  size, # v5
                size,  size,  size, # v6
                -size,  size,  size, # v7
                ],
            colors=[
                1, 0, 0, # v0の色
                0, 1, 0, # v1の色
                0, 0, 1, # v2の色
                1, 1, 1, # v3の色
                0, 1, 1, # v4の色
                1, 0, 1, # v5の色
                1, 1, 0, # v6の色
                0, 0, 0, # v7の色
                ],
            indices=[
                4, 5, 6, # triangle0の頂点index
                6, 7, 4, # triangle1の頂点index
                5, 1, 2, # triangle2の頂点index
                2, 6, 5, # triangle3の頂点index
                1, 0, 3, # triangle4の頂点index
                3, 2, 1, # triangle5の頂点index
                0, 4, 7, # triangle6の頂点index
                7, 3, 0, # triangle7の頂点index
                3, 7, 6, # triangle8の頂点index
                6, 2, 3, # triangle9の頂点index
                0, 1, 5, # triangle10の頂点index
                5, 4, 0, # triangle11の頂点index
            ])


if __name__=="__main__":
    import rotation
    glut_ui.run(glbase.BaseController(rotation.Rotation(), createCube(0.4)))