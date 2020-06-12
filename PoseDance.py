import pygame as pg
import numpy as np
import random
# from pygameCamera import Camera
from utils import *
from get_emg import EMGDetector

unit = 1.83
Pool = loadPose()
class PoseDance:
    def __init__(self, display, similarity):
        self.RGB = (255, 255, 255)
        self.display = display
        self.X = []
        self.Y = []
        self.changeX = []
        self.changeY = []
        self.detector = EMGDetector("COM7")
        #self.camera = Camera(self.display)
        #self.similarity = similarity
        #self.imgs, self.buttons = loadGamePoses()

    def title(self):
        pool = loadPose(140,140)
        Pose = []
        for i in range(21):
            Pose.append(pool[random.randint(0,len(Pool)-1)])

        Pose_x = []
        Pose_y = []
        ChangeX = []
        ChangeY = []
        for i in range(len(Pose)):
            Pose_x.append(i*190)
            Pose_y.append(i*50)
            ChangeX.append(1)
            ChangeY.append(1)
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

            self.display.fill(self.RGB)
            for i in range (len(Pose)):
                Pose_x[i] += ChangeX[i]
                if Pose_x[i] <= 0:
                    ChangeX[i] = 1
                elif Pose_x[i] >= 1150:
                    ChangeX[i] = -1

                Pose_y[i] += ChangeY[i]
                if Pose_y[i] <= 0:
                    ChangeY[i] = 1
                elif Pose_y[i] >= 520:
                    ChangeY[i] = -1
                self.display.blit(Pose[i], (Pose_x[i],Pose_y[i]))
            load('logo.png', self.display, 330, 200, 640, 128)
            load('start-b.png', self.display, 500, 470, 252, 72)
            load('quit-b.png', self.display, 500, 570, 252, 72)
            mouse = pg.mouse.get_pos()
            click = pg.mouse.get_pressed()
            if 500 <= mouse[0] <= 752 and 470<= mouse[1] <= 542:
                load('start-r.png', self.display, 500, 470, 252, 72)
                if click[0] == 1:
                    break
            elif 500 <= mouse[0] <= 752 and 570<= mouse[1] <= 642:
                load('quit-r.png', self.display, 500, 570, 252, 72)
                if click[0] == 1:
                    pg.quit()
            else:
                load('start-b.png', self.display, 500, 470, 252, 72)
                load('quit-b.png', self.display, 500, 570, 252, 72)

            pg.display.update()


    def course_select(self):
        start = pg.time.get_ticks()
        imag1 = Pool[random.randint(1, len(Pool) / 3) * 3 - 1]
        imag2 = Pool[random.randint(1, len(Pool) / 3) * 3 - 3]
        imag3 = Pool[random.randint(1, len(Pool) / 3) * 3 - 1]
        imag4 = Pool[random.randint(1, len(Pool) / 3) * 3 - 3]
        imag5 = Pool[random.randint(1, len(Pool) / 3) * 3 - 2]
        imag6 = Pool[random.randint(1, len(Pool) / 3) * 3 - 3]
        imag7 = Pool[random.randint(1, len(Pool) / 3) * 3 - 1]
        imag8 = Pool[random.randint(1, len(Pool) / 3) * 3 - 2]
        imag9 = Pool[random.randint(1, len(Pool) / 3) * 3 - 3]
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
            self.display.fill(self.RGB)
            load('course1-b.png', self.display, 500, 100, 252, 72)
            load('course2-b.png', self.display, 500, 200, 252, 72)
            load('course3-b.png', self.display, 500, 300, 252, 72)
            sec = (pg.time.get_ticks() - start) / 1000
            if sec > 0.175:
                start = pg.time.get_ticks()
                imag1 = Pool[random.randint(1, len(Pool) / 3) * 3 - 1]
                imag2 = Pool[random.randint(1, len(Pool) / 3) * 3 - 3]
                imag3 = Pool[random.randint(1, len(Pool) / 3) * 3 - 1]
                imag4 = Pool[random.randint(1, len(Pool) / 3) * 3 - 3]
                imag5 = Pool[random.randint(1, len(Pool) / 3) * 3 - 2]
                imag6 = Pool[random.randint(1, len(Pool) / 3) * 3 - 3]
                imag7 = Pool[random.randint(1, len(Pool) / 3) * 3 - 1]
                imag8 = Pool[random.randint(1, len(Pool) / 3) * 3 - 2]
                imag9 = Pool[random.randint(1, len(Pool) / 3) * 3 - 2]
            self.display.blit(imag1, (0, 0))
            self.display.blit(imag2, (1050, 0))
            self.display.blit(imag3, (0, 400))
            self.display.blit(imag4, (1050, 400))
            self.display.blit(imag5, (500, 400))
            self.display.blit(imag6, (250, 0))
            self.display.blit(imag7, (780, 0))
            self.display.blit(imag8, (250, 400))
            self.display.blit(imag9, (780, 400))

            mouse = pg.mouse.get_pos()
            click = pg.mouse.get_pressed()
            if 500 <= mouse[0] <= 752 and 100 <= mouse[1] <= 172:
                load('course1-r.png', self.display, 500, 100, 252, 72)
                if click[0] == 1:
                    course = 1
                    break
            elif 500 <= mouse[0] <= 752 and 200 <= mouse[1] <= 272:
                load('course2-r.png', self.display, 500, 200, 252, 72)
                if click[0] == 1:
                    course = 2
                    break
            elif 500 <= mouse[0] <= 752 and 300 <= mouse[1] <= 372:
                load('course3-r.png', self.display, 500, 300, 252, 72)
                if click[0] == 1:
                    course = 3
                    break
            else:
                load('course1-b.png', self.display, 500, 100, 252, 72)
                load('course2-b.png', self.display, 500, 200, 252, 72)
                load('course3-b.png', self.display, 500, 300, 252, 72)
            pg.display.update()
        return course

    def Game(self, course):
        dance = self.sequence('pose.txt')
        imag = []
        init_pos = []
        color = []
        index = 0
        for i in range(len(dance)):
            imag.append(Pool[int(dance[i][1])])
            init_pos.append(dance[i][2])
            color.append(dance[i][1] % 3)
            self.X.append(-1000)
            self.Y.append(300)
            if init_pos[i] == 0:
                self.changeX.append(dance[i][3])
                self.changeY.append(unit)
            elif init_pos[i] == 1:
                self.changeX.append(-dance[i][3])
                self.changeY.append(unit)
        if course == 1:
            pg.mixer.music.load(os.path.join("assets/music", "dancing-moon-night.wav"))
            pg.mixer.music.set_volume(0.3)
            pg.mixer.music.play(1)
            start = pg.mixer.music.get_pos()
        elif course == 2:
            pg.mixer.music.load(os.path.join("assets/music", "dancing-all-night.wav"))
            pg.mixer.music.set_volume(1)
            pg.mixer.music.play(1)
            start = pg.mixer.music.get_pos()
        elif course == 3:
            pg.mixer.music.load(os.path.join("assets/music", "dancing-star-night.wav"))
            pg.mixer.music.set_volume(0.2)
            pg.mixer.music.play(1)
            start = pg.mixer.music.get_pos()
        while pg.mixer.music.get_busy():
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
            self.display.fill((255, 255, 255))   # substitute this line for camera background
            text = "pass" if self.detector.exec() else "not pass"
            load('left.png', self.display, 0, 0, 430, 128)
            load('middle.png', self.display, 430, 0, 425, 150)
            load('right.png', self.display, 855, 0, 430, 128)
            show_text('Score:', self.display, 490, 70, 75, (0, 0, 0))
            show_text(text, self.display, 150, 150, 75, (0, 0, 0))
            sec = (pg.mixer.music.get_pos() - start) / 1000
            show_text('time:' + str(sec), self.display, 0, 70, 75, (0, 0, 0))
            for i in range(len(dance)):
                if sec >= dance[i][0] and sec-dance[i][0] <= 0.08:
                    if index == i:
                        if init_pos[i] == 0:
                            self.X[i] = -300
                            self.Y[i] = 300
                        elif init_pos[i] == 1:
                            self.X[i] = 1280
                            self.Y[i] = 300
                        index += 1
                        break
                elif i == len(dance)-1 and sec-dance[i][0] > 0.1:
                    pass

            # display pose sequence
            self.move(init_pos, self.X, self.Y, self.changeX, self.changeY, imag, color)
            pg.display.update()


    def sequence(self, filename):
        with open(filename, 'r') as fin:
            a = fin.read()
            line = a.split()
            line = np.array([float(s) for s in line]).reshape(-1, 4)
        return line

    def move(self, init_pos, X, Y, changeX, changeY, imag, color):
        for i in range(len(imag)):
            if X[i] != -1000:
                self.display.blit(imag[i], (X[i], Y[i]))
                X[i] += changeX[i]
                if color[i] == 0:  # blue = 0
                    if init_pos[i] == 0 and X[i] >= 950:
                        changeX[i] = 0
                        Y[i] += changeY[i]
                        if Y[i] >= 400:  # here is where the image disappears
                            X[i] = -1000
                    elif init_pos[i] == 1 and X[i] <= 950:
                        changeX[i] = 0
                        Y[i] += changeY[i]
                        if Y[i] >= 400:  # here is where the image disappears
                            X[i] = -1000
                elif color[i] == 1:  # green = 1
                    if init_pos[i] == 0 and X[i] >= 500:
                        changeX[i] = 0
                        Y[i] += changeY[i]
                        if Y[i] >= 400:  # here is where the image disappears
                            X[i] = -1000
                    elif init_pos[i] == 1 and X[i] <= 500:
                        changeX[i] = 0
                        Y[i] += changeY[i]
                        if Y[i] >= 400:  # here is where the image disappears
                            X[i] = -1000
                elif color[i] == 2:  # red = 2
                    if init_pos[i] == 0 and X[i] >= 100:
                        changeX[i] = 0
                        Y[i] += changeY[i]
                        if Y[i] >= 400:  # here is where the image disappears
                            X[i] = -1000
                    elif init_pos[i] == 1 and X[i] <= 100:
                        changeX[i] = 0
                        Y[i] += changeY[i]
                        if Y[i] >= 400:  # here is where the image disappears
                            X[i] = -1000
    def check(self):
        pass

    def bonus(self):
        print('Time to do the bonus')

















    def run(self):
        self.title()
        course = self.course_select()
        self.Game(course)
        self.bonus()


