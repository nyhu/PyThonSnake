"""
Hearth of the programm:
    main class is used to load the snake in accordance with the exec environement
    it takes:
        size_x
        size_y
"""
import gameplay
import graphic

class Map():
    """docstring for ClassName"""
    def __init__(self, max):
        self.snake = gameplay.Snake()
        self.max = max
        self.food = gameplay.Food(self)



class PyThonSnake():
    """Only compatible with terminal at the moment"""
    def __init__(self):
        pass

    def init_term(self, argv):
        max = 32
        if len(argv) == 2:
            try:
                x = int(argv[1])
                assert(x > 3 and x < 500)
            except ValueError:
                pass
            except AssertionError:
                pass
            else:
                max = x
        self.map = Map(max)
