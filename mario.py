import pygame as pg

class character:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 40
        self.vel = 5
        self.jumping = False
        self.jumpCount = 10
    def jump(self):
        if mario.jumpCount >= -10 and not(self.colli()):
            mario.y -= (mario.jumpCount * abs(mario.jumpCount)) * 0.5
            mario.jumpCount -= 1
        else:
            mario.jumping = False
            mario.jumpCount = 10
    def hitbox(self):
        return pg.Rect(self.x, self.y, self.width, self.height)
    def draw(self):
        pg.draw.rect(screen,(255,255,255),self.hitbox())



class wt_on_earth:
    def __init__(self):
        self.box = [pg.Rect(0,360,400,40),pg.Rect(400,320,200,80)]
    def draw(self):
        for i in range(2):
            pg.draw.rect(screen,(0,255,0),self.box[i])

def colli():
    if mario.hitbox().colliderect(map.box[0]) or mario.hitbox().colliderect(map.box[1]):
        return True
    return False

pg.init()
screen = pg.display.set_mode((600,400))
pg.display.set_caption('Mario')
clock = pg.time.Clock()

mario = character(50,320)
map = wt_on_earth()

run = True
while run:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    screen.fill((0, 0, 0))
    map.draw()
    mario.draw()
    mario.gravity()
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and mario.x > 0:
        mario.x -= mario.vel
        if mario.colli():
            mario.x += mario.vel
    if keys[pg.K_RIGHT] and mario.x < 600:
        mario.x += mario.vel
        if mario.colli():
            mario.x -= mario.vel
    if not(mario.jumping):
        if keys[pg.K_UP]:
            mario.jumping = True
    else:
        mario.jump()

    pg.display.update()
pg.quit()