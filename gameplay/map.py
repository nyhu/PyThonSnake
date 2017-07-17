""" ... """
import snake
import food

class Map():
    """docstring for ClassName"""
    def __init__(self, max):
        self.max = max
        self.snake = snake.Snake(self)
        self.food = food.Food(self)

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
