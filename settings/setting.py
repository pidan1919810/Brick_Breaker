from logging import Logger
import settings.cheat as cheat

#界面相关
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

FPS = 30

import sys
import os

def resource_path(relative_path: str) -> str:
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS  # type: ignore
    else:
        base_path = os.path.dirname(os.path.abspath('Brick_Breaker'))

    #规范化路径
    return os.path.normpath(os.path.join(base_path, relative_path))
    

TEXT_FONT: str = resource_path("assets/font/ZiTiGuanJiaFangSongTi-2.ttf")

#失败界面
FAILED_TEXT_SIZE = 30

#游戏中
IN_GAME_TEXT_SIZE = 25
INSTRUCTION_LINE_LENGTH = 50

EFFECT_BALL_GENRATE_PERCENTAGE = 0.06

#胜利界面
WON_TEXT_SIZE = 25

#元素相关
BALL_SPEED = 10
BALL_NUMBER_LIMIT = 100

BOARD_LENGTH = 150
BOARD_MOVEING_SPEED = 10
BOARD_Y = 600

BRICK_SIZE = 40
LINES_OF_BRICKS = 7


