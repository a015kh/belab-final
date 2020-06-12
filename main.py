import pygame as pg
import os
from PoseDance import PoseDance
import random



def main():
    similarity =3 #Similarity()

    pg.init()
    clock = pg.time.Clock()
    clock.tick(30)
    # create screen
    display_width = 960
    display_height = 650
    pos_x = 0
    pos_y = 30
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x, pos_y)
    gameDisplay = pg.display.set_mode((display_width, display_height))
    pg.display.set_caption('Pose Dance')

    game = PoseDance(gameDisplay, similarity)
    game.run()

if __name__ == '__main__':
    main()

# with open('pose.txt', 'w') as fout:
#     for i in range(1,80, 2):
#         fout.write("{} {} {}\n".format(i, random.randint(0,50), random.randint(0,1)))

