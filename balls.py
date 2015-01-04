# -*- coding: utf-8 -*-
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import Image

__author__ = 'mayns'

WHITE = [1, 1, 1]
RED = [1, 0, 0]
GREEN = [0, 1, 0]
DARK_GREEN = [0, 0.5, 0]
MAGENTA = [1, 0, 1]
TEXTURE = 0


class Camera(object):
    def __init__(self, theta=0, y=3, dTheta=0.04, dy=0.2):
        super(Camera, self).__init__()
        self.theta = theta
        self.y = y
        self.dTheta = dTheta
        self.dy = dy

    def get_x(self):
        return 10 * math.cos(self.theta)

    def get_y(self):
        return self.y

    def get_z(self):
        return 10 * math.sin(self.theta)

    def move_right(self):
        self.theta += self.dTheta

    def move_left(self):
        self.theta -= self.dTheta

    def move_up(self):
        self.y += self.dy

    def move_down(self):
        if self.y > self.dy:
            self.y -= self.dy


class Ball(object):
    def __init__(self, r, c, h, x, z, direction=-1):
        super(Ball, self).__init__()
        self.r = r
        self.c = c
        self.max_h = h
        self.x = x
        self.z = z
        self.direction = direction
        self.y = h

    def update(self):
        self.y += self.direction * 0.05
        if self.y > self.max_h:
            self.y = self.max_h
            self.direction = -1
        elif self.y < self.r:
            self.y = self.r
            self.direction = 1
        glPushMatrix()
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, self.c)
        glTranslated(self.x, self.y, self.z)
        glutSolidSphere(self.r, 30, 30)
        glPopMatrix()


class Checkerboard(object):
    def __init__(self, w, d):
        super(Checkerboard, self).__init__()
        self.w = w
        self.d = d
        self.d_list_id = None

    def center_x(self):
        return self.w / 2.0

    def center_z(self):
        return self.d / 2.0

    def create(self):
        self.d_list_id = glGenLists(1)
        glNewList(self.d_list_id, GL_COMPILE)
        light_position = [4, 3, 7, 1]
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
        glBindTexture(GL_TEXTURE_2D, TEXTURE)
        glBegin(GL_QUADS)
        glNormal3d(0, 1, 0)
        for x in xrange(self.w):
            for z in xrange(self.d):
                glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, GREEN if (x + z) % 2 else DARK_GREEN)
                glTexCoord2f(0, 0)
                glVertex3d(x, 0, z)
                glTexCoord2f(1, 0)
                glVertex3d(x + 1, 0, z)
                glTexCoord2f(1, 1)
                glVertex3d(x + 1, 0, z + 1)
                glTexCoord2f(0, 1)
                glVertex3d(x, 0, z + 1)

        glEnd()
        glEndList()

    def draw(self):
        glCallList(self.d_list_id)


board = Checkerboard(8, 8)
cam = Camera()
balls = [Ball(1, GREEN, 7, 6, 1),
         Ball(1.5, MAGENTA, 6, 3, 4),
         Ball(0.4, WHITE, 5, 1, 7),
         Ball(0.15, RED, 10, 2, 3),
         Ball(0.15, RED, 13, 5, 6),
         Ball(0.15, RED, 12, 7, 4),
         ]


def init():
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_DEPTH_TEST)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, WHITE)
    glLightfv(GL_LIGHT0, GL_SPECULAR, WHITE)
    glMaterialfv(GL_FRONT, GL_SPECULAR, WHITE)
    glMaterialf(GL_FRONT, GL_SHININESS, 30)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    board.create()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(cam.get_x(), cam.get_y(), cam.get_z(), board.center_x(), 0.0, board.center_z(), 0.0, 1.0, 0.0)
    board.draw()
    for i in xrange(len(balls)):
        balls[i].update()
    glFlush()
    glutSwapBuffers()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(40.0, float(w) / h, 1.0, 150.0)
    glMatrixMode(GL_MODELVIEW)


def timer(v):
    glutPostRedisplay()
    glutTimerFunc(1000 / 60, timer, v)


def special(key, x, y):
    if key == GLUT_KEY_LEFT:
        cam.move_left()
    if key == GLUT_KEY_RIGHT:
        cam.move_right()
    if key == GLUT_KEY_UP:
        cam.move_up()
    if key == GLUT_KEY_DOWN:
        cam.move_down()
    glutPostRedisplay()


def texture(tex_path):
    image = Image.open(tex_path)
    width = image.size[0]
    height = image.size[1]
    image = image.convert("RGBA").tostring("raw", "RGBA")

    texture = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texture)  # 2d texture (x and y size)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 3, width, height, GL_RGBA, GL_UNSIGNED_BYTE, image)
    return texture


def main():
    global TEXTURE

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowPosition(80, 80)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Bouncing Balls")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutSpecialFunc(special)
    glutTimerFunc(100, timer, 0)
    TEXTURE = texture('textures/grass.bmp')
    init()

    glutMainLoop()


if __name__ == u'__main__':
    main()