import snake
import food


class Map():
    """docstring for ClassName"""
    def __init__(self, max):
        self.snake = snake.Snake()
        self.max = max
        self.food = food.Food(self)
