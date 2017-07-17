import random


class Food():
    """Use to tell food stories when talked to"""
    def __init__(self, map):
        """declare variables"""
        self.posX = 0
        self.posY = 0
        self.map = map
        self.size = map.max
        self.spawn()

    def spawn(self):
        """ Generate food """
        while 42:
            self.posX = random.randrange(self.size)
            self.posY = random.randrange(self.size)
            if self.map.isFree(self.posX, self.posY):
                break

    def tell(self):
        """tell where food is"""
        return self.posX, self.posY

    def eat(self, pos_x, pos_y):
        """ take pos_x and pos_y from targeting eater
            tell if where eaten, if so, create more food """
        if pos_x == self.posX and pos_y == self.posY:
            self.spawn()
            return True
        return False
