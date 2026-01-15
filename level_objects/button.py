import pygame, enum, types
from .base_object import Base_object
from easy_types import *

class Button(Base_object):
    class Status(enum.Enum):
        normal = 1
        enter = 2
        clicked = 3
    
    def __init__(
        self, 
        x:float, 
        y:float, 
        w:float, 
        h:float, 
        text:str = '', 
        on_or_off=True
    ) -> None:
        
        super().__init__(x,y)
        self.w: float = w
        self.h: float = h
        
        self.status = self.Status.normal
        
        from .text import Text
        self.text = Text(self.x, self.y, self.w, self.h, text)
        self.on_or_off = on_or_off #Call the events when click on(True) or after click on
        self.click_on = False
        
        self.args = ()
        
    def get_rect(self) -> Rect:
        return Rect(self.x, self.y, self.w, self.h)
        
    def add_event(self, event:types.FunctionType, *args) -> None:
        self.event: types.FunctionType = event
        self.args = args
        
    def is_enter(self, x, y) -> bool:
        return x > self.x and x < self.x+self.w and y > self.y and y < self.y + self.h
    
    def is_click(self, event:pygame.event.Event) -> bool:
        return event.type == pygame.MOUSEBUTTONDOWN
                    
    def draw(self, screen:pygame.Surface) -> None:
        if self.status == self.Status.enter:
            screen.fill(pygame.color.Color(255,100,0), self.get_rect())
        else:
            screen.fill("white", self.get_rect())
            
        self.text.draw(screen)
        
    def update(self, events:list[pygame.event.Event]) -> None:
        for event in events:
            self.status = self.Status.normal
            mouse_x, mouse_y = pygame.mouse.get_pos()
            #print(self.status)
            if self.on_or_off:
                if self.is_enter(mouse_x, mouse_y):
                    self.status = self.Status.enter
                    if self.is_click(event):
                        self.status = self.Status.clicked
                        self.on_click()
            else:
                if self.is_enter(mouse_x, mouse_y):
                    self.status = self.Status.enter
                    if self.is_click(event):
                        self.click_on = True
                    if not self.is_click(event) and self.click_on:
                        self.click_on = False
                        self.status = self.Status.clicked
                        self.on_click()
                else:
                    self.click_on = False

    def on_click(self) -> None:
        self.event(*self.args)
        