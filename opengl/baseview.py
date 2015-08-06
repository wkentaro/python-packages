#!/usr/bin/python
# coding: utf-8

from OpenGL.GL import *


class BaseView(object):
    def __init__(self):
        self.x=0
        self.y=0
        self.w=1
        self.h=1
        self.isLeftDown=False
        self.isMiddleDown=False
        self.isRightDown=False

    def updateProjection(self):
        pass

    def updateView(self):
        pass

    def onResize(self, w=None, h=None):
        self.w=w or self.w
        self.h=h or self.h
        glViewport(0, 0, self.w, self.h)

    def onLeftDown(self, x, y):
        self.isLeftDown=True
        self.x=x
        self.y=y

    def onLeftUp(self, x, y):
        self.isLeftDown=False

    def onMiddleDown(self, x, y):
        self.isMiddleDown=True
        self.x=x
        self.y=y

    def onMiddleUp(self, x, y):
        self.isMiddleDown=False

    def onRightDown(self, x, y):
        self.isRightDown=True
        self.x=x
        self.y=y

    def onRightUp(self, x, y):
        self.isRightDown=False

    def onMotion(self, x, y):
        print "onMotion", x, y
