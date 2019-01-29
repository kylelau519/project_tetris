import pygame as pg

class character:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vel = 10
        self.jumping = False
        self.jumpCount = 10
    def draw(self):
        pg.draw.rect(screen,(255,255,255),(self.x,self.y,50,50))


pg.init()
screen = pg.display.set_mode((600,400))
pg.display.set_caption('Mario')
clock = pg.time.Clock()


mario = character(50,350)


run = True
while run:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    screen.fill((0, 0, 0))
    mario.draw()

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and mario.x > 0:
        mario.x -= mario.vel
    if keys[pg.K_RIGHT] and mario.x < 550:
        mario.x += mario.vel
    if keys[pg.K_UP] or mario.jumping:
        mario.jumping = True
        if mario.jumpCount >= -10:
            mario.y -= (mario.jumpCount * abs(mario.jumpCount)) * 0.5
            mario.jumpCount -= 2
        else:
            mario.jumping = False
            mario.jumpCount = 10



    pg.display.update()
pg.quit()