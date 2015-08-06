#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

This example draws 9 rectangles in different
brush styles.

author: Jan Bodnar
website: zetcode.com 
last edited: September 2011
"""

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 355, 280)
        self.setWindowTitle('Brushes')
        self.show()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()

    def drawBrushes(self, qp):

        brush = QtGui.QBrush(QtCore.Qt.SolidPattern)

        brush.setStyle(QtCore.Qt.NoBrush)
        qp.setBrush(brush)

        points = [QtCore.QPoint(10, 10),
                  QtCore.QPoint(10, 80),
                  QtCore.QPoint(90, 80),
                  QtCore.QPoint(80, 0),]
        needle = QtGui.QPolygon(points)
        qp.drawPolygon(needle)


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
