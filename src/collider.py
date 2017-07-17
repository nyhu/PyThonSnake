""" ... """
from src import snake, food
from pygame import font

class Collider(object):
    """docstring for ClassName"""
    def __init__(self, size_max):
        self.decimal_pi = "3@14159265359"
        self.max = size_max
        self.snake = snake.Snake(self)
        self.food = food.Food(self)
        # Food.spawn call collider.is_free who call self.food,
        # So food have to be ready to spawn !
        self.food.spawn()

    def __repr__(self):
        mess = "\nCalling univers inhabitant\n"
        mess += self.snake.__repr__()
        mess += "\n" + self.food.__repr__()
        return mess

    def to_window(self, window, snake_sprite, food_sprite, scale):
        pos_x, pos_y = self.food.get()
        window.blit(food_sprite, (pos_x * scale, pos_y * scale))
        pi_txt = font.Font(None, 24)
        snake = self.snake.get()
        i = 0
        for pos_x, pos_y in reversed(snake):
            print(self.decimal_pi[i:i + 1])
            snake_sprite = pi_txt.render(self.decimal_pi[i:i + 1],1,(0,0,0))
            window.blit(snake_sprite, (pos_x * scale, pos_y * scale))
            i += 1
            if i == len(self.decimal_pi):
                i = 2

    def move(self):
        print(self)
        return self.snake.move()

    def eat(self, pos_x, pos_y):
        """ Serve eatable food as True statement
            if special tuna present at pos_x, pos_y """
        if self.food.eat(pos_x, pos_y):
            return True
        return False

    def is_free(self, pos_x, pos_y):
        """ Tell if nothing present at pos_x, pos_y """
        if self.food.collide(pos_x, pos_y):
            return False
        return self.is_free_from_snake(pos_x, pos_y)

    def is_free_from_snake(self, pos_x, pos_y):
        if self.snake.collide(pos_x, pos_y):
            return False
        return True
