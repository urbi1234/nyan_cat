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

while not ext:
    clock.tick(30)
    canvas.fill(color)
    for event in py.event.get():
        if event.type == py.QUIT:
            ext = True

    keys = py.key.get_pressed()

    if keys[py.K_SPACE]:
        player.y -= 10
        
        player.y += 10


    py.draw.rect(canvas, (10, 230, 180), player)

    py.display.update()