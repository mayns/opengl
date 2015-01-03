# -*- coding: utf-8 -*-
from OpenGL.GL   import *
from OpenGL.GLU  import *
from OpenGL.GLUT import *
import Image                    # PIL
import sys
import math

__author__ = 'mayns'

ctrlpoints = [
    [-4.0, -4.0, 0.0], [-2.0, 4.0, 0.0],
    [2.0, -4.0, 0.0], [4.0, 4.0, 0.0]
]


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_STRIP)
    for i in xrange(31):
        glEvalCoord1f(i/30.0)
    glEnd()
    glPointSize(5.0)
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_POINTS)
    for i in xrange(4):
        glVertex3fv(ctrlpoints[i])
    glEnd()
    glFlush()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if w <= h:
        glOrtho(-5.0, 5.0, -5.0 * h / w, 5.0 * h / w, -5.0, 5.0)
    else:
        glOrtho(-5.0 * w / h, 5.0 * w / h, -5.0, 5.0, -5.0, 5.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_FLAT)
    glMap1f(GL_MAP1_VERTEX_3, 0.0, 1.0, ctrlpoints)
    glEnable(GL_MAP1_VERTEX_3)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow('Bezier curve')
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()


main()