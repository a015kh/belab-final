import pygame as pg
import numpy as np
from pygameCamera import Camera
from utils import *

class PoseDance:
    def __init__(self, display, similarity):
        self.RGB = (255, 255, 255)
        self.display = display
        #self.camera = Camera(self.display)
        #self.similarity = similarity
        #self.imgs, self.buttons = loadGamePoses()

    def title(self):
        load('Xeno.jpg', self.display, 0, 0, 1280, 650)
        load('start-b.png', self.display, 500, 470, 252, 72)
        load('quit-b.png', self.display, 500, 570, 252, 72)
        pg.display.update()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
            mouse = pg.mouse.get_pos()
            click = pg.mouse.get_pressed()
            if 500 <= mouse[0] <= 752 and 470<= mouse[1] <= 542:
                load('start-r.png', self.display, 500, 470, 252, 72)
                pg.display.update()
                if click[0] == 1:
                    break
            elif 500 <= mouse[0] <= 752 and 570<= mouse[1] <= 642:
                load('quit-r.png', self.display, 500, 570, 252, 72)
                pg.display.update()
                if click[0] == 1:
                    pg.quit()
            else:
                load('start-b.png', self.display, 500, 470, 252, 72)
                load('quit-b.png', self.display, 500, 570, 252, 72)
                pg.display.update()

    def Game(self):
        # course selection
        load('second.jpg', self.display, 0, 0, 1280, 650)
        load('course1-b.png', self.display, 555, 200, 252, 72)
        load('course2-b.png', self.display, 555, 300, 252, 72)
        load('course3-b.png', self.display, 555, 400, 252, 72)
        pg.display.update()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
            mouse = pg.mouse.get_pos()
            click = pg.mouse.get_pressed()
            if 555 <= mouse[0] <= 807 and 200 <= mouse[1] <= 272:
                load('course1-r.png', self.display, 555, 200, 252, 72)
                pg.display.update()
                if click[0] == 1:
                    course = 1
                    break
            elif 555 <= mouse[0] <= 807 and 300 <= mouse[1] <= 372:
                load('course2-r.png', self.display, 555, 300, 252, 72)
                pg.display.update()
                if click[0] == 1:
                    course = 2
                    break
            elif 555 <= mouse[0] <= 807 and 400 <= mouse[1] <= 472:
                load('course3-r.png', self.display, 555, 400, 252, 72)
                pg.display.update()
                if click[0] == 1:
                    course = 3
                    break
            else:
                load('course1-b.png', self.display, 555, 200, 252, 72)
                load('course2-b.png', self.display, 555, 300, 252, 72)
                load('course3-b.png', self.display, 555, 400, 252, 72)
                pg.display.update()

        Pose = loadPose()

        if (course == 1):
            pg.mixer.music.load("dancing-moon-night.wav")
            pg.mixer.music.set_volume(0.3)
            pg.mixer.music.play(1)
            while True:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                for index in range(29):
                    self.display.blit(Pose[index],(0,index))
                pg.display.update()

        elif (course == 2):
            pg.mixer.music.load("dancing-all-night.wav")
            pg.mixer.music.set_volume(1)
            pg.mixer.music.play(1)
        elif (course == 3):
            pg.mixer.music.load("dancing-star-night.wav")
            pg.mixer.music.set_volume(0.2)
            pg.mixer.music.play(1)






    def run(self):
        self.title()
        self.Game()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
            self.display.fill((0,0,0))
            pg.display.update()

