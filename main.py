from gui.gui import gui
from board.board import board
from board.vector2 import vector2
from AI.AI import AI

board = board(vector2(9, 9))

gui = gui()
gui.gui_init()
gui.board = board
while not gui.done:
    event = gui.main_loop()