import pygame as pg
import numpy as np
from time import sleep

###the grid######the boundary###
def draw_frame():
    for v_line in range(1, 10):
        pg.draw.line(screen, (153, 204, 255), [25 + 40 * v_line, 25], [25 + 40 * v_line, 625], 1)  # rgb(153,204,255)
    for h_line in range(1, 15):
        pg.draw.line(screen, (153, 204, 255), [25, 25 + 40 * h_line], [425, 25 + 40 * h_line], 1)  # rgb(153,204,255)
    pg.draw.rect(screen, (255, 255, 255), (25, 0, 425, 25))
    pg.draw.line(screen, (0, 0, 0), [25, 25], [25, 625], 3)  # rgb(0,0,0)
    pg.draw.line(screen, (0, 0, 0), [25, 25], [425, 25], 3)  # rgb(0,0,0)
    pg.draw.line(screen, (0, 0, 0), [425, 25], [425, 625], 3)  # rgb(0,0,0)
    pg.draw.line(screen, (0, 0, 0), [425, 625], [25, 625], 3)  # rgb(0,0,0)


class block:
    def __init__(self,shape,x,y):
        self.shape = shape
        self.x = x
        self.y = y
    def rotate(self):
        self.shape = np.rot90(self.shape,axes=(0,1))
        if collision() or out():
            self.shape = np.rot90(self.shape, 3,axes=(0,1))
    def draw(self):
        for a in self.coor():
            i,j = a
            pg.draw.rect(screen, (0, 0, 0), (25 + 40 * i, 25 + 40 * j, 40, 40))
    def coor(self):
        coor_set = []
        for i in range(len(self.shape)):
            for j in range(len(self.shape[0])):
                if self.shape[i][j] == True:
                    coor_set.append([self.x + j, self.y + i])
        return coor_set

class backgrid:
    def __init__(self,grid):
        self.grid = grid
    def add_to(self):
        for c in block_now.coor():
            i,j = c
            self.grid[j][i] = True
    def T_coor(self):
        t = []
        for y in range(15):
            for x in range(10):
                if self.grid[y][x]:
                    t.append([x,y])
        return t
    def remove(self):
        for q in range(15):
            if all(self.grid[q]):
                self.grid.pop(q)
                self.grid.insert(0, [False for o in range(10)])
    def print_block(self):
        for y in range(2,17):
            for x in range(10):
                if self.grid[y][x] == True:
                    pg.draw.rect(screen, (49, 79, 79), (25 + 40 * x, 25 + 40 * y, 40, 40))

def add_block():
    return block(np.random.choice(block_list),4,0)

def out():
    if block_now.x > 10 - len(block_now.shape[0]) or block_now.x < 0:
        return True

def collision():
    temp_block = block_now.coor()
    temp_grid = back_grid.T_coor()
    for w in temp_block:
        if w in temp_grid:
            return True

def fall_fnc():
    global block_now
    if not(Gameover):
        if block_now.y < 15 - len(block_now.shape):
            block_now.y += 1
        if block_now.y == 15 - len(block_now.shape) or collision():
            if collision():
                block_now.y -= 1
                back_grid.add_to()
                block_now = add_block()
            else:
                back_grid.add_to()
                block_now = add_block()

def ticking():
    global tickCount
    tick = 10
    tickCount += 1
    if tickCount % tick == 0:
        fall_fnc()
        tickCount = 0

def over():
    global Gameover
    font = pg.font.SysFont("comicsansms", 75, False)
    text = font.render("Game Over", 1, (255, 0, 0))
    if any(back_grid.grid[0]):
        Gameover = True
        screen.blit(text, (35,200))
##blocks###
bl_T = np.array([[True,True,True],[False,True,False]])
bl_L = np.array([[True,False],[True,False],[True,True]])
bl_J = np.array([[False,True],[False,True],[True,True]])
bl_I = np.array([[True,True,True,True]])
bl_S = np.array([[False,True,True],[True,True,False]])
bl_Z = np.array([[True,True,False],[False,True,True]])
bl_O = np.array([[True,True],[True,True]])
block_list = [bl_T,bl_L,bl_J,bl_I,bl_S,bl_Z,bl_O]


block_now = block(np.random.choice(block_list),4,0)
grid1 = [[False for x in range(10)] for y in range(17)]
back_grid = backgrid(grid1)



pg.init()
screen = pg.display.set_mode((450,653))
pg.display.set_caption('Tetris')
clock = pg.time.Clock()
tickCount = 0
Gameover = False

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                block_now.rotate()
    ticking()
    screen.fill((255, 255, 255))
    block_now.draw()
    back_grid.print_block()
    draw_frame()
    back_grid.remove()
    over()
####key session####
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and block_now.x > 0:
        block_now.x -= 1
        if collision():
            block_now.x += 1
    if keys[pg.K_RIGHT] and block_now.x < 10 - len(block_now.shape[0]):
        block_now.x += 1
        if collision():
            block_now.x -= 1
    if keys[pg.K_DOWN]:
        fall_fnc()

    pg.display.update()
    clock.tick(20)
pg.quit()
