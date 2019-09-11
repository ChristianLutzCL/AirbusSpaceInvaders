from pygame import *
import sys
from os.path import abspath, dirname


#Paths
BASE_PATH = abspath(dirname(__file__))
IMAGE_PATH = BASE_PATH + '/images/'
SOUND_PATH = BASE_PATH + '/sounds/'

#Color = (Red, Green, Blue)
BLACK = (0, 0, 0)
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

IMAGE_NAMES = ['aircraft', 
               'enemy1_1', 'enemy1_2',
               'enemy2_1', 'enemy2_2', 
               'enemy3_1', 'enemy3_2',
               'explosionblue', 'explosiongreen', 'explosionpurple',
               'laser', 'enemylaser']
IMAGES = {name: image.load(IMAGE_PATH + '{}.png'.format(name)).convert_alpha()
            for name in IMAGE_NAMES}



class PlayerAircraft(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = IMAGES['aircraft']
        self.rect = self.image.get_rect()
        self.speed = 100

    def move(self, x, y):
        game.screen.blit(self.image, (x, y))





class AirbusInvaders(object):
    def __init__(self):
        init()
        self.clock = time.Clock()
        self.background = image.load(IMAGE_PATH + 'airbus_nd.jpg').convert()
        self.screen = SCREEN

        self.startGame = True

        self.p = PlayerAircraft()

        self.x = 50
        self.y = 50




    def main(self):
        while True:
            for e in event.get():
                if e.type == KEYDOWN:
                    if e.key == K_LEFT:
                        self.x += 10
                        self.p.move(self.x, 50)
                    elif e.key == K_RIGHT:
                        self.x -= 10
                        self.p.move(self.x, 400)
                    
            #self.screen.blit(self.background, (0,0))
            display.update()
            self.clock.tick(60)



if __name__ == '__main__':
    game = AirbusInvaders()
    game.main()