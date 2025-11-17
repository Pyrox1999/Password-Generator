import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '100,100'
import random
import pgzrun
import pygame
import random
import string

random.seed()

pygame.mixer.music.load("song.mp3") #Wolfgang_
pygame.mixer.music.play(-1)

level = -1
pw=""
target="12"

def generate_password(length=12, use_digits=True, use_specials=True):
    chars = string.ascii_letters  # a-z + A-Z
    if use_digits:
        chars += string.digits
    if use_specials:
        chars += "!@#$%^&*()-_=+[]{};:,.<>?/"

    password = "".join(random.choice(chars) for _ in range(length))
    return password

def draw():
    global level,target,pw
    screen.clear()
    if level == -1:
        screen.blit("title", (0, 0))
    elif level == 0:
        screen.blit("intro", (0, 0))
    elif level == 1:
        screen.blit("back", (0, 0))
        screen.draw.text("Password length:", center=(400, 130), fontsize=24, color=(25, 200, 255))
        screen.draw.text(target, center=(400, 180), fontsize=24, color=(255, 255, 0))
    elif level == 3:
        screen.draw.text(pw, center=(400, 380), fontsize=24, color=(255, 255, 0))
        print(pw)

def on_key_down(key, unicode=None):
    global level, target
    if key==keys.ESCAPE:
        pygame.quit()
    if key == keys.BACKSPACE:
        target = ""
    elif key == keys.RETURN and level == 1:
        level = 2
    elif unicode and key != keys.RETURN and level==1:
        target += unicode
    elif level==3 and key==keys.SPACE:
        level=0

def update():
    global level,target,pw
    if (level == 0 or level==-2) and keyboard.RETURN:
        level +=1
    elif level -1 and keyboard.space:
        level = 0
    if level==2:
        pw=generate_password(int(target))
        level=3

pgzrun.go()
