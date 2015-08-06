#-*- coding: utf-8 -*-
# mouse-event.py
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        widget = QtGui.QWidget(self)
        layout = QtGui.QVBoxLayout(widget)
        self.edit = QtGui.QLineEdit(self)
        self.list = QtGui.QWidget(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.list)
        self.setCentralWidget(widget)

        self.pos = [None, None]

    def paintEvent(self, e):
        qp = QtGui.QPainter(self)
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)
        # draw rectangle
        pos1, pos2 = self.pos
        if pos1 is not None and pos2 is not None:
            if pos1.y() > pos2.y():
                print 'drawing'
                qp.drawRect(pos1.x(), pos1.y(),
                        pos2.x() - pos1.x(), pos2.y() - pos1.y())
            else:
                qp.drawRect(pos2.x(), pos2.y(),
                        pos1.x() - pos2.x(), pos1.y() - pos2.y())

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseMove:
            if event.buttons() == QtCore.Qt.NoButton:
                self.pos[1] = event.pos()
                self.edit.setText('x: %d, y: %d' %
                        (event.pos().x(), event.pos().y()))
            else:
                pass # do other stuff
        elif event.type() == QtCore.QEvent.MouseButtonPress:
            print "pressed"
            self.pos[0] = event.pos()
        return QtGui.QMainWindow.eventFilter(self, source, event)

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    win = Window()
    win.show()
    app.installEventFilter(win)
    sys.exit(app.exec_())
