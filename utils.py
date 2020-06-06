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
    font = pg.font.SysFont('comicsansms', size)
    render_txt = font.render(text, True, color)
    display.blit(render_txt, (x,y))
        
def loadPose():
    imgs = []
    for index in range (1, 11):
        imgs.append(load_image('{:02}-b'.format(index)+'.png',96,96))
        imgs.append(load_image('{:02}-g'.format(index)+'.png', 96, 96))
        imgs.append(load_image('{:02}-r'.format(index)+'.png', 96, 96))
    imgs = np.array(imgs)
    return imgs
        
def loadGamePoses():
    imgs = []
    imgs.append(load_image('pessistic.png'))
    imgs.append(load_image('surprised.png'))
    imgs.append(load_image('wink.png'))
    imgs.append(load_image('sad.png'))
    imgs.append(load_image('grin.png'))
    imgs.append(load_image('angry.png'))
    imgs.append(load_image('LeftO.png'))
    imgs.append(load_image('RightO.png'))
    imgs.append(load_image('toothache.png'))
    imgs.append(load_image('calm.png'))
    imgs.append(load_image('bling.png'))
    imgs = np.array(imgs)

    buttons = []
    buttons.append(load_image('pause.png',96,96))
    buttons.append(load_image('exit.png',96,96))
    buttons = np.array(buttons)

    return imgs, buttons

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
