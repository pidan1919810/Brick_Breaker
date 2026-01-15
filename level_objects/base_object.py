import pygame
from easy_types import *
from pygame.event import Event
from typing import Self, Any, Generic, TypeVar
from abc import ABC, abstractmethod



class Base_object(ABC):
    """
        定义了所有的物体基类
    """
    x:float
    y:float
    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y
    
    @abstractmethod
    def draw(self, screen:Surface) -> None:
        pass
    
    @abstractmethod
    def update(self, events:L_events) -> None:
        pass
    
    @classmethod
    def create(cls, x:float, y:float) -> Self:
        return cls(x,y)
    
    def get_x(self) -> float:
        return self.x
    def get_y(self) -> float:
        return self.y
    def get_pos(self) -> Vector2:
        return pygame.Vector2(self.x, self.y)
    
T = TypeVar("T")
    
class Base_manager(Generic[T], ABC):
    objects:list[T]
    object_count:int
    
    def __init__(self) -> None:
        self.init()
    
    def init(self) -> None:
        self.object_count = 0
        self.objects.clear()
    
    def extend( 
            self, 
            cls:type[T], 
            **args:tuple[float, float] | Vector2
        ) -> bool:
        for pos in args:
            self.object_count += 1
            self.objects.append(cls.create(pos[0], pos[1]))  # type: ignore
        return True
    
    def update(self, events) -> None:
        for object in self.objects:
            object.update(events)  # type: ignore
            
    def draw(self, screen:Surface) -> None:
        for object in self.objects:
            object.draw(screen)  # type: ignore
            
    def delete_item(self, object:T) -> None:
        self.object_count -= 1
        self.objects.remove(object)
        
    def get_cout(self) -> int:
        return self.object_count
    
class Base_image(Base_object, ABC):
    """
        包含了渲染图片的的逻辑
        未实现
    """