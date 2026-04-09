import pygame as py
import threading
import random
import time

from pygame import Surface

py.init()
canvas = py.display.set_mode((500,500))
py.display.set_caption('nyan_cat')

white = (255,255,255)
kovanček = py.mixer.Sound("kovanček.wav")

picture = py.image.load('nyan_cat_firgure.png').convert_alpha()
size = (90, 50)
picture = py.transform.scale(picture, size)

class Character:
    def __init__(self, x, y):
        self.image = picture
        self.image.set_colorkey(white)
        self.x = x
        self.y = y

    def draw(self):
        canvas.blit(self.image, (self.x, self.y))
    
    def get_rect(self):
        return py.Rect(self.x, self.y, size[0], size[1])

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
            nariši(500, 490, 200, 15)
        if num == 2:
            nariši(500, 200, 200, 15)
        if num == 3:
            nariši(500, 300, 200, 15)
            nariši(500, 100, 200, 15)
        if num == 4:
            nariši(500, 400, 200, 15)
            nariši(500, 200, 200, 15)
        if num == 5:
            nariši(500, 490, 200, 15)
        

    
def nariši(x,y,w,h):
    platforme.append([x, y, w, h])
    random_num = random.randint(1, 3)
    if random_num == 1:
        kovanci.append([600, y-20, 10, 10])
    
    
nariši(0, 250, 1000, 20)
threading.Thread(target=nariši_platformo, daemon=True).start()


x = 200
y = 10

clock = py.time.Clock()
#player = py.Rect(x,y,30,30)
player= Character(x,y)
gravitacija = 5 
hitrost_gor = 0

def igra():
    global ext, tocke, player, gravitacija, hitrost_gor
    
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
        pop_seznam_kov=[]
        
        for i in range(len(kovanci)):
            if player.get_rect().colliderect(py.Rect(kovanci[i])):
                tocke += 1
                kovanček.play()
                kovanci.pop(i)
                break  # Da ne pride do napake zaradi spreminjanja seznama med iteracijo
        
        for i in range(len(platforme)):
            if platforme[i][0] < -platforme[i][2]:
                pop_seznam.append(i)
                #print("izbrisano")
        
        for i in range(len(kovanci)):
            if kovanci[i][0] < -10:
                pop_seznam_kov.append(i)
                
        for i in pop_seznam[::-1]:
            platforme.pop(i)
        
        
        for i in pop_seznam_kov[::-1]:
            kovanci.pop(i)
        
        
        for i in range(len(platforme)):
            platforme[i][0] -= 5
            py.draw.rect(canvas, (31, 31, 31), platforme[i])

        dotik = False

        try:
            for dx in range(90):  # širina mačke
                if canvas.get_at((int(player.x + dx), int(player.y + 50)))[:3] == (31, 31, 31):
                    dotik = True
                    break
        except IndexError:
            # GAME OVER - prikaži game over screen
            return game_over_screen()
        if dotik:
            gravitacija = 0
        else:
            gravitacija = 5
            
        for i in range(len(kovanci)):
            kovanci[i][0] -= 5
            py.draw.rect(canvas, (255, 218, 65), kovanci[i])
            
            
        točke = my_font.render(str(tocke), False, (31, 31, 31))
        canvas.blit(točke, (10,10))
        py.display.update()


def game_over_screen():
    """Prikaži game over screen z restart buttonom"""
    global ext, tocke
    
    restart_button_width = 150
    restart_button_height = 60
    restart_button_x = (500 - restart_button_width) // 2
    restart_button_y = 300
    restart_button_rect = py.Rect(restart_button_x, restart_button_y, restart_button_width, restart_button_height)
    
    button_color = (100, 200, 100)
    button_hover_color = (150, 255, 150)
    text_color = (0, 0, 0)
    
    game_over_title = py.font.SysFont('Comic Sans MS', 50).render('GAME OVER', False, (255, 0, 0))
    score_text = my_font.render(f'SCORE: {tocke}', False, (31, 31, 31))
    
    waiting = True
    while waiting and not ext:
        clock.tick(30)
        canvas.blit(bg, (0, 0))
        
        # Naslov
        canvas.blit(game_over_title, (100, 80))
        
        # Score
        canvas.blit(score_text, (150, 180))
        
        # Preveri ali je miška nad buttonom
        mouse_pos = py.mouse.get_pos()
        
        # RESTART button
        restart_color = button_hover_color if restart_button_rect.collidepoint(mouse_pos) else button_color
        py.draw.rect(canvas, restart_color, restart_button_rect)
        py.draw.rect(canvas, (0, 0, 0), restart_button_rect, 2)
        restart_text = my_font.render('RESTART', False, text_color)
        restart_text_rect = restart_text.get_rect(center=restart_button_rect.center)
        canvas.blit(restart_text, restart_text_rect)
        
        # Obdelaj evente
        for event in py.event.get():
            if event.type == py.QUIT:
                ext = True
                return "quit"
            if event.type == py.MOUSEBUTTONDOWN:
                if restart_button_rect.collidepoint(mouse_pos):
                    return "restart"
        
        py.display.update()
    
    return "restart"


def menu():
    """Homescreen menu z Play buttonom"""
    global ext
    
    button_width = 150
    button_height = 60
    button_x = (500 - button_width) // 2
    button_y = (500 - button_height) // 2
    button_rect = py.Rect(button_x, button_y, button_width, button_height)
    
    button_color = (100, 200, 100)
    button_hover_color = (150, 255, 150)
    text_color = (0, 0, 0)
    
    menu_title = my_font.render('NYAN CAT', False, (31, 31, 31))
    
    while not ext:
        clock.tick(30)
        canvas.blit(bg, (0, 0))
        
        # Naslov
        canvas.blit(menu_title, (150, 100))
        
        # Preveri ali je miška nad buttonom
        mouse_pos = py.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            button_color_current = button_hover_color
        else:
            button_color_current = button_color
        
        # Nariši button
        py.draw.rect(canvas, button_color_current, button_rect)
        py.draw.rect(canvas, (0, 0, 0), button_rect, 3)  # Border
        
        # Nariši besedilo na buttonu
        play_text = my_font.render('PLAY', False, text_color)
        text_rect = play_text.get_rect(center=button_rect.center)
        canvas.blit(play_text, text_rect)
        
        # Obdelaj evente
        for event in py.event.get():
            if event.type == py.QUIT:
                ext = True
                return False
            if event.type == py.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(mouse_pos):
                    return True  # Vrni True da se igra() zažene
        
        py.display.update()


while not ext:
    # Prikaži menu in čakaj, da user klikne PLAY
    if menu():
        # Zaženi igro in čakaj rezultat
        result = igra()
        
        if result == "restart":
            # Resetiraj spremenljivke in nadaljuj igro
            tocke = 0
            player = Character(200, 10)
            gravitacija = 5
            hitrost_gor = 0
            platforme.clear()
            kovanci.clear()
            nariši(0, 250, 1000, 20)
        elif result == "menu" or result == None:
            # Vrni se v menu (continue je znotraj while True na začetku)
            pass
        else:
            # Quit
            break
    else:
        break
        
    
    
    
    
    
    
