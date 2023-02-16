############ Imports ############

import pygame

######## Base Dot Class ##########

class Ball:
    def __init__(self, x : int, y : int) -> None:
        ### Physics Parameters
        # Position
        self.x = x
        self.y = y
        
        # Velocity
        self.v_x = 0.0
        self.v_y = 0.0

        # Internal Characteristics
        self.radius = 10

        ### Cosmetic Parameters 
        self.color = pygame.Color("white")
    
    def coords(self):
        return (self.x, self.y)

    def step(self, dt):
        
        # Position update
        self.x += self.v_x * dt
        self.y += self.v_y * dt


    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

