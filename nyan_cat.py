import pygame as py
import threading
import random
import time

py.init()
canvas = py.display.set_mode((500,500))
py.display.set_caption('nyan_cat')

color = (200,0,200)
ext = False
platforme = []

def nariši_platformo():
    while not ext:
        time.sleep(random.randint(1,2))
        num = random.randint(1,5)
        if num == 1:
            nariši(500, 100, 200, 15)
        if num == 2:
            nariši(500, 200, 200, 15)
        if num == 3:
            nariši(500, 300, 200, 15)
        if num == 4:
            nariši(500, 400, 200, 15)
        if num == 5:
            nariši(500, 490, 200, 15)
        
clock = py.time.Clock()
    
    


def nariši(x,y,w,h):
    platforme.append([x, y, w, h])
nariši(0, 250, 1000, 20)
threading.Thread(target=nariši_platformo, daemon=True).start()
while not ext:
    clock.tick(30)
    canvas.fill(color)
    for event in py.event.get():
        if event.type == py.QUIT:
            ext = True
    
    
    
    
    
    pop_seznam=[]
    
    for i in range(len(platforme)):
        if platforme[i][0] < -platforme[i][2]:
            pop_seznam.append(i)
    
    for i in pop_seznam:
        platforme.pop(i)
    
    for i in range(len(platforme)):
        platforme[i][0] -= 5
        py.draw.rect(canvas, (0,0,0), platforme[i])
        
        
            
    
    py.display.update()