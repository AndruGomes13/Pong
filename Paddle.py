import pygame


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


    @pos.setter
    def pos(self, input):
        if input < 0:
            self._pos = 0
            return
        if  input > self.screen_width - self.width:
            self._pos = self.screen_width - self.width
            return
        self._pos = input


    def check_ball_collision(self, ball):
        if self.type == "BOTTOM":
            if (ball.y + ball.radius < self.y_pos_contact) or (ball.v_y < 0):
                return False
            
            if (ball.x > self.pos) and (ball.x < self.pos + self.width):
                ball.y = self.y_pos_contact - ball.radius
                ball.v_y *= -1
                return True
            

        if self.type == "TOP":
        
            if (ball.y - ball.radius > self.y_pos_contact)  or (ball.v_y > 0):
                return False
                
            
            if (ball.x > self.pos) and (ball.x < self.pos + self.width):
                ball.y = self.y_pos_contact + ball.radius
                ball.v_y *= -1
                return True 

    def draw(self, win) -> None:
        # Draw button
        rect = pygame.Rect(self.pos, self.y_pos, self.width, self.height)
        pygame.draw.rect(win, pygame.Color("white"), rect)

    
    def step(self, dt):
        
        # Position update
        self.pos += self.vel * dt

