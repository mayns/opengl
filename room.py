# -*- coding: utf-8 -*-

import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

__author__ = 'mayns'

rotate_y = 0
rotate_x = 0

spin = 0


def draw_scene():
    # White side - BACK
    glBegin(GL_POLYGON)
    glNormal3f(0.0, 0.0, 1.0)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glEnd()

    # Purple side - RIGHT
    glBegin(GL_POLYGON)
    glNormal3f(-1.0, 0.0, 0.0)
    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glEnd()

    # Green side - LEFT
    glBegin(GL_POLYGON)
    glNormal3f(1.0, 0.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glEnd()

    # Blue side - TOP
    glBegin(GL_POLYGON)
    glNormal3f(0.0, -1.0, 0.0)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glEnd()

    # Red side - BOTTOM
    glBegin(GL_POLYGON)
    glNormal3f(0.0, 1.0, 0.0)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glEnd()


def display():
    # Clear screen and Z-buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    glTranslatef(0, 0, -1)

    # Rotate when user changes rotate_x and rotate_y
    # glRotatef(rotate_x, 1.0, 0.0, 0.0)
    # glRotatef(rotate_y, 0.0, 1.0, 0.0)
    draw_scene()
    # glutSolidCube(0.5)
    glFlush()


def init():
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
    mat_specular = [.8, 0.0, 0.0, 1.0]
    mat_shininess = [30.0]
    # light_position = [-1.0, 1.0, 1.0, 0.0]
    glClearColor(0.0, 0.0, 0.0, 0.0)
    light_position = [10, 10, 10, 1.0]
    glShadeModel(GL_SMOOTH)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    # glMaterialfv(GL_FRONT, GL_AMBIENT, mat_specular)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_specular)
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
    glFrustum(-1.0, 1.0, -1.0, 1.0, 1.0, .5)
    # if w <= h:
    #     glOrtho(-1.5, 1.5, -1.5*h/w, 1.5*h/w, -10.0, 10.0)
    # else:
    #     glOrtho(-1.5*w/h, 1.5*w/h, -1.5, 1.5, -10.0, 10.0)
    glMatrixMode(GL_MODELVIEW)
    # glLoadIdentity()


def keyboard(key, x, y):

    global rotate_x, rotate_y

    #  Right arrow - increase rotation by 5 degree
    if key == GLUT_KEY_RIGHT:
        rotate_y += 5

        # Left arrow - decrease rotation by 5 degree
    elif key == GLUT_KEY_LEFT:
        rotate_y -= 5

    elif key == GLUT_KEY_UP:
        rotate_x += 5

    elif key == GLUT_KEY_DOWN:
        rotate_x -= 5

    # Request display update
    glutPostRedisplay()


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
    glutCreateWindow(u"=(")

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    # glutIdleFunc(animate)
    glutSpecialFunc(keyboard)
    glutMouseFunc(mouse)

    init()
    glutMainLoop()


if __name__ == u'__main__':
    main()