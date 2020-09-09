from board.vector2 import vector2
import numpy as np
class board:
    def __init__(self, size):
        self.size = size # vector2
        self.board = np.zeros(size.x * size.y, dtype=int).reshape(size.y, size.x)  # 0: 모름

    def move(self, pos:vector2, to):
        self.board[pos.y][pos.x] = to

    def solved(self):
        for horizontal in self.board:
            if list(sorted(horizontal)) != list(range(1, self.size.x + 1)):
                return False
        for vertical in [[self.board[i][j] for i in range(self.size.x)] for j in range(self.size.y)]:
            if list(sorted(vertical)) != list(range(1, self.size.y + 1)):
                return False

        three_list =[i*3 for i in range(int(self.size.y / 3))]
        for x,y in zip(three_list, three_list):
            box = []
            for i in range(3):
                for j in range(3):
                    box.append(self.board[y+i][x+j])
            if list(sorted(box)) != list(range(1, 10)):
                return False

        return True