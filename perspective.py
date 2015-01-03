# -*- coding: utf-8 -*-

import sys
from OpenGL.GL   import *
from OpenGL.GLU  import *
from OpenGL.GLUT import *
import math
import numpy as np
from jitter import *

__author__ = 'mayns'

ACSIZE = 8


def draw_figure():
    pass


def accFrustum(left, right, bottom, top, near, far, pixdx, pixdy, eyedx, eyedy, focus):
    viewport = np.zeros(4)
    viewport = glGetIntegerv(GL_VIEWPORT, viewport)
    xwsize = right - left
    ywsize = top - bottom
    dx = -(pixdx*xwsize/viewport[2] + eyedx*near/focus)
    dy = -(pixdy*ywsize/viewport[3] + eyedy*near/focus)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(left + dx, right + dx, bottom + dy, top + dy, near, far)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(-eyedx, -eyedy, 0.0)


def accPerspective(fovy, aspect, near, far, pixdx, pixdy, eyedx, eyedy, focus):
    fov2 = ((fovy*math.pi) / 180.0) / 2.0
    top = near / (math.cos(fov2) / math.sin(fov2))
    bottom = -top
    right = top * aspect
    left = -right
    accFrustum(left, right, bottom, top, near, far, pixdx, pixdy, eyedx, eyedy, focus)


def display():
    viewport = np.zeros(4)
    print 'v'
    viewport = glGetIntegerv(GL_VIEWPORT, viewport)
    print viewport
    glClear(GL_ACCUM_BUFFER_BIT)
    for jitter in xrange(ACSIZE):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        accPerspective(50.0, viewport[2] / viewport[3], 1.0, 15.0, j8[jitter][0], j8[jitter][1], 0.0, 0.0, 1.0)
        display_obj()
        glAccum(GL_ACCUM, 1.0 / ACSIZE)
    glAccum(GL_RETURN, 1.0)
    glFlush()


def init():
    mat_ambient = [1.0, 1.0, 1.0, 1.0]
    mat_specular = [1.0, 1.0, 1.0, 1.0]
    light_position = [0.0, 0.0, 10.0, 1.0]
    lm_ambient = [0.2, 0.2, 0.2, 1.0]
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, 50.0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, lm_ambient)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_FLAT)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearAccum(0.0, 0.0, 0.0, 0.0)


def display_obj():
    torus_diffuse = [0.7, 0.7, 0.0, 1.0]
    cube_diffuse = [0.0, 0.7, 0.7, 1.0]
    sphere_diffuse = [0.7, 0.0, 0.7, 1.0]
    octa_diffuse = [0.7, 0.4, 0.4, 1.0]

    glPushMatrix()
    glTranslatef(0.0, 0.0, -5.0)
    glRotatef(30.0, 1.0, 0.0, 0.0)
    glPushMatrix()
    glTranslatef(-0.80, 0.35, 0.0)
    glRotatef(100.0, 1.0, 0.0, 0.0)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, torus_diffuse)
    glutSolidTorus(0.275, 0.85, 16, 16)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(-0.75, -0.50, 0.0)
    glRotatef(45.0, 0.0, 0.0, 1.0)
    glRotatef(45.0, 1.0, 0.0, 0.0)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, cube_diffuse)
    glutSolidCube(1.5)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0.75, 0.60, 0.0)
    glRotatef(30.0, 1.0, 0.0, 0.0)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, sphere_diffuse)
    glutSolidSphere(1.0, 16, 16)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0.70, -0.90, 0.25)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, octa_diffuse)
    glutSolidOctahedron()
    glPopMatrix()
    glPopMatrix()


def textures():
    pass


def animate():
    pass


def reshape(w, h):
    glViewport(0, 0, w, h)


def keyboard():
    pass


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_ACCUM | GLUT_DEPTH)
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