from .base_object import Base_object
from easy_types import *
from typing import Literal
import pygame

class Text(Base_object):
    """
        文字组件
    """
    def __init__(self, x: float, y: float, w:float, h:float, text:str) -> None:
        super().__init__(x,y)
        self.text:str = text
        self.w:float = w
        self.h:float = h
        self.x_dis_mode:str = 'middle'
        self.y_dis_mode:str = 'middle'
        self.line_spacing: int = 2
        
    def set_display_mode(
                            self, 
                            x_mode:Literal['middle'] | Literal['left'] | Literal['right'] = 'middle',
                            y_mode:Literal['middle'] | Literal['up'] | Literal['down'] = 'middle'
                        ) -> None:
        self.x_dis_mode = x_mode
        self.y_dis_mode = y_mode
        
    def set_line_spacing(self, spacing:int) -> None:
        self.line_spacing: int = spacing
    
    def draw(self, screen: pygame.Surface) -> None:
        if not self.text:
            return

        from settings.setting import TEXT_FONT
        font = pygame.font.Font(TEXT_FONT, 22)

        # 1. 自动换行
        max_width = self.w
        lines: list[str] = []
        current = ""

        for char in self.text:
            test = current + char
            if font.size(test)[0] <= max_width:
                current = test
            else:
                lines.append(current)
                current = char
        if current:
            lines.append(current)

        # 2. 行高（关键）
        line_height = font.get_linesize()
        total_height = (
            line_height * len(lines)
            + self.line_spacing * (len(lines) - 1)
        )

        # 3. 计算起始 y
        if self.y_dis_mode == "middle":
            start_y = self.y + (self.h - total_height) / 2
        elif self.y_dis_mode == "up":
            start_y = self.y
        elif self.y_dis_mode == "down":
            start_y = self.y + self.h - total_height
        else:
            start_y = self.y

        y = start_y

        # 4. 绘制每一行
        for line in lines:
            surf = font.render(line, True, (0, 0, 0))
            rect = surf.get_rect()

            if self.x_dis_mode == "middle":
                rect.centerx = int(self.x + self.w / 2)
            elif self.x_dis_mode == "left":
                rect.left = int(self.x)
            elif self.x_dis_mode == "right":
                rect.right = int(self.x + self.w)
            else:
                rect.left = int(self.x)

            rect.top = int(y)
            screen.blit(surf, rect)

            y += line_height + self.line_spacing

    def update(self, events: L_events) -> None:
        return super().update(events)