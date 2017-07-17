import random

class Food():
    """Use to tell food stories when talked to"""
    def __init__(self, map):
        """declare variables"""
        self.pos_x = 0
        self.pos_y = 0
        self.map = map
        self.size = map.max
        self.spawn()

    def spawn(self):
        """ Generate food """
        while 42:
            new_pos_x = random.randrange(self.size)
            new_pos_y = random.randrange(self.size)
            if self.map.is_free(new_pos_x, new_pos_y):
                self.pos_x = new_pos_x
                self.pos_y = new_pos_y
                break

    def collide(self, pos_x, pos_y):
        """tell where food is"""
        if self.pos_x == pos_x and self.pos_y == pos_y:
            return True
        return False

    def eat(self, pos_x, pos_y):
        """ take pos_x and pos_y from targeting eater
            tell if where eaten, if so, create more food """
        if pos_x == self.pos_x and pos_y == self.pos_y:
            self.spawn()
            return True
        return False
