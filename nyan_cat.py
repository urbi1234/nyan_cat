import pygame as py

py.init()
canvas = py.display.set_mode((500,500))
py.display.set_caption('nyan_cat')

ext = False

while not ext:
    for event in py.event.get():
        if event.type == py.QUIT:
            ext = True