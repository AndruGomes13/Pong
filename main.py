############### Imports ################

import pygame
from Ball import *
from pygame.event import Event
import math
import random
from Paddle import Paddle
from Joystick import Joystick
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
FPS = 200
CLOCK = pygame.time.Clock()


# --------------- Global Variables ------------

# Initialize global project variables
pygame.init()

# Program Context
ProgramContext = {"Player_1_vel": 0,
                  "Playey_2_vel": 0}


########## Auxiliary functions ##########

# Adds dot

def distance(ball_1, ball_2):
    return ((ball_1.x - ball_2.x)**2 + (ball_1.y - ball_2.y)**2)**(1/2)

# Handles mouse clicks (Adding and removing dots)
def click_handling(event: Event, mouse_pos : tuple, ProgramContext : ProgramContext) -> None:
    if event.button == 1 and ProgramContext["Mode_dot_create"]:
        add_ball(mouse_pos, "red")

    if event.button == 1 and ProgramContext["Mode_dot_remove"]:
        rm_ball_last(ball_list)

    if event.button == 3 and ProgramContext["Mode_dot_create"]:
        add_ball(mouse_pos, "blue")

# Handles key presses (Mode changes)
def key_handling(event: Event, ProgramContext: ProgramContext) -> None:
    
    # Set dot add mode
    if event.key == pygame.K_a:
        pass
        ProgramContext["Player_1_vel"] = -1

    # Set dot remove mode
    if event.key == pygame.K_d:
        pass
        ProgramContext["Player_1_vel"] = 1
# Physics Functions


def ground_collision(ball, dt):
    position_prediction = (ball.x + ball.v_x * dt, ball.y + ball.v_y * dt)

       # Floor
    if (position_prediction[0]) >= DISPLAY_DIM[0] - ball.radius:
        ball.v_x *= -1
        return
        # Ceiling
    if (position_prediction[0]) <= ball.radius:
        ball.v_x *= -1
        return

        # Right Wall
    if (position_prediction[1]) >= DISPLAY_DIM[1] - ball.radius:
        ball.v_y *= -1
        return

        # Left Wall
    if (position_prediction[1]) <= ball.radius:
        ball.v_y *= -1
        return

# Displays FPS
def display_fps():
    "Data that will be rendered and blitted in _display"
    def render(fnt, what, color, where):
        "Renders the fonts as passed from display_fps"
        text_to_show = fnt.render(what, 1, pygame.Color(color))
        WIN.blit(text_to_show, where)

    # Renders the FPS count at the corner of the screen
    render(
        pygame.font.SysFont("Arial", 20),
        what  = str(int(CLOCK.get_fps())),
        color = "green",
        where = (WINDOW_WIDTH - 50, 0))

def ball_outside(ball):
    if (ball.y + ball.radius > WINDOW_HEIGHT - 4) or (ball.y - ball.radius < 4):
        return True
    return False 

def show_gameover_screen(win):
    fnt = pygame.font.SysFont("Arial", 40)
    text = fnt.render("Game Over", True, pygame.Color("red"))
    win.blit(text, (WINDOW_WIDTH//2 - text.get_width() // 2, WINDOW_HEIGHT//2 - text.get_height()//2))
    pygame.display.flip()
    waiting = True
    while waiting:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
        




########## Main ##########
def main():


    # Running
    running = True

    # Initializing joystick input
    joystick = Joystick()


    ### Initializing aux variables
    getTicksLastFrame = pygame.time.get_ticks()

    object_list = []

    ### Setting up paddles
    # Setting top paddle
    player_1 = Paddle(100, DISPLAY_DIM, "TOP")
    player_1.t = "TOP"
    object_list.append(player_1)

    # Setting bottom paddle
    player_2 = Paddle(100, DISPLAY_DIM, "BOTTOM")
    object_list.append(player_2)
    
    # Setting ball
    ball_velocity = 300
    ball = Ball(WINDOW_WIDTH//2, WINDOW_HEIGHT//2, ball_velocity)
    ball.set_velocity_angle(random.random())

    object_list.append(ball)



    while running:
        # Setting FPS
        CLOCK.tick(FPS)

        # Getting Mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Resetting velocities
        ProgramContext.update({"Player_1_vel": 0, "Player_2_vel": 0})


        ########## Handling key presses #############
        pressed_keys = pygame.key.get_pressed()
        
        ### Paddle 1
        if pressed_keys[pygame.K_a]:
            ProgramContext["Player_1_vel"] = -300
        if pressed_keys[pygame.K_d]:
            ProgramContext["Player_1_vel"] = 300

        ### Paddle 2
        # if pressed_keys[pygame.K_RIGHT]:
        #     ProgramContext["Player_2_vel"] = 300
        # if pressed_keys[pygame.K_LEFT]:
        #     ProgramContext["Player_2_vel"] = -300
        ProgramContext["Player_2_vel"] = joystick.get_joystick()[1] * 300

        ########### Top player AI ###########
        AI_max_speed = ball_velocity * 0.6
        if player_1.center_pos - 20> ball.x:
            ProgramContext["Player_1_vel"] = -AI_max_speed

        elif player_1.center_pos + 20 < ball.x:
            ProgramContext["Player_1_vel"] = AI_max_speed



        # Updating game status with program context

        player_1.vel = ProgramContext["Player_1_vel"]
        player_2.vel = ProgramContext["Player_2_vel"]


        


        #######################
        # Handling events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_handling(event, mouse_pos, ProgramContext)

            if event.type == pygame.KEYDOWN:
                key_handling(event, ProgramContext)



        ######### Simulating and Rendering ###########
        ### Steping through object dynamics

        # Delta t
        t = pygame.time.get_ticks()
        # deltaTime in seconds.
        dt = (t - getTicksLastFrame) / 1000.0
        getTicksLastFrame = t


        # Check ground and wall collisions
        ground_collision(ball, dt)

        # Check ball colission with paddle
        if not player_1.check_ball_collision(ball) and not player_2.check_ball_collision(ball) and ball_outside(ball):
            print("LOST")
            show_gameover_screen(WIN)
            ball.x = WINDOW_WIDTH//2
            ball.y = WINDOW_HEIGHT//2
            ball.set_velocity_angle(0)
    
            

        # Steping objects
        for obj in object_list:
            obj.step(dt)


        ### Rendering objects
        WIN.fill(pygame.Color("black"))

        # Rendering balls
        for obj in object_list:
            obj.draw(WIN)

        # Display FPS
        display_fps()

        # Update display
        pygame.display.update()




if __name__ == "__main__":
    main()
    pygame.quit() 