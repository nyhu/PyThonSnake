class Snake():
    """Run map for tuna"""
    def __init__(self, map):
        self.map = map
        self.head_x = map.max // 2
        self.head_y = map.max // 2
        self.direction = "North"
        self.tail = [
            (self.head_x, self.head_y + 1),
            (self.head_x, self.head_y + 2),
        ]

    def move(self):
        """ Follow direction to add a head ahead"""
        nextHeadX = self.headX
        nextHeadY = self.headY
        if self.direction == "NORTH":
            nextHeadY -= 1
            if nextHeadY < 0:
                nextHeadY = self.map.max - 1
        elif self.direction == "EAST":
            nextHeadX += 1
            if nextHeadX >= self.map.max:
                nextHeadX = 0
        elif self.direction == "SOUTH":
            nextHeadY += 1
            if nextHeadY >= self.map.max:
                nextHeadY = 0
        elif self.direction == "WEST":
            nextHeadX -= 1
            if nextHeadX < 0:
                nextHeadX = self.map.max - 1
        if self.map.isFree(nextHeadX, nextHeadY):
            return True
        return False

    def goNorth(self):
        """ Key_north """
        self.direction = "NORTH"

    def goEast(self):
        """ key_east """
        self.direction = "EAST"

    def goSouth(self):
        """ key_south """
        self.direction = "SOUTH"

    def goWest(self):
        """ key_west """
        if self.headX - self.tail[0][0]
        self.direction = "WEST"

    def go(self, direction):
        pass
