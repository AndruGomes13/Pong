############ Imports ############

import pygame
import math

######## Base Dot Class ##########

class Ball:
    def __init__(self, x : int, y : int, default_velocity: int) -> None:
        ### Physics Parameters
        # Position
        self.x = x
        self.y = y
        
        # Velocity
        self.default_velocity = default_velocity
        self.v_x = 0.0
        self.v_y = 0.0

        # Internal Characteristics
        self.radius = 10

        ### Cosmetic Parameters 
        self.color = pygame.Color("white")

    @property
    def velocity(self):
        return ((self.v_x**2) + (self.v_y**2))**(1/2) 

    
    def set_velocity_angle(self, angle):
        self.v_x = math.sin(angle) * self.default_velocity
        self.v_y = math.cos(angle) * self.default_velocity
    
    def coords(self):
        return (self.x, self.y)

    def step(self, dt):
        
        # Position update
        self.x += self.v_x * dt
        self.y += self.v_y * dt


    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

