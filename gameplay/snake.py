class Snake():
    """Run map for tuna"""
    def __init__(self, map):
        self.map = map
        self.head_x = map.max // 2
        self.head_y = map.max // 2
        self.direction = "NORTH"
        self.previous = "SOUTH"
        self.tail = [
            (self.head_x, self.head_y + 2),
            (self.head_x, self.head_y + 1),
        ]

    def collide(self, pos_x, pos_y):
        """ Tell if collide at pos_x, pos_y """
        # Check collision on head
        if self.head_x == pos_x and self.head_y == pos_y:
            return True
        # Check collision along the tail
        for pox, poy in self.tail:
            if pox == pos_x and poy == pos_y:
                return True
        return False

    def move(self):
        """ Follow direction
            Ask for food ahead, if not, delete a tail at the bottom
            Ask for collision ahead,
                if not, add a head ahead
                else return False and wait for death"""
        # ADD HEAD : initialize position for next head
        next_head_x = self.head_x
        next_head_y = self.head_y
        if self.direction == "NORTH":
            next_head_y -= 1
            if next_head_y < 0:
                next_head_y = self.map.max - 1
        elif self.direction == "EAST":
            next_head_x += 1
            if next_head_x >= self.map.max:
                next_head_x = 0
        elif self.direction == "SOUTH":
            next_head_y += 1
            if next_head_y >= self.map.max:
                next_head_y = 0
        elif self.direction == "WEST":
            next_head_x -= 1
            if next_head_x < 0:
                next_head_x = self.map.max - 1
        if not self.map.eat(next_head_x, next_head_y):      # If no food ahead
            del self.tail[0]                                # We delete tail
        if self.map.isfree(next_head_x, next_head_y):
            self.tail.append((self.head_x, self.head_y))
            self.head_x = next_head_x
            self.head_y = next_head_y
            # IDEA: set orientation previous
            return True
        return False

    def go_north(self):
        """ Key_north """
        if self.previous != "NORTH":
            self.direction = "NORTH"

    def go_east(self):
        """ key_east """
        if self.previous != "EAST":
            self.direction = "EAST"

    def go_south(self):
        """ key_south """
        if self.previous != "SOUTH":
            self.direction = "SOUTH"

    def go_west(self):
        """ key_west """
        if self.previous != "WEST":
            self.direction = "WEST"
