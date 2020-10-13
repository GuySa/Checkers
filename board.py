import Tkinter

BOARD_WIDTH = 400
BOARD_HEIGHT = 400

CELL_COLORS= ["#c8c8c8", "#966400"]

def onClick(event):
    print("meow")

class Board(Tkinter.Frame):
    def __init__(self, master):
        Tkinter.Frame.__init__(self, width=BOARD_WIDTH, height=BOARD_HEIGHT)

        # Drawing 10 by 10 board
        backgroundCanvas = Tkinter.Canvas(self, width=BOARD_WIDTH, height=BOARD_HEIGHT)
        backgroundCanvas.pack()
        
        for i in range(10):
            for j in range(10):
                backgroundCanvas.create_rectangle(  i*(BOARD_WIDTH/10), j*(BOARD_HEIGHT/10),
                                                    (i+1)*(BOARD_WIDTH/10), (j+1)*(BOARD_HEIGHT)/10,
                                                    fill=CELL_COLORS[(i+j)%2])

                currentPiece = Tkinter.Canvas(backgroundCanvas)
                currentPiece.grid(row=i, column=j)
                currentPiece.bind("<ButtonPress-1>", onClick)

        # Setting pieces 
