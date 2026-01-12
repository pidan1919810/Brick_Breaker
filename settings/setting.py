import settings.cheat as cheat
#界面相关
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

FPS = 30

import sys
import os

import os
import sys

def resource_path(path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, path)  # type: ignore
    return os.path.join(os.path.abspath("."), path)


TEXT_FONT: str = resource_path("assets/font/ZiTiGuanJiaFangSongTi-2.ttf")

#失败界面
FAILED_TEXT_SIZE = 30

#游戏中
IN_GAME_TEXT_SIZE = 25
INSTRUCTION_LINE_LENGTH = 50

EFFECT_BALL_GENRATE_PERCENTAGE = 0.1

#胜利界面
WON_TEXT_SIZE = 25

#元素相关
BALL_SPEED = 10
BALL_NUMBER_LIMIT = 20

BOARD_LENGTH = 150
BOARD_MOVEING_SPEED = 10
BOARD_Y = 600

BRICK_SIZE = 20
LINES_OF_BRICKS = 10

#游戏模式
INFINITE_MODE = True


