# -*- coding: utf-8 -*-

from OpenGL.GL   import *
from OpenGL.GLU  import *
from OpenGL.GLUT import *
import numpy as np

__author__ = 'mayns'


def draw_figure(x1, y1, x2, y2, x3, y3, z):
    glBegin(GL_TRIANGLES)
    glVertex3f(x1, y1, z)
    glVertex3f(x2, y2, z)
    glVertex3f(x3, y3, z)
    glEnd()


def draw_view(x1, x2, y1, y2, z1, z2):
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    glVertex3f(x1, y1, -z1)
    glVertex3f(x2, y1, -z1)
    glVertex3f(x2, y2, -z1)
    glVertex3f(x1, y2, -z1)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex3f(x1, y1, -z2)
    glVertex3f(x2, y1, -z2)
    glVertex3f(x2, y2, -z2)
    glVertex3f(x1, y2, -z2)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(x1, y1, -z1)
    glVertex3f(x1, y1, -z2)
    glVertex3f(x1, y2, -z1)
    glVertex3f(x1, y2, -z2)
    glVertex3f(x2, y1, -z1)
    glVertex3f(x2, y1, -z2)
    glVertex3f(x2, y2, -z1)
    glVertex3f(x2, y2, -z2)
    glEnd()


def draw_scene():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(30.0, 4.0/3.0, 1.0, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(7.5, 7.5, 12.5, 2.5, 2.5, -5.0, 0.0, 1.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    draw_figure(2.0, 2.0, 3.0, 2.0, 2.5, 3.0, -5.0)
    glColor3f(1.0, 0.0, 0.0)
    draw_figure(2.0, 7.0, 3.0, 7.0, 2.5, 8.0, -5.0)
    glColor3f(1.0, 1.0, 0.0)
    draw_figure(2.0, 2.0, 3.0, 2.0, 2.5, 3.0, 0.0)
    draw_figure(2.0, 2.0, 3.0, 2.0, 2.5, 3.0, -10.0)
    draw_view(0.0, 5.0, 0.0, 5.0, 0.0, 10.0)


def process_hits(hits, buf):
    for i in xrange(len(hits)):
        print " number of names for hit = %d\n" % i
        print " z1 is %g;" % (i / 0x7fffffff)
        print " z2 is %g\n" % (i / 0x7fffffff)
        print " the name is "
        for j in xrange(buf[i]):
            print"%d\n" % j


def select_obj():
    select_buf = glSelectBuffer(512)
    glRenderMode(GL_SELECT)
    glInitNames()
    glPushName(0)
    glPushMatrix()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 5.0, 0.0, 5.0, 0.0, 10.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    select_buf = np.append(select_buf, glLoadName(1))
    draw_figure(2.0, 2.0, 3.0, 2.0, 2.5, 3.0, -5.0)
    select_buf = np.append(select_buf, glLoadName(2))
    draw_figure(2.0, 7.0, 3.0, 7.0, 2.5, 8.0, -5.0)
    select_buf = np.append(select_buf, glLoadName(3))
    draw_figure(2.0, 2.0, 3.0, 2.0, 2.5, 3.0, 0.0)
    draw_figure(2.0, 2.0, 3.0, 2.0, 2.5, 3.0, -10.0)
    glPopMatrix()
    glFlush()
    hits = glRenderMode(GL_RENDER)
    process_hits(hits, select_buf)


def display():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_scene()
    select_obj()
    glFlush()


def init():
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_FLAT)


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
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
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