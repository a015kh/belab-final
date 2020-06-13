from constants import *
import numpy as np
import pygame as pg
from pygame.locals import QUIT, KEYDOWN
from math import pi

def hex2rgb(hex_value):
    hex_value = hex_value.strip("#")
    r = hex_value[0:2]
    g = hex_value[2:4]
    b = hex_value[4:6]
    return int(r, 16), int(g, 16), int(b, 16)

def l2_dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def draw_poses(display, poses, scale=1):
    """
    in PoseDance.Game()
    while scope:
        poses = self.similarity.keypoint_coords
        draw_poses(self.display, poses)
    """
    poses *= scale
    poses = np.reshape(poses, (17, 2))
    poses[:, 1] = 960 - poses[:, 1]
    #print(poses.shape)
    for event in pg.event.get():
        if event.type in (QUIT,KEYDOWN):
            pg.quit()

    color = 100,255,200
    width = 4
    for a, b in CONNECTED_PART_INDICES:

        [ay, ax] = poses[a].astype(int)
        [by, bx] = poses[b].astype(int)
        pg.draw.line(display,color,(ax,ay),(bx,by),width)

    [nosex, nosey] = poses[0]
    [e1x, e1y] = poses[1]
    [e2x, e2y] = poses[2]
    r = int(np.max((l2_dist(nosex, nosey, e1x, e1y), l2_dist(nosex, nosey, e2x, e2y))))
    c = (int(nosey), int(nosex))
    r = np.floor((r + width) * 2)
    pg.draw.arc(display, color, (c[0]-r, c[1]-r, r, r), -pi/2, -pi/2-0.01, width)
    pg.display.update()

if __name__ == "__main__":
    """test"""
    poses = np.loadtxt("golden_pattern.txt").T
    display_width = 1280
    display_height = 650
    gameDisplay = pg.display.set_mode((display_width, display_height))
    draw_poses(gameDisplay, poses)

