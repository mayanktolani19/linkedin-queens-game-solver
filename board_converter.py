import numpy as np
import math

class board_converter:
    def __init__(self, queens):
        self.queens = queens

    def convertHtmlBoardToArray(self):
        queens_cells = self.queens.find_all("div", class_="queens-cell")

        n_cells = len(queens_cells)

        # Find the shape of the board
        board_size = math.sqrt(n_cells)
        shape = (int(board_size), int(board_size))
        board = np.zeros(shape)
        
        board = []
        for cell in queens_cells:
            color = cell["class"][1].split("-")[2]
            board.append(int(color))
        return np.asarray(board).reshape(shape)
