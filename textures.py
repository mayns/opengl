# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLUT import *
import math, sys

__author__ = 'mayns'

imageWidth = 64
imageHeight = 64
image = []

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

texpts = [
    [[0.0, 0.0], [0.0, 1.0]],
    [[1.0, 0.0], [1.0, 1.0]]
]


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glEvalMesh2(GL_FILL, 0, 20, 0, 20)
    glFlush()


def make_image():
    for i in xrange(imageWidth):
        ti = 2.0 * 3.14159265 * i / imageWidth
        for j in xrange(imageHeight):
            tj = 2.0 * 3.14159265 * j / imageHeight
            image.append(int(127 * (1.0 + math.sin(ti))))
            image.append(int(127 * (1.0 + math.cos(2*tj))))
            image.append(int(127 * (1.0 + math.cos(ti+tj))))


def init():
    glMap2f(GL_MAP2_VERTEX_3, 0, 1, 0, 1, ctrlpoints)
    glMap2f(GL_MAP2_TEXTURE_COORD_2, 0, 1, 0, 1, texpts)
    glEnable(GL_MAP2_TEXTURE_COORD_2)
    glEnable(GL_MAP2_VERTEX_3)
    glMapGrid2f(20, 0.0, 1.0, 20, 0.0, 1.0)
    make_image()
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    try:
        glTexImage2D(GL_TEXTURE_2D, 0, 3, imageWidth, imageHeight, 0, GL_RGB, GL_UNSIGNED_BYTE, image)
    except Exception, ex:
        print ex
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_FLAT)


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if w <= h:
        glOrtho(-4.0, 4.0, -4.0 * h / w, 4.0 * h / w, -4.0, 4.0)
    else:
        glOrtho(-4.0 * w / h, 4.0 * w / h, -4.0, 4.0, -4.0, 4.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glRotatef(85.0, 1.0, 1.0, 1.0)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100);
    glutCreateWindow('Textures')
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

main()