#importing libraries
import pygame
from pygame.locals import *
import sys
import time
import random

class TypingSpeed:

    def __init__(self):
        self.w=1920
        self.h=1080


        pygame.init()

        self.bg = pygame.image.load('screen1.png')
        self.bg = pygame.transform.scale(self.bg, (500,750))


        self.screen = pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption('Type Speed test')




    def run(self):
        pygame.display.update()




TypingSpeed().run()
