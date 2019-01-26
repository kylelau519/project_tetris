import pygame as pg
import numpy as np
import random
import time

###the grid######the boundary###
def draw_frame():
    for v_line in range(1, 10):
        pg.draw.line(screen, (153, 204, 255), [25 + 40 * v_line, 25], [25 + 40 * v_line, 625], 1)  # rgb(153,204,255)
        for h_line in range(1, 15):
            pg.draw.line(screen, (153, 204, 255), [25, 25 + 40 * h_line], [425, 25 + 40 * h_line], 1)  # rgb(153,204,255)

            pg.draw.line(screen, (0, 0, 0), [25, 25], [25, 625], 3)  # rgb(0,0,0)
            pg.draw.line(screen, (0, 0, 0), [25, 25], [425, 25], 3)  # rgb(0,0,0)
            pg.draw.line(screen, (0, 0, 0), [425, 25], [425, 625], 3)  # rgb(0,0,0)
            pg.draw.line(screen, (0, 0, 0), [425, 625], [25, 625], 3)  # rgb(0,0,0)
blockCount = 0

class block(object):
    def __init__(self,shape,x,y):
        self._shape = shape
        self._x = x
        self._y = y
    def rotate(self):
        self._shape = np.rot90(self._shape)
    def draw(self):
        for i in range(len(self._shape)):
            for j in range(len(self._shape[i])):
                if self._shape[i][j]:
                    pg.draw.rect(screen, (0, 0, 0), (25+40*self._x+40*j,25+40*self._y+40*i,40,40))
    def kyleon99(self):
        coor_set = []
        for i in range(len(self._shape)):
            for j in range(len(self._shape[i])):
                if self._shape[i][j] == True:
                    coor_set.append((self._x + j, self._y + i))
        return coor_set


def add_block():
    x = random.randrange(0, 6)
    return block(block_list[x],4,0)
def print_block():
    for q in range(0,blockCount):
        block_now[q].draw()


def collision():
    global blockCounts
    for i in range(blockCount):
        for w in block_now[blockCount].kyleon99():
            if w in block_now[i].kyleon99():
                return True

def fall_fnc():
    global blockCount
    if block_now[blockCount]._y < 15 - len(block_now[blockCount]._shape):
        block_now[blockCount]._y += 1
    if block_now[blockCount]._y == 15 - len(block_now[blockCount]._shape):
        blockCount += 1
        block_now.append(add_block())
    elif collision():
        block_now[blockCount]._y -= 1
        blockCount += 1
        block_now.append(add_block())

##blocks###
bl_T = np.array([[True,True,True],[False,True,False]])
bl_L = np.array([[True,False],[True,False],[True,True]])
bl_J = np.array([[False,True],[False,True],[True,True]])
bl_I = np.array([[True,True,True,True]])
bl_S = np.array([[False,True,True],[True,True,False]])
bl_Z = np.array([[True,True,False],[False,True,True]])
bl_O = np.array([[True,True],[True,True]])
block_list = [bl_T,bl_L,bl_J,bl_I,bl_S,bl_Z,bl_O]

init_x = random.randrange(0, 6)
block_now = [block(block_list[init_x],4,0)]

pg.init()
back_grid = np.zeros((20,10),dtype = np.bool)
screen = pg.display.set_mode((500,670))
pg.display.set_caption('tetris')
clock = pg.time.Clock()
FALLING = pg.USEREVENT + 1
pg.time.set_timer(FALLING,400)

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == FALLING:
            fall_fnc()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                block_now[blockCount].rotate()

    screen.fill((255, 255, 255))  # rgb(255,255,255)
    block_now[blockCount].draw()
    draw_frame()
    print_block()



####key session####
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and block_now[blockCount]._x > 0:
        block_now[blockCount]._x -= 1
    if keys[pg.K_RIGHT] and block_now[blockCount]._x < 10 - len(block_now[blockCount]._shape[0]):
        block_now[blockCount]._x += 1
    pg.display.update()
    clock.tick(20)
pg.quit()
