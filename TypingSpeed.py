#importing libraries
import pygame
from pygame.locals import *
import sys
import time
import random

from pyparsing import White
pygame.init()

#setting windows width and height
WIDTH, HEIGHT = 1000, 550
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Typing Speed")
#loading image and scaling it to width and height
background_image = pygame.image.load("screen1.png").convert()
background_image = pygame.transform.scale(background_image,(WIDTH,HEIGHT))
TEXT_C = (240,240,240)



def main():

    run = True
    word = get_sentence()

    while run:

        #blit function takes the image variable and coordinates of the image
        WIN.blit(background_image,[0,0])
        draw_text(WIN, word, 200, 28, TEXT_C )


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        
        #updating display
    
        pygame.display.update()
    pygame.quit()

def draw_text(WIN, msg, y ,fsize, color):
    font = pygame.font.Font(None, fsize)
    text = font.render(msg, 1,color)
    text_rect = text.get_rect(topleft=(50,50))
    WIN.blit(text, text_rect)
    #pygame.display.update()

def get_sentence():
    f = open('sentences.txt').read()
    sentences = f.split('\n')
    sentence = random.choice(sentences)
    return sentence

if __name__ == "__main__":
    main()