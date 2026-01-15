import pygame

class Timer:
    def __init__(self, interval_ms: int) -> None:
        self.interval = interval_ms
        self.last_time = pygame.time.get_ticks()

    def ready(self) -> bool:
        now = pygame.time.get_ticks()
        if now - self.last_time >= self.interval:
            self.last_time = now
            return True
        return False
