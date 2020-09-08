from board.board import board

class AI:
    def __init__(self, current_board):
        self.board = current_board

    def get_moves(self):
        moves = [[0 for j in range(self.board.size.x)] for i in range(self.board.size.y)]
        for y in range(self.board.size.y):
            for x in range(self.board.size.x):
                if self.board.board[y][x] == 0:
                    check_list = [
                        [self.board.board[i][x] for i in range(self.board.size.y)],
                        [self.board.board[y][i] for i in range(self.board.size.x)],
                        []
                    ]
                    for i in range(3):
                        for j in range(3):
                            check_list[2].append(self.board.board[y-y%3+j][x-x%3+i])

                    numbers = []
                    for number in range(1, self.board.size.x + 1):
                        canMove = True
                        for check in check_list:
                            if number in check:
                                canMove = False
                                break
                        if canMove:
                            numbers.append(number)

                    moves[y][x] = numbers
                else:
                    moves[y][x] = []
        return moves

