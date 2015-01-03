# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLUT import *
import sys

__author__ = 'mayns'

ctrlpoints = [
    [[-1.5, -1.5, 4.0], [-0.5, -1.5, 2.0],
    [0.5, -1.5, -1.0], [1.5, -1.5, 2.0]],
    [[-1.5, -0.5, 1.0], [-0.5, -0.5, 3.0],
     [0.5, -0.5, 0.0], [1.5, -0.5, -1.0]],
    [[-1.5, 0.5, 4.0], [-0.5, 0.5, 0.0],
     [0.5, 0.5, 3.0], [1.5, 0.5, 4.0]],
    [[-1.5, 1.5, -2.0], [-0.5, 1.5, -2.0],
     [0.5, 1.5, 0.0], [1.5, 1.5, -1.0]],
]


def display_1():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glPushMatrix()
    glRotatef(85.0, 1.0, 1.0, 1.0)
    for j in xrange(9):
        glBegin(GL_LINE_STRIP)
        for i in xrange(31):
            glEvalCoord2f(i/30.0, j/8.0)
        glEnd()
        glBegin(GL_LINE_STRIP)
        for i in xrange(31):
            glEvalCoord2f(j/8.0, i/30.0)
        glEnd()
    glPopMatrix()
    glFlush()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(85.0, 1.0, 1.0, 1.0)
    glEvalMesh2(GL_FILL, 0, 20, 0, 20)
    glPopMatrix()
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


def init_lights():
    ambient = [0.2, 0.2, 0.2, 1.0]
    position = [0.0, 0.0, 2.0, 1.0]
    mat_diffuse = [0.6, 0.6, 0.6, 1.0]
    mat_specular = [1.0, 1.0, 1.0, 1.0]
    mat_shininess = [50.0]
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient)
    glLightfv(GL_LIGHT0, GL_POSITION, position)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)


def init_1():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMap2f(GL_MAP2_VERTEX_3, 0, 1, 0, 1, ctrlpoints)
    glEnable(GL_MAP2_VERTEX_3)
    glMapGrid2f(20, 0.0, 1.0, 20, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_FLAT)


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glEnable(GL_DEPTH_TEST)
    glMap2f(GL_MAP2_VERTEX_3, 0, 1, 0, 1, ctrlpoints)
    glEnable(GL_MAP2_VERTEX_3)
    glEnable(GL_AUTO_NORMAL)
    glMapGrid2f(20, 0.0, 1.0, 20, 0.0, 1.0)
    init_lights()


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