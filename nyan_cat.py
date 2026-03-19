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
        time.sleep(random.randint(1,4))
        nariši(500, random.randint(0,500), random.randint(20,500), 10)
        
clock = py.time.Clock()
    
    


def nariši(x,y,w,h):
    platforme.append([x, y, w, h])

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