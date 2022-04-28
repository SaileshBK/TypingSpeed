#importing libraries
import pygame
from pygame.locals import *
import sys
import time
import random


#setting windows width and height
WIDTH, HEIGHT = 1000, 550
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Typing Speed")
#loading image and scaling it to width and height
background_image = pygame.image.load("screen1.png").convert()
background_image = pygame.transform.scale(background_image,(WIDTH,HEIGHT))


def main():

    run = True

    while run:
        WIN.blit(background_image,[0,0])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()



if __name__ == "__main__":
    main()