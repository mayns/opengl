# -*- coding: utf-8 -*-

import sys
from OpenGL.GL   import *
from OpenGL.GLU  import *
from OpenGL.GLUT import *

__author__ = 'mayns'

spin = 0


def draw_figure():
    pass


def display():
    position = [0.0, 0.0, 1.5, 1.0]
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(0.0, 0.0, -5.0)
    glPushMatrix()
    glRotated(spin, 1.0, 0.0, 0.0)
    glLightfv(GL_LIGHT0, GL_POSITION, position)
    glTranslated(0.0, 0.0, 1.5)
    glDisable(GL_LIGHTING)
    glColor3f(0.0, 1.0, 1.0)
    glutWireCube(0.1)
    glEnable(GL_LIGHTING)
    glPopMatrix()
    glutSolidTorus(0.275, 0.85, 8, 15)
    glPopMatrix()
    glFlush()


def init():
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_SMOOTH)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)


def lights():
    pass


def textures():
    pass


def animate():
    pass


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(40.0, w / h, 1.0, 20.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def keyboard():
    pass


def mouse(btn, state, x, y):
    global spin
    if btn == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        spin = (spin + 30) % 360
        glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(u"Oks' Project")

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutIdleFunc(animate)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse)

    init()
    glutMainLoop()


if __name__ == u'__main__':
    main()