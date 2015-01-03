# -*- coding: utf-8 -*-

import sys
from OpenGL.GL   import *
from OpenGL.GLU  import *
from OpenGL.GLUT import *

__author__ = 'mayns'


def draw_figure():
    pass


def display():
    pass


def init():
    pass


def lights():
    pass


def textures():
    pass


def animate():
    pass


def reshape(w, h):
    pass


def keyboard():
    pass


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(u"Oks' Project")

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutIdleFunc(animate)
    glutKeyboardFunc(keyboard)

    init()
    glutMainLoop()


if __name__ == u'__main__':
    main()