#-*- coding: utf-8 -*-
# hello_world.py
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


def main():
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA)
    glut.glutCreateWindow('Hello world!')
    glut.glutReshapeWindow(512, 512)
    glut.glutReshapeFunc(reshape)
    glut.glutDisplayFunc(display)
    glut.glutKeyboardFunc(keyboard)
    glut.glutMainLoop()


if __name__ == '__main__':
    main()
