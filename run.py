"""
Hearth of the program:
    main class is used to load the snake in accordance with the exec environement
    RUN : python3.6 __main__.py [MAP SIZE]
"""
import sys
import pygame
from pygame.locals import *
from src import collider


class PyThonSnake(object):
    """Only compatible with terminal at the moment"""
    def __init__(self):
        self.map = 0

    def init_map(self, str):
        size_max = 32
        try:
            width = int(str)
            assert width > 3 and width < 500
        except ValueError:
            pass
        except AssertionError:
            pass
        else:
            size_max = width
        self.map = collider.Collider(size_max)

    def init_window(self, argv):
        """ Initialize game in a terminal """

        if (len(argv) == 2):
            self.init_map(argv[1])
        else:
            self.init_map("")
        pygame.init()
        window = pygame.display.set_mode((500, 500))
        scale = 500 // self.map.max
        background = pygame.image.load("background.jpg").convert()
        background = pygame.transform.scale(background, (500, 500))
        snake_sprite = pygame.image.load("snake_sprite.png").convert()
        snake_sprite = pygame.transform.scale(snake_sprite, (scale, scale))
        food_sprite = pygame.image.load("food_sprite.png").convert()
        food_sprite = pygame.transform.scale(food_sprite, (scale, scale))
        working = 1
        while working:
            window.blit(background, (0, 0))
            if not self.map.move():
                print("YOU LOOOOSE !!!")
                working = 0
            self.map.to_window(window, snake_sprite, food_sprite, scale)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    working = 0
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        working = 0
                    elif event.key == K_UP:
                        self.map.snake.go_north()
                        print("going up")
                    elif event.key == K_RIGHT:
                        self.map.snake.go_east()
                    elif event.key == K_DOWN:
                        self.map.snake.go_south()
                    elif event.key == K_LEFT:
                        self.map.snake.go_west()
            pygame.time.delay(150)

    def raise_error(self):
        print("error")

play = PyThonSnake()
if __name__ == "__main__":
    play.init_window(sys.argv)
else:
    play.raise_error()
