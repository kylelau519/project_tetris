import pygame as pg
import numpy as np
import random
import time
import tetris_block as blk
import tetris_back as bg
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

bl_Count = 0
bg = bg.background()

def fall_fnc():
    global bl_Count
    global bg
    if (bl_now[bl_Count].pos_y < 15 - len(bl_now[bl_Count].shape)) and (
     not bg.check_blocked(bl_now[bl_Count].pos_y,bl_now[bl_Count].pos_x,'Down',bl_now[bl_Count])):
        bl_now[bl_Count].pos_y += 1

    elif (bl_now[bl_Count].pos_y < 15 - len(bl_now[bl_Count].shape)) and (
      bg.check_blocked(bl_now[bl_Count].pos_y,bl_now[bl_Count].pos_x,'Down',bl_now[bl_Count])):
        bg.set_pos_blocked(bl_now[bl_Count].pos_y,bl_now[bl_Count].pos_x,bl_now[bl_Count].shape)
        bg.check_explode(bl_now[bl_Count])
        bl_Count += 1
        bl_now.append(add_block())



    elif bl_now[bl_Count].pos_y == 15 - len(bl_now[bl_Count].shape):
        bg.set_pos_blocked(bl_now[bl_Count].pos_y,bl_now[bl_Count].pos_x,bl_now[bl_Count].shape)
        bg.check_explode(bl_now[bl_Count])
        bl_Count += 1
        bl_now.append(add_block())


def add_block():
    x = random.randrange(0, 6)
    return blk.block(block_type[x],block_list[x],4,0)
####dont know why is dont work
def print_block():
    bl_now[bl_Count].draw(screen)

def grid_block(screen):
    global bg
    for i in range(0,bg.grid.shape[0]):
        for j in range(0,bg.grid.shape[1]):
            if bg.grid[i][j]:
                pg.draw.rect(screen,(90,90,90), (25+40*j,25+40*i,40,40))


##blocks###
bl_T = np.array([[True,True,True],[False,True,False]])
bl_L = np.array([[True,False],[True,False],[True,True]])
bl_J = np.array([[False,True],[False,True],[True,True]])
bl_I = np.array([[True,True,True,True]])
bl_S = np.array([[False,True,True],[True,True,False]])
bl_Z = np.array([[True,True,False],[False,True,True]])
bl_O = np.array([[True,True],[True,True]])
block_list = [bl_T,bl_L,bl_J,bl_I,bl_S,bl_Z,bl_O]
block_type = ['T', 'L', 'J', 'I', 'S', 'Z', 'O']

init = random.randrange(0, 6)
bl_now = [blk.block(block_type[init],block_list[init],4,0)]


pg.init()

screen = pg.display.set_mode((500,670))
pg.display.set_caption('tetris')
clock = pg.time.Clock()
FALLING = pg.USEREVENT + 1
pg.time.set_timer(FALLING,500)

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == FALLING:
            fall_fnc()

    screen.fill((255, 255, 255))  # rgb(255,255,255)
    bl_now[bl_Count].draw(screen)
    draw_frame()
    print_block()
    grid_block(screen)
####key session+block####
    keys = pg.key.get_pressed()
    if (keys[pg.K_LEFT] and bl_now[bl_Count].pos_x > 0 and
    not bg.check_blocked(bl_now[bl_Count].pos_y,bl_now[bl_Count].pos_x,'Left',bl_now[bl_Count])):
        bl_now[bl_Count].pos_x -= 1

    if (keys[pg.K_RIGHT] and bl_now[bl_Count].pos_x < 10 - len(bl_now[bl_Count].shape[0]) and
    not bg.check_blocked(bl_now[bl_Count].pos_y,bl_now[bl_Count].pos_x,'Right',bl_now[bl_Count])):
        bl_now[bl_Count].pos_x += 1

    if keys[pg.K_UP] and not bg.check_blocked(bl_now[bl_Count].pos_y,bl_now[bl_Count].pos_x,'Rotation',bl_now[bl_Count]):
        bl_now[bl_Count].rotate()


    pg.display.update()
    clock.tick(10)
pg.quit()
