import numpy as np
import pygame as pg
class block(object):
    def __init__(self,type,shape,x,y):
        self._shape = shape
        self._type = type
        self._x = x
        self._y = y

    def rotate(self):
        self._shape = np.rot90(self._shape)
        if self._x + len(self._shape[0]) > 10:
            self._x = 10-len(self._shape[0])
        if self._y + len(self._shape) > 15:
            self._y = 15 - len(self._shape)

    def get_type(self):
        return self._type

    def __str__(self):
        return '{0}'.format(self._shape)

    def draw(self,screen):
        for i in range(len(self._shape)):
            for j in range(len(self._shape[i])):
                if self._shape[i][j]:
                    pg.draw.rect(screen, (0, 0, 0), (25+40*self._x+40*j,25+40*self._y+40*i,40,40))
    @property
    def pos_x(self):
        return self._x
    @pos_x.setter
    def pos_x(self,new):
        self._x = new


    @property
    def pos_y(self):
        return self._y
    @pos_y.setter
    def pos_y(self,new):
        self._y = new

    @property
    def shape(self):
        return self._shape
