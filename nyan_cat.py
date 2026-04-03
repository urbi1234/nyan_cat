import pygame as py
import threading
import random
import time

py.init()
canvas = py.display.set_mode((500,500))
py.display.set_caption('nyan_cat')

white = (255,255,255)






class Character:
    def __init__(self, x, y):
        self.image = py.image.load('nyan_cat_firgure-ozadje.png').convert_alpha()
        self.image.set_colorkey(white)
        self.size = (80, 50)
        self.image = py.transform.scale(self.image, self.size)
        self.x = x
        self.y = y

    def draw(self):
        canvas.blit(self.image, (self.x, self.y))
    
    def get_rect(self):
        return py.Rect(self.x, self.y, self.size[0], self.size[1])

bg = py.image.load('ozadje.png')
bg = py.transform.scale(bg, (500,500))
py.font.init()
my_font = py.font.SysFont('Comic Sans MS', 30)

color = (200,0,200)
color1 = (0,0,200)
ext = False
platforme = []
kovanci=[]

tocke=0

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
        

    
def nariši(x,y,w,h):
    platforme.append([x, y, w, h])
    random_num = random.randint(1,2)
    if random_num == 1:
        kovanci.append([600, y-20, 10, 10])
    
    
nariši(0, 250, 1000, 20)
threading.Thread(target=nariši_platformo, daemon=True).start()


x = 200
y = 10

clock = py.time.Clock()
#player = py.Rect(x,y,30,30)
player= Character(x,y)
gravitacija = 3
hitrost_gor = 0

while not ext:
    clock.tick(30)
    canvas.blit(bg, (0,0))
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
    pop_seznam=[]
    
    for i in range(len(kovanci)):
        if player.get_rect().colliderect(py.Rect(kovanci[i])):
            tocke += 1
            kovanci.pop(i)
            break  # Da ne pride do napake zaradi spreminjanja seznama med iteracijo
    
    for i in range(len(platforme)):
        if platforme[i][0] < -platforme[i][2]:
            pop_seznam.append(i)
    
    for i in pop_seznam:
        platforme.pop(i)
    
    for i in range(len(platforme)):
        platforme[i][0] -= 5
        py.draw.rect(canvas, (31, 31, 31), platforme[i])
        
    for i in range(len(kovanci)):
        kovanci[i][0] -= 5
        py.draw.rect(canvas, (255, 218, 65), kovanci[i])
        
        
    točke = my_font.render(str(tocke), False, (31, 31, 31))
    canvas.blit(točke, (10,10))
    py.display.update()



    
    
    
    
    
    