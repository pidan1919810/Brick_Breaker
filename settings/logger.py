#日志
from logging import Logger


def get_logger() -> Logger:
    import logging

    logging.basicConfig(
        level=logging.INFO,
        filename="game.log",
        filemode="a",
        format="%(asctime)s [%(levelname)s] %(message)s"
    )
    
    return logging.getLogger()