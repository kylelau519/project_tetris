import pygame as pg
from random import randrange as rg

class player:
    def __init__(self):
        self.body = [[5,5],[6,5],[7,5]]
        self.x = 5
        self.y = 5
        self.up = False
        self.down = False
        self.left = True
        self.right = False
        self.poped = []
    def draw(self):
        for q in self.body:
            a,b = q
            pg.draw.rect(screen,(255,255,255),(a * 20,b * 20,20,20))
    def move(self):
        global Gameover
        if not(Gameover):
            if self.left:
                self.x -= 1
            if self.right:
                self.x += 1
            if self.up:
                self.y -= 1
            if self.down:
                self.y += 1
            self.body.insert(0, [self.x, self.y])
            self.poped = self.body.pop(len(self.body)-1)
    def collision(self):
        global Gameover
        if self.x > 11 or (self.x < 0 or (self.y < 0 or self.y > 11)):
            Gameover = True
        for i in range(1,len(self.body)):
            if self.body[0] in self.body[i]:
                Gameover = True

class fruit:
    def __init__(self):
        self.x = rg(0,11)
        self.y = rg(0,11)
    def popup(self,thing):
        self.x = rg(0,11)
        self.y = rg(0,11)
        if [self.x,self.y] in thing.body:
            self.popup()
    def draw(self):
        pg.draw.rect(screen,(255,0,0),(self.x * 20,self.y * 20,20,20))

def eat(something):
    if [apple.x,apple.y] == [snake.x,snake.y]:
        apple.popup(something)
        snake.body.insert(len(snake.body),snake.poped)

def ticking(thing):
    global tickCount
    global dirCount
    tick = 5
    tickCount += 1
    if tickCount % tick == 0:
        thing.move()
        tickCount = 0
        dirCount = False

def ggdelay():
    global delayCount
    delayCount += 1
    if delayCount >= 60:
        run = False


pg.init()
screen = pg.display.set_mode((220,220))
pg.display.set_caption('Snake')
clock = pg.time.Clock()
tickCount = 0
dirCount = True
delayCount = 0
Gameover = False

font = pg.font.SysFont("comicsansms", 25, False)
text = font.render("Game Over", 1, (0, 255, 0))

apple = fruit()
snake = player()



run = True
while run:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN and not(dirCount):
            if not(snake.down):
                if event.key == pg.K_UP:
                    snake.up = True
                    snake.down = False
                    snake.left = False
                    snake.right = False
                    dirCount = True
            if not(snake.up):
                if event.key == pg.K_DOWN:
                    snake.up = False
                    snake.down = True
                    snake.left = False
                    snake.right = False
                    dirCount = True
            if not(snake.left):
                if event.key == pg.K_RIGHT:
                    snake.up = False
                    snake.down = False
                    snake.left = False
                    snake.right = True
                    dirCount = True
            if not(snake.right):
                if event.key == pg.K_LEFT:
                    snake.up = False
                    snake.down = False
                    snake.left = True
                    snake.right = False
                    dirCount = True
    if not(Gameover):
        screen.fill((0,0,0))
        snake.collision()
        ticking(snake)
        eat(snake)
        apple.draw()
        snake.draw()
    else:
        screen.blit(text, (0, 0))
        ggdelay()











    pg.display.update()
pg.quit()