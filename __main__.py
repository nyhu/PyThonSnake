"""
Hearth of the program:
    main class is used to load the snake in accordance with the exec environement
    RUN : python3.6 __main__.py [MAP SIZE]
"""
import sys
import pygame
from src import collider

class PyThonSnake(object):
    """Only compatible with terminal at the moment"""
    def __init__(self):
        self.map = 0

    def init_window(self, argv):
        """ Initialize game in a terminal """
        size_max = 32
        if len(argv) >= 2:
            try:
                width = int(argv[1])
                assert width > 3 and width < 500
            except ValueError:
                pass
            except AssertionError:
                pass
            else:
                size_max = width
        self.map = collider.Collider(size_max)


    def raise_error():
        print("error")

play = PyThonSnake()
if __name__ == "__main__":
    play.init_window(sys.argv)
else:
    play.raise_error()
