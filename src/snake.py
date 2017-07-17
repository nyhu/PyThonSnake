class Snake(object):
    """Run map for tuna"""
    def __init__(self, collider):
        self.map = collider
        self.head_x = collider.max // 2
        self.head_y = collider.max // 2
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

    def _get_a_head_ahead(self, direction):
        next_head_x = self.head_x
        next_head_y = self.head_y
        if direction == "NORTH":
            next_head_y -= 1
            if next_head_y < 0:
                next_head_y = self.map.max - 1
        elif direction == "EAST":
            next_head_x += 1
            if next_head_x >= self.map.max:
                next_head_x = 0
        elif direction == "SOUTH":
            next_head_y += 1
            if next_head_y >= self.map.max:
                next_head_y = 0
        elif direction == "WEST":
            next_head_x -= 1
            if next_head_x < 0:
                next_head_x = self.map.max - 1
        return next_head_x, next_head_y

    def move(self):
        """ Follow direction
            Ask for food ahead, if not, delete a tail at the bottom
            Ask for collision ahead,
                if not, add a head ahead
                else return False and wait for death"""
        # ADD HEAD : initialize position for next head
        next_head_x, next_head_y = self._get_a_head_ahead(self.direction)
        # If no food ahead
        if not self.map.eat(next_head_x, next_head_y):
            # We delete tail
            del self.tail[0]
        # If we can go ahead
        if self.map.is_free(next_head_x, next_head_y):
            # We append current head to tail
            self.tail.append((self.head_x, self.head_y))
            # And set our head on precalculated one
            self.head_x = next_head_x
            self.head_y = next_head_y
            return True
        return False

    def go_north(self):
        """ Key_north """
        if self.map.is_free(self._get_a_head_ahead("NORTH")):
            self.direction = "NORTH"

    def go_east(self):
        """ key_east """
        if self.map.is_free(self._get_a_head_ahead("EAST")):
            self.direction = "EAST"

    def go_south(self):
        """ key_south """
        if self.map.is_free(self._get_a_head_ahead("SOUTH")):
            self.direction = "SOUTH"

    def go_west(self):
        """ key_west """
        if self.map.is_free(self._get_a_head_ahead("WEST")):
            self.direction = "WEST"
