import pygame
import math

class Paddle:

    def __init__(self, width:int, screen_dim: tuple, t: "TOP/BOTTOM" ) -> None:

        self.width = width
        self.height = 20
        self.screen_width = screen_dim[0]
        self.screen_height = screen_dim[1]

        self.type = t
        self.y_pos = 0

        if self.type == "BOTTOM":
            self.y_pos = self.screen_height - self.height
            self.y_pos_contact = self.y_pos
        if self.type == "TOP":
            self.y_pos = 0
            self.y_pos_contact = self.height
    
        # Setting starting position at the middle
        self._pos = self.screen_width / 2
        self.vel = 0

    @property
    def pos(self):
        return self._pos

    @property
    def center_pos(self):
        return self._pos + self.width/2

    @pos.setter
    def pos(self, input):
        if input < 0:
            self._pos = 0
            return
        if  input > self.screen_width - self.width:
            self._pos = self.screen_width - self.width
            return
        self._pos = input

    def set_new_vel(self, hit_pos, ball):
        # hit_pos_normalized = (hit_pos - 0.5) * 2
        # return_angle = hit_pos_normalized * math.pi / 2
        # vel = ball.velocity
        # ball.v_x = (vel * math.sin(return_angle) * abs(hit_pos_normalized) + ball.v_x * (1 - abs(hit_pos_normalized)))
        # if self.type == "TOP":
        #     ball.v_y = (vel * math.cos(return_angle) - ball.v_y) / 2
        #     return
        # ball.v_y = - (vel * math.cos(return_angle) + ball.v_y) / 2
        max_angle = math.radians(75)
        hit_pos_normalized = (hit_pos - 0.5) * 2
        return_angle = max_angle * hit_pos_normalized
        if self.type == "TOP":
            ball.set_velocity_angle(return_angle)
            return

        ball.set_velocity_angle(- return_angle + math.pi)
        return
        




    def check_ball_collision(self, ball):
        if self.type == "BOTTOM":
            if (ball.y + ball.radius < self.y_pos_contact) or (ball.v_y < 0):
                return False
            
            if (ball.x > self.pos) and (ball.x < self.pos + self.width):
                ball.y = self.y_pos_contact - ball.radius
                hit_position = (ball.x - self.pos) / self.width 
                self.set_new_vel(hit_position, ball)
                return True
            

        if self.type == "TOP":
        
            if (ball.y - ball.radius > self.y_pos_contact)  or (ball.v_y > 0):
                return False
                
            
            if (ball.x > self.pos) and (ball.x < self.pos + self.width):
                ball.y = self.y_pos_contact + ball.radius
                hit_position = (ball.x - self.pos) / self.width 
                self.set_new_vel(hit_position, ball)
                return True 

    def draw(self, win) -> None:
        # Draw button
        rect = pygame.Rect(self.pos, self.y_pos, self.width, self.height)
        pygame.draw.rect(win, pygame.Color("white"), rect)

    
    def step(self, dt):
        
        # Position update
        self.pos += self.vel * dt

