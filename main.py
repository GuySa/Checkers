import Tkinter
from board import Board

root = Tkinter.Tk()

board = Board(root)
board.pack()

root.mainloop()
