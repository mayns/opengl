# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

__author__ = 'mayns'


def room():

    # glBegin(GL_POLYGON)

    # Floor
    # glColor3f(0, 0, 0)
    # glVertex3f(.5528, 0.0, 0.0)
    # glVertex3f(0.0, 0.0, 0.0)
    # glVertex3f(0.0, 0.0, .5592)
    # glVertex3f(.5496, 0.0, .5592)
    # glEnd()

    # Light
    # glBegin(GL_POLYGON)
    # glColor3f(1, 0, 0)
    # glVertex3f(343.0, 548.8, 227.0)
    # glVertex3f(343.0, 548.8, 332.0)
    # glVertex3f(213.0, 548.8, 332.0)
    # glVertex3f(213.0, 548.8, 227.0)
    # glEnd()

    # Ceiling
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    glVertex3f(0.556, 0.5488, 0.0)
    glVertex3f(.5560, 0.5488, 0.5592)
    glVertex3f(0.0, .5488, 0.5592)
    glVertex3f(0.0, .5488, 0.0)
    glEnd()

    # Back wall
    # glBegin(GL_POLYGON)
    # glColor3f(0, 0, 0)
    # glVertex3f(.5496, 0.0, .5592)
    # glVertex3f(0.0, 0.0, .5592)
    # glVertex3f(0.0, .5488, .5592)
    # glVertex3f(.5560, .5488, .5592)
    # glEnd()

    # Right wall
    # glBegin(GL_POLYGON)
    # glColor3f(0, 1, 0)
    # glVertex3f(0.0, 0.0, .5592)
    # glVertex3f(0.0, 0.0, 0.0)
    # glVertex3f(0.0, .5488, 0.0)
    # glVertex3f(0.0, .5488, .5592)
    # glEnd()

    # Left wall
    # glBegin(GL_POLYGON)
    # glColor3f(1, 0, 0)
    # glVertex3f(.5528, 0.0, 0.0)
    # glVertex3f(.5496, 0.0, .5592)
    # glVertex3f(.5560, .5488, .5592)
    # glVertex3f(.5560, .5488, 0.0)
    #
    # glEnd()
    # glFinish()


def display():
    # glClear(GL_COLOR_BUFFER_BIT)
    # glColor3f(1.0, 1.0, 1.0)
    # glMatrixMode(GL_MODELVIEW)
    # glLoadIdentity()
    # glTranslatef(1.0, 1.5, -7.0)
    # gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    # glScalef(1.0, 1.0, 1.0)
    # glutWireCube(1.0)
    # room()
    # glFlush()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)

    # Render a color-cube consisting of 6 quads with different colors
    glLoadIdentity()
    # glTranslatef(-1.0, 1.5, 2.0)     # Move right and into the screen

    glBegin(GL_QUADS)                # Begin drawing the color cube with 6 quads
    # Top face (y = 1.0f)
    # Define vertices in counter-clockwise (CCW) order with normal pointing out
    glColor3f(0.0, 1.0, 0.0)         # Green
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0,  1.0)
    glVertex3f(1.0, 1.0,  1.0)

    # Bottom face (y = -1.0f)
    glColor3f(1.0, 0.5, 0.0)     # Orange
    glVertex3f(1.0, -1.0,  1.0)
    glVertex3f(-1.0, -1.0,  1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)

    # Front face  (z = 1.0f)
    glColor3f(1.0, 0.0, 0.0)     # Red
    glVertex3f(1.0,  1.0, 1.0)
    glVertex3f(-1.0,  1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    # Back face (z = -1.0f)
    glColor3f(1.0, 1.0, 0.0)     # Yellow
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glVertex3f(1.0,  1.0, -1.0)

    # Left face (x = -1.0f)
    glColor3f(0.0, 0.0, 1.0)     # Blue
    glVertex3f(-1.0,  1.0,  1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0,  1.0)

    # Right face (x = 1.0f)
    glColor3f(1.0, 0.0, 1.0)     # Magenta
    glVertex3f(1.0,  1.0, -1.0)
    glVertex3f(1.0,  1.0,  1.0)
    glVertex3f(1.0, -1.0,  1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glEnd()  # End of drawing color-cube
    glFlush()
    glFinish()
    glutSwapBuffers()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)
    glMatrixMode(GL_MODELVIEW)


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glShadeModel(GL_SMOOTH)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow('Cornell Box')
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()


if __name__ == u'__main__':
    main()