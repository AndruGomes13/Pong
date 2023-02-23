############### Imports ################

import pygame
from Ball import *
from pygame.event import Event
import math
import random
from Buttons import *
import time

############### Variable Declaration ###########

# --------------- Constants -----------------

# Window Size
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700
DISPLAY_DIM = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Creating Window
WIN = pygame.display.set_mode(DISPLAY_DIM)
pygame.display.set_caption('Algorithm Demo')

# Frames per second
FPS = 60
CLOCK = pygame.time.Clock()

pygame.init()

objects = []
b1 = Button(10, 10, 100, 20)
b2 = Hover_Button(100, 100 , 200, 50)
objects.append(b1)
objects.append(b2)

running = True
while running:
    CLOCK.tick(FPS)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    input_context = (events, pygame.mouse, pygame.key)
    WIN.fill("white")
    b2.step(input_context, "a")
    b2.draw(WIN)

    pygame.display.update()

pygame.quit()