import pygame
import settings.setting as setting
from settings.setting import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from settings.logger import get_logger
import level

logger: setting.Logger = get_logger()
logger.info(f"text_font_dir:{setting.TEXT_FONT}")
logger.info(f"cheat_ball_follow:{setting.cheat.BALL_FOLLOW_MOUSE}")
logger.info(f"cheat_spawn_element:{setting.cheat.SPAWN_ELEMENT}")

pygame.init()
screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Brick Breaker")

level.main_init()

logger.info("Enter game")
clock = pygame.time.Clock()
while level.is_running():
    level.update_level(screen)
    
    clock.tick(FPS)
logger.info("Quit game")

pygame.quit()