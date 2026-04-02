import pygame as py

py.init()
canvas = py.display.set_mode((500,500))
py.display.set_caption('nyan_cat')

class Character:
    def __init__(self, x, y):
        self.image = py.image.load('nyan_cat_firgure.png')
        self.x = x
        self.y = y

    def draw(self):
        canvas.blit(self.image, (self.x, self.y))


color = (200,0,200)
color1 = (0,0,200)
ext = False

x = 200
y = 10

clock = py.time.Clock()
#player = py.Rect(x,y,30,30)
player= Character(x,y)
gravitacija = 3
hitrost_gor = 0

while not ext:
    clock.tick(30)
    canvas.fill(color)
    for event in py.event.get():
        if event.type == py.QUIT:
            ext = True

    keys = py.key.get_pressed()

    if keys[py.K_SPACE] and hitrost_gor < 2:
        hitrost_gor = 15


    #padanje
    player.y += gravitacija - hitrost_gor

    if hitrost_gor > 0:
        hitrost_gor -= 1


    player.draw()

    py.display.update()