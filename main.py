from pygame import *
import sys
from os.path import abspath, dirname


#Paths
BASE_PATH = abspath(dirname(__file__))
IMAGE_PATH = BASE_PATH + '/images/'
SOUND_PATH = BASE_PATH + '/sounds/'

#Color = (Red, Green, Blue)
WHITE = (255, 255, 255)
GREEN = (78, 255, 87)
YELLOW = (241, 255, 0)
BLUE = (80, 255, 239)
PURPLE = (203, 0, 255)
RED = (237, 28, 36)

#Display
DISPLAY_WIDTH = 530
DISPLAY_HEIGHT = 511
SCREEN = display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

IMAGE_NAMES = ['ship', 
               'enemy1_1', 'enemy1_2',
               'enemy2_1', 'enemy2_2', 
               'enemy3_1', 'enemy3_2',
               'explosionblue', 'explosiongreen', 'explosionpurple',
               'laser', 'enemylaser']
IMAGES = {name: image.load(IMAGE_PATH + '{}.png'.format(name)).convert_alpha()
            for name in IMAGE_NAMES}



class Ship(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = IMAGES['ship']
        self.rect = self.image.get_rect(topleft=(375, 540))
        self.speed = 5

    def update(self, keys, *args):
        if keys[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 740:
            self.rect.x += self.speed
        game.screen.blit(self.image, self.rect)




class SpaceInvaders(object):
    def __init__(self):
        init()
        self.background = image.load(IMAGE_PATH + 'airbus_nd.jpg').convert()
        self.screen = SCREEN
        self.mainScreen = True



    def main(self):
        while True:
            if self.mainScreen:
                self.screen.blit(self.background, (0,0))
            display.update()



if __name__ == '__main__':
    game = SpaceInvaders()
    game.main()