import pygame as pg
import os
from PoseDance import PoseDance



def main():
    similarity =3 #Similarity()

    pg.init()
    #pg.mixer.music.load("dancing-moon-night.mp3")
    # create screen
    display_width = 1280
    display_height = 650
    pos_x = 0
    pos_y = 30
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x, pos_y)
    gameDisplay = pg.display.set_mode((display_width, display_height))
    pg.display.set_caption('Pose Dance')

    game = PoseDance(gameDisplay, similarity)
    game.run()


main()