#!/usr/bin/env python
# -*- coding: utf-8 -*-
# hello_flat_world.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import sys

import OpenGL.GL as gl
import OpenGL.GLUT as glut

def display():
    glut.glutSwapBuffers()

def reshape(width, height):
    gl.glViewport(0, 0, width, height)

def keyboard(key, x, y):
    if key == '\033':
        sys.exit()


if __name__ == '__main__':
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
    glut.glutCreateWindow('Hello world!')
    glut.glutReshapeWindow(512, 512)
    glut.glutReshapeFunc(reshape)
    glut.glutDisplayFunc(display)
    glut.glutKeyboardFunc(keyboard)
    glut.glutMainLoop()