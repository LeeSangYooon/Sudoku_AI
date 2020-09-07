from board.board import board

class AI:
    def __init__(self, current_board):
        self.board = current_board

    def get_moves(self):
        for y in range(self.board.size.y):
            for x in range(self.board.size.x):
                check_list = [
                    [(x, i) for i in range(self.board.size.y)],
                    [(i, y) for i in range(self.board.size.x)],
                    []
                ]
                for i in range(3):
                    for j in range(3):
                        check_list[3].append((x+i%3, y+j%3))