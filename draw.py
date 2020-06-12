# import posenet
from constants import *
import numpy as np
import pygame as pg
from pygame.locals import QUIT, KEYDOWN

def hex2rgb(hex_value):
    hex_value = hex_value.strip("#")
    r = hex_value[0:2]
    g = hex_value[2:4]
    b = hex_value[4:6]
    return int(r, 16), int(g, 16), int(b, 16)

def l2_dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def draw_poses(display, poses, scale=0.2):
    poses *= scale
    for event in pg.event.get():
        if event.type in (QUIT,KEYDOWN):
            pg.quit()

    #draw the line
    color = 100,255,200
    width = 8
    for a, b in CONNECTED_PART_INDICES:
        # [a_, ay, ax] = poses[a].astype(int)
        # [b_, by, bx] = poses[b].astype(int)
        [ay, ax] = poses[a].astype(int)
        [by, bx] = poses[b].astype(int)
        pg.draw.line(display,color,(ax,ay),(bx,by),width)
        # print()
    # [_, nosex, nosey] = poses[0]
    # [_, e1x, e1y] = poses[1]
    # [_, e2x, e2y] = poses[2]
    [nosex, nosey] = poses[0]
    [e1x, e1y] = poses[1]
    [e2x, e2y] = poses[2]
    r = int(np.mean((l2_dist(nosex, nosey, e1x, e1y), l2_dist(nosex, nosey, e2x, e2y))))
    pg.draw.circle(display,color, (int(nosey), int(nosex)), r + width)
    pg.draw.circle(display,(255,255,255), (int(nosey), int(nosex)), r)
    pg.display.update()

if __name__ == "__main__":
    poses = np.loadtxt("golden_pattern.txt").T
    display_width = 1280
    display_height = 650
    gameDisplay = pg.display.set_mode((display_width, display_height))
    while True:
        draw_poses(gameDisplay, poses)