from run import *


def test_map():
	play = PyThonSnake()
	play.init_window(["", ""])
	assert play.map.max == 32
