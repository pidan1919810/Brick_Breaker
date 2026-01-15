from typing import List
import pygame
from pygame.event import Event
from level_objects.base_object import Base_object, Base_manager
from settings.setting import *
from level_objects.ball import ball_manager, Normal_ball
from level_objects.board import board
from level_objects.brick import brick_manager, Brick
from level_objects.button import Button
from easy_types import *

class Scene_manger(Base_manager[Base_manager|Base_manager]):
    def __init__(self) -> None:
        super().__init__()
        #self.level = 
        
    def switch_scene(self):
        ...
    
in_level:bool

restart_button:Button
running:bool = True
objects:list = []
score:int = 0

def level_init(infinite:bool) -> None:
    global score, objects, restart_button, in_level
    score = 0
    in_level = True
    
    brick_manager.clear()
    brick_manager.init()
    brick_manager.set_mode(infinite)
    
    ball_manager.clear()
    ball_manager.init()
    
    objects.clear()
    objects.append(brick_manager)
    
    ball_manager.clear()
    objects.append(ball_manager)
    ball_manager.extend(Normal_ball, (300, BOARD_Y-40))
    
    objects.append(board)
    
    restart_button = Button(225,400,150,50,"再来一次")
    restart_button.add_event(level_init,infinite)
    
    from settings.logger import get_logger
    logger = get_logger()
    
    logger.info(f"infinite mode:{infinite}")

finite_level_button:Button
infinite_level_button:Button

def main_init() -> None:
    global in_level,finite_level_button,infinite_level_button
    in_level = False
    finite_level_button = Button(20,20,60,60,'有限')
    finite_level_button.add_event(level_init, False)
    infinite_level_button = Button(100,20,60,60,'无限')
    infinite_level_button.add_event(level_init, True)

def is_running() -> bool:
    global running
    return running

def is_in_level() -> bool:
    global in_level
    return in_level

def add_score(addend:int) -> None:
    global score
    score += addend

def in_game(screen:pygame.Surface, events:list[pygame.event.Event]) -> None:
    for object in objects:
        object.update(events)
        
    for object in objects:
        object.draw(screen)
        
    fonts = pygame.font.Font(TEXT_FONT, IN_GAME_TEXT_SIZE)
    text = fonts.render(f"Score:{score}", False, (128,128,128))
    screen.blit(text,(0,0))

def in_main_screen(screen:Surface) -> None:
    infinite_level_button.draw(screen)
    finite_level_button.draw(screen)
    

def failed_screen(screen:pygame.Surface) -> None:
    for object in objects:
        object.draw(screen)

    fonts = pygame.font.Font(TEXT_FONT, FAILED_TEXT_SIZE)
    text: pygame.Surface = fonts.render("你输了", False, (128,128,128))
    screen.blit(text,(200,350))
    
    restart_button.draw(screen)


def won_screen(screen:pygame.Surface) -> None:
    for object in objects:
        object.draw(screen)

    fonts = pygame.font.Font(TEXT_FONT, WON_TEXT_SIZE)
    text: pygame.Surface = fonts.render("你赢了", False, (128,128,128))
    screen.blit(text,(200,350))
    
    restart_button.draw(screen)


def is_fail() -> bool:
    #return True
    if ball_manager.get_cout() < 1:
        return True
    else:
        return False
    
def is_win() -> bool:
    if brick_manager.get_brick_cout() <= 0:
        return True
    else:
        return False

def update_level(screen:pygame.Surface) -> None:
    global running
    events: L_events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
                if cheat.SPAWN_ELEMENT:
                    if event.key == pygame.K_l:
                        brick_manager.new_line()
                        
    screen.fill((0, 0, 0))
    if is_in_level():
        if is_fail():
            restart_button.update(events)
            failed_screen(screen)
        elif is_win():
            restart_button.update(events)
            won_screen(screen)
        else:
            in_game(screen, events)
    else:
        finite_level_button.update(events)
        infinite_level_button.update(events)
        in_main_screen(screen)
    pygame.display.flip()