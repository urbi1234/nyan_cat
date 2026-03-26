import pygame as py

py.init()
canvas = py.display.set_mode((500,500))
py.display.set_caption('nyan_cat')

color = (200,0,200)
color1 = (0,0,200)
ext = False

x = 10
y = 10

clock = py.time.Clock()
player = py.Rect(x,y,30,30)

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


    py.draw.rect(canvas, (10, 230, 180), player)

    py.display.update()