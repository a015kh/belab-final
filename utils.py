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
        if (index != 4 and index != 5 and index != 8):
            imgs.append(load_image('{:02}-b'.format(index)+'.png',a, b))
            imgs.append(load_image('{:02}-g'.format(index)+'.png', a, b))
            imgs.append(load_image('{:02}-r'.format(index)+'.png', a, b))
    for index in range (1, 11):
        if (index != 4 and index != 5 and index != 8):
            imgs.append(pg.transform.flip(load_image('{:02}-b'.format(index)+'.png',a, b), True, False))
            imgs.append(pg.transform.flip(load_image('{:02}-g'.format(index)+'.png',a, b), True, False))
            imgs.append(pg.transform.flip(load_image('{:02}-r'.format(index)+'.png',a, b), True, False))
    imgs.append(pg.transform.flip(load_image('{:02}-b'.format(4) + '.png', a, b), True, False))
    imgs.append(pg.transform.flip(load_image('{:02}-g'.format(4) + '.png', a, b), True, False))
    imgs.append(pg.transform.flip(load_image('{:02}-r'.format(4) + '.png', a, b), True, False))
    imgs.append(pg.transform.flip(load_image('{:02}-b'.format(5) + '.png', a, b), True, False))
    imgs.append(pg.transform.flip(load_image('{:02}-g'.format(5) + '.png', a, b), True, False))
    imgs.append(pg.transform.flip(load_image('{:02}-r'.format(5) + '.png', a, b), True, False))
    imgs.append(pg.transform.flip(load_image('{:02}-b'.format(8) + '.png', a, b), True, False))
    imgs.append(pg.transform.flip(load_image('{:02}-g'.format(8) + '.png', a, b), True, False))
    imgs.append(pg.transform.flip(load_image('{:02}-r'.format(8) + '.png', a, b), True, False))



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
