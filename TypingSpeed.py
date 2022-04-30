#importing libraries
import pygame
from pygame.locals import *
import sys
import time
import random

from pyparsing import White

#setting windows width and height
WIDTH, HEIGHT = 1000, 550
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Typing Speed")
#loading image and scaling it to width and height

TEXT_C = (240,240,240)
pygame.init()



def get_sentence():
    #reading lines from text file
    with open("sentences.txt", "r") as file:
        text = file.read()
        text.strip('\n')
        return text
    

def main():
    word = get_sentence()
    #initializing font
    font = pygame.font.SysFont(word, 60)
    #rendering font 
    text = font.render(word, True,TEXT_C)
    #posotioning the text from text file.
    text_rect = text.get_rect(topleft=(50,50))
    #load image
    background_image = pygame.image.load("screen1.png")
    background_image = pygame.transform.scale(background_image,(WIDTH,HEIGHT))

    #blit function takes the image variable and coordinates of the image.
    WIN.blit(background_image,[0,0])
    WIN.blit(text, text_rect)
    
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        
        #updating display
    
        pygame.display.update()
    pygame.quit()





if __name__ == "__main__":
    main()