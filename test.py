import pygame as pg
import numpy as np

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

class block:
    def __init__(self,shape,x,y):
        self.shape = shape
        self._x = x
        self._y = y
    def rotate(self):
        self.shape = np.rot90(self.shape,axes=(0,1))
        if collision() or if_out():
            self.shape = np.rot90(self.shape, 3,axes=(0,1))
    def draw(self):
        for a in self.coor():
            i,j = a
            pg.draw.rect(screen, (0, 0, 0), (25 + 40 * i, 25 + 40 * j, 40, 40))
    def coor(self):
        coor_set = []
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if self.shape[i][j] == True:
                    coor_set.append([self._x + j, self._y + i])
        return coor_set
    def after_cut(self):
        self._y += 1

class backgrid:
    def __init__(self,grid):
        self.grid = grid
    def add_to(self):
        global blockCount
        for c in block_now[blockCount].coor():
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

def print_block():
    for y in range(15):
        for x in range(10):
            if back_grid.grid[y][x] == True:
                pg.draw.rect(screen, (0, 0, 0), (25 + 40 * x, 25 + 40 * y, 40, 40))
def add_block():
    return block(np.random.choice(block_list),4,0)

def if_out():
    if block_now[blockCount]._x > 10 - len(block_now[blockCount].shape[0]) or block_now[blockCount]._x < 0:
        return True

def collision():
    global blockCount
    if blockCount > 0:
        temp_block = block_now[blockCount].coor()
        temp_grid = back_grid.T_coor()
        for w in temp_block:
            if w in temp_grid:
                return True

def fall_fnc():
    global blockCount
    if block_now[blockCount]._y < 15 - len(block_now[blockCount].shape):
        block_now[blockCount]._y += 1
    if block_now[blockCount]._y == 15 - len(block_now[blockCount].shape) or collision():
        if collision():
            block_now[blockCount]._y -= 1
            back_grid.add_to()
            blockCount += 1
            block_now.append(add_block())
        else:
            back_grid.add_to()
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


block_now = [block(np.random.choice(block_list),4,0)]
grid1 = [[False for x in range(10)] for y in range(15)]
back_grid = backgrid(grid1)



pg.init()
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

    screen.fill((255, 255, 255))
    block_now[blockCount].draw()
    print_block()
    draw_frame()
    back_grid.remove()
####key session####
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and block_now[blockCount]._x > 0:
        block_now[blockCount]._x -= 1
        if collision():
            block_now[blockCount]._x += 1
    if keys[pg.K_RIGHT] and block_now[blockCount]._x < 10 - len(block_now[blockCount].shape[0]):
        block_now[blockCount]._x += 1
        if collision():
            block_now[blockCount]._x -= 1
    if keys[pg.K_DOWN] and not(block_now[blockCount]._y < 15 - len(block_now[blockCount].shape) and collision()):
        block_now[blockCount]._y += 1

    pg.display.update()
    clock.tick(20)
pg.quit()
