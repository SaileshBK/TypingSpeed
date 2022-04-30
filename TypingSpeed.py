#importing libraries
import pygame as pg
from pygame.locals import *
import sys
import time
import random

from pyparsing import White

#setting windows width and height
WIDTH, HEIGHT = 1000, 550
WIN = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Typing Speed")
#loading image and scaling it to width and height

TEXT_C = (240,240,240)
pg.init()



def get_sentence():
    #reading lines from text file
    with open("sentences.txt", "r") as file:
        text = file.read()
        text.strip('\n')
        return text
    

def main():
    word = get_sentence()
    #initializing font
    font = pg.font.SysFont(word, 60)
    #rendering font 
    text = font.render(word, True,TEXT_C)
    #posotioning the text from text file.
    text_rect = text.get_rect(topleft=(50,50))
    #load image
    background_image = pg.image.load("screen1.png")
    background_image = pg.transform.scale(background_image,(WIDTH,HEIGHT))

    #blit function takes the image variable and coordinates of the image.
    WIN.blit(background_image,[0,0])
    WIN.blit(text, text_rect)
    #pg.draw.rect(WIN,(255,192,25), (50,250,650,50), 2)


    input_box = pg.draw.rect(WIN,(255,213,102), (50,250,650,50), 2)
    # update the text of user input
    # self.draw_text(self.screen, self.input_text, 274, 26,(250,250,250))
    # pg.display.update()
    user_input = ''
    

    
    run = True
    active = False

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.MOUSEBUTTONUP:
                # in case user click the input box.
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key ==pg.K_RETURN:
                        print(user_input)
                        user_input = ''

        
        
        #updating display
    
        pg.display.update()
    pg.quit()





if __name__ == "__main__":
    main()