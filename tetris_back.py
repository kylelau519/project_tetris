import pygame as pg
import numpy as np
import copy

class background(object):
    def __init__(self,grid = np.zeros((18,10),dtype = np.bool)):
        self._grid = grid

    def check_blocked(self,pos_y,pos_x,direction,block):
        if direction == 'Left' or 'Right' or 'Down':
            for i in range(len(block.shape)):
                for j in range(len(block.shape[i])):
                    if block.shape[i][j]:
                        if direction == 'Left' and self._grid[pos_y+i][pos_x+j-1]:
                            return True
                        if direction == 'Right' and self._grid[pos_y+i][pos_x+j+1]:
                            return True
                        if direction == 'Down' and self._grid[pos_y+i+1][pos_x+j]:
                            return True
        if direction == 'Rotation':
            rot = copy.copy(block)
            rot.rotate()
            for i in range(len(rot.shape)):
                for j in range(len(rot.shape[i])):
                    if self._grid[rot.pos_y+i][rot.pos_x+j]:
                        return True

        return False

    @property
    def grid(self):
        return self._grid


    def set_pos_blocked(self,pos_y,pos_x,blockshape):
        for i in range(len(blockshape)):
            for j in range(len(blockshape[i])):
                if blockshape[i][j]:
                    self._grid[pos_y+i][pos_x+j] = True

    def explode(self,row):
        self._grid[1:row+1] = self._grid[0:row]
        self._grid[0] = np.zeros(10,dtype = np.bool)
        print self._grid

    def check_explode(self,block):
        print len(block.shape)
        for row in range(0,len(block.shape)):
            if np.all(self._grid[block.pos_y + row]):
                self.explode(block.pos_y+row)
                print 'explode'
