import pygame as pg
import numpy as np
import random
import time
pg.init()

back_grid = np.zeros((20,10),dtype = np.bool)
print(back_grid)

screen = pg.display.set_mode((500,670))
pg.display.set_caption('tetris')
clock = pg.time.Clock()

###the grid######the boundary###
def draw():
    for v_line in range(1, 10):
        pg.draw.line(screen, (153, 204, 255), [25 + 40 * v_line, 25], [25 + 40 * v_line, 625], 1)  # rgb(153,204,255)
    for h_line in range(1, 15):
        pg.draw.line(screen, (153, 204, 255), [25, 25 + 40 * h_line], [425, 25 + 40 * h_line], 1)  # rgb(153,204,255)

    pg.draw.line(screen, (0, 0, 0), [25, 25], [25, 625], 3)  # rgb(0,0,0)
    pg.draw.line(screen, (0, 0, 0), [25, 25], [425, 25], 3)  # rgb(0,0,0)
    pg.draw.line(screen, (0, 0, 0), [425, 25], [425, 625], 3)  # rgb(0,0,0)
    pg.draw.line(screen, (0, 0, 0), [425, 625], [25, 625], 3)  # rgb(0,0,0)

##blocks###
bl_T = np.array([[True,True,True],[False,True,False]])
bl_L = np.array([[True,False],[True,False],[True,True]])
bl_J = np.array([[False,True],[False,True],[True,True]])
bl_I = np.array([[True,True,True,True],[False,False,False,False]])
bl_S = np.array([[False,True,True],[True,True,False]])
bl_Z = np.array([[True,True,False],[False,True,True]])
bl_O = np.array([[True,True],[True,True]])


##test#######
class block(object):
    def __init__(self,type,shape,x,y):
        self._shape = shape
        self._type = type
        self.x = x
        self.y = y
    def rotate(self):
        b = np.zeros((self._shape.shape[1],self._shape.shape[0]))
        for h_dim in range(0,self._shape.shape[1]):
            b[h_dim] = np.flip(self._shape[:,h_dim])
        return block(self._type,b)
    def get_type(self):
        return self._type
    def __str__(self):
        return '{0}'.format(self._shape)
    def print(self):
        for i in range(len(self._shape)):
            for j in range(len(self._shape[i])):
                if self._shape[i][j]:
                    pg.draw.rect(screen, (0, 0, 0), (25+40*self.x+40*j,25+40*self.y+40*i,40,40))
block_list = [bl_T,bl_L,bl_J,bl_I,bl_S,bl_Z,bl_O]
block_type = ['T','L', 'J','I','S','Z','O']
x = random.randrange(0,6)
block_now = block(block_type[x],block_list[x],5,0)
block_dim = [len(block_now._shape),len(block_now._shape[0])]


run = True
while run:
    pg.time.delay(100)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    screen.fill((255, 255, 255))  # rgb(255,255,255)
    block_now.print()
    draw()

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and block_now.x > 0:
        block_now.x -= 1
    if keys[pg.K_RIGHT] and block_now.x < 10 - block_dim[1]:
        block_now.x += 1
    if block_now.y < 15 - block_dim[0]:
        block_now.y += 1

    pg.display.update()
    clock.tick(60)
pg.quit()
