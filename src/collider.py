""" ... """
from src import snake, food

class Collider(object):
    """docstring for ClassName"""
    def __init__(self, size_max):
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
        for pos_x, pos_y in self.snake.get():
            window.blit(snake_sprite, (pos_x * scale, pos_y * scale))

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

    def colide(self, pos_x, pos_y):
        """ Give the collision type """
        if self.food.collide(pos_x, pos_y):
            return 'FOOD'
        elif self.snake.collide(pos_x, pos_y):
            return 'SNAKE'
        return None
