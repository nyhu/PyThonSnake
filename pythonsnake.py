"""
Hearth of the programm:
    main class is used to load the snake in accordance with the exec environement
    it takes:
        size_x
        size_y
"""
import sys
from gameplay import map


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
        self.map = map.Map(max)

if __name__ == "__main__":
    main = pythonsnake.PyThonSnake()
   	main.init_term(sys.argv)
