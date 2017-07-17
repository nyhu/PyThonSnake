import snake
import food


class Map():
    """docstring for ClassName"""
    def __init__(self, max):
        self.snake = snake.Snake(self)
        self.max = max
        self.food = food.Food(self)

    def eat(self, pos_x, pos_y):
        if self.food.eat(pos_x, pos_y):
            return True
        return False
