import pygame
from pygame.event import Event
from enum import Enum

class Button:
    
    def additional_behaviour(self, input_context, context):
        pass
    
    def __init__(self, x, y, w, h,  
    additional_function = None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.limits = ((x, x + w),(y, y + h))
        self.caption = ""

        self.font_color = pygame.Color("black")
        self.font_size = 30

        self.background_color = pygame.Color("grey")

        self.background_color_2 = pygame.Color("green")
        self.border_width = 0
        self.border_radius = -1

        self.state = False

        if additional_function != None:
            self.additional_behaviour = additional_function
 
  
    def draw(self, win):
        # Draw button
        button_rect = pygame.Rect(self.x, self.y, self.w, self.h)
        b_color = self.background_color if self.state else self.background_color_2
        pygame.draw.rect(win, b_color, button_rect, self.border_width, border_radius=self.border_radius)
        
        # Draw caption
        font = pygame.font.Font(None, self.font_size)
        text = font.render(self.caption, True, self.font_color)
        rect_text = text.get_rect(center=(self.x + self.w // 2, self.y + self.h // 2))
        win.blit(text, rect_text)

    def interact(self, input_context : tuple, context):
        """ Interface function - children of this class will define their own """

        return self.additional_behaviour(input_context, context)


    def check_press(self, input_context, context) -> None:
        
        # Check if the the left mouse button is pressed
        events = input_context[0]
        mouse_coord = input_context[1].get_pos()

        click_event = False
        for event in events:
            print(event.type)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click_event = True
        if not click_event:
            return
        
        print("Checking location")
        # Check if mouse is inside hitbox
        if mouse_coord[0] > self.limits[0][0] and \
           mouse_coord[0] < self.limits[0][1] and \
           mouse_coord[1] > self.limits[1][0] and \
           mouse_coord[1] < self.limits[1][1]:
            return self.interact(input_context, context)

        

class StateMachineButton(Button):

    def interact(self, input_context: tuple, context):
        
        self.state = not self.state

        return self.additional_behaviour(input_context, context)

class Hover_Button:
    
    def additional_behaviour(self, input_context, context):
        pass
    
    def __init__(self, x, y, w, h,  
    additional_function = None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.limits = ((x, x + w),(y, y + h))
        self.caption = ""

        self.font_color = pygame.Color("black")
        self.font_size = 30

        self.background_color = pygame.Color("white")

        self.background_color_2 = pygame.Color("green")
        self.border_width = 3
        self.border_radius = 4

        self.state = False
        self.hovering = False

        if additional_function != None:
            self.additional_behaviour = additional_function
 
  
    def draw(self, win):
        # Draw button
        button_rect = pygame.Rect(self.x, self.y, self.w, self.h)
        if self.state:
            b_color = self.background_color
        elif self.hovering:
            b_color = pygame.Color("grey")
        else:
            b_color = self.background_color_2

        pygame.draw.rect(win, b_color, button_rect, self.border_width, border_radius=self.border_radius)
        
        # Draw caption
        font = pygame.font.Font(None, self.font_size)
        text = font.render(self.caption, True, self.font_color)
        rect_text = text.get_rect(center=(self.x + self.w // 2, self.y + self.h // 2))
        win.blit(text, rect_text)

    def interact(self, input_context : tuple, context):
        """ Interface function - children of this class will define their own """
        self.state = not self.state
        return self.additional_behaviour(input_context, context)


    def step(self, input_context, context) -> None:
        
        # Check if the the left mouse button is pressed
        events = input_context[0]
        mouse_coord = input_context[1].get_pos()

        hovering = False
        click_event = False

        if mouse_coord[0] > self.limits[0][0] and \
           mouse_coord[0] < self.limits[0][1] and \
           mouse_coord[1] > self.limits[1][0] and \
           mouse_coord[1] < self.limits[1][1]:
            self.hovering = True
        else:
            self.hovering = False

        for event in events:
            print(event.type)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click_event = True
        if click_event:
            return self.interact(input_context, context)




# class WorkspaceButton(Button):

#     def interact(self, mouse_coord: tuple, event: Event, context: ProgramContext):
        
#         return self.additional_behaviour(mouse_coord, event, context)
        
#         if not self.state:
#             if dot_list:
#                 print("remove")
#                 dot = get_closest_dot(mouse)
#                 remove_dot(dot)
#                 continue
            
#             if color_select_button.state:
#                 add_dot(mouse, "red")

#             if not color_select_button.state:
#                 add_dot(mouse, "green")

