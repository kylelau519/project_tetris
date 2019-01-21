
import pygame as pg
import numpy as np
pg.init()

back_grid = np.zeros((20,10),dtype = np.bool)
print back_grid

screen = pg.display.set_mode((500,670))
screen.fill((255,255,255))#rgb(255,255,255)
pg.display.set_caption('tetris')

###the grid###
for v_line in range(1,10):
    pg.draw.line(screen,(153,204,255),[25+40*v_line,25],[25+40*v_line,625],1)#rgb(153,204,255)
for h_line in range(1,15):
    pg.draw.line(screen,(153,204,255),[25,25+40*h_line],[425,25+40*h_line],1)#rgb(153,204,255)


###the boundary###
pg.draw.line(screen,(0,0,0),[25,25],[25,625],3)#rgb(0,0,0)
pg.draw.line(screen,(0,0,0),[25,25],[425,25],3)#rgb(0,0,0)
pg.draw.line(screen,(0,0,0),[425,25],[425,625],3)#rgb(0,0,0)
pg.draw.line(screen,(0,0,0),[425,625],[25,625],3)#rgb(0,0,0)


##blocks###
bl_T = np.array([[True,True,True],[False,True,False]])
bl_L = np.array([[True,False],[True,False],[True,True]])
bl_J = np.array([[False,True],[False,True],[True,True]])
bl_I = np.array([[True,True,True,True],[False,False,False,False]])
bl_S = np.array([[False,True,True],[True,True,False]])
bl_Z = np.array([[True,True,False],[False,True,True]])
bl_O = np.array([[True,True],[True,True]])

pg.display.update()

run = True
while run:
    pg.time.delay(100)


    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

pg.quit()
