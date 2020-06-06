import pygame as pg
import os
import numpy as np

def load(filename, display, x=0, y=0, a=96, b=96):
    image = pg.image.load(filename)
    image = pg.transform.scale(image,(a,b))  
    display.blit(image,(x,y))   

def load_image(filename, a=160, b=160):
    image = pg.image.load(filename)
    image = pg.transform.scale(image, (a,b))  
    return image
    
def show_text(text, display, x, y, size=30, color=(255,255,255)):
    font = pg.font.SysFont('timesnewroman', size)
    render_txt = font.render(text, True, color)
    display.blit(render_txt, (x,y))
        
def loadPose(a=256,b=256):
    imgs = []
    for index in range (1, 11):
        imgs.append(load_image('{:02}-b'.format(index)+'.png',a, b))
        imgs.append(load_image('{:02}-g'.format(index)+'.png', a, b))
        imgs.append(load_image('{:02}-r'.format(index)+'.png', a, b))
    imgs = np.array(imgs)
    return imgs

def loadPauseButtons():
    buttons = []
    buttons.append(load_image('play.png',200,200))
    buttons.append(load_image('exit.png',200,200))
    return buttons
    
def loadEndButtons():
    buttons = []
    buttons.append(load_image('replay.png',200,200))
    buttons.append(load_image('exit.png',200,200))
    return buttons
