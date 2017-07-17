""" ... """
from src import snake, food

class Collider():
    """docstring for ClassName"""
    def __init__(self, size_max):
        self.max = size_max
        self.snake = snake.Snake(self)
        self.food = food.Food(self)
        # Food.spawn call collider.is_free who call self.food,
        # So food have to be ready to spawn !
        self.food.spawn()

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
        if self.snake.collide(pos_x, pos_y):
            return False
        return True
