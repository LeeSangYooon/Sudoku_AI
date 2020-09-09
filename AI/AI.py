from board.board import board
from board.vector2 import vector2
from gui import gui

class AI:
    def __init__(self, current_board):
        self.board = current_board
        self.answer = []

    def get_moves(self, board:board):
        moves = [[0 for j in range(board.size.x)] for i in range(board.size.y)]
        for y in range(board.size.y):
            for x in range(board.size.x):
                if board.board[y][x] == 0:
                    check_list = [
                        [board.board[i][x] for i in range(board.size.y)],
                        [board.board[y][i] for i in range(board.size.x)],
                        []
                    ]
                    for i in range(3):
                        for j in range(3):
                            check_list[2].append(board.board[y-y%3+j][x-x%3+i])

                    numbers = []
                    for number in range(1, board.size.x + 1):
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

    def search_node(self, node_board:board, depth, gui:gui):
        gui.draw()
        moves = self.get_moves(node_board)
        move_lengths = []
        for x in range(node_board.size.x):
            for y in range(node_board.size.y):
                if len(moves[y][x]) != 0:
                    move_lengths.append([len(moves[y][x]),moves[y][x], x, y])
        move_lengths = sorted(move_lengths)

        if sum([[node_board.board[i][j] for j in range(node_board.size.x)].count(0) for i in range(node_board.size.y)]) > len(move_lengths):
            return False

        if len(move_lengths) == 0:
            if node_board.solved():
                return True
            return False

        for i in range(len(move_lengths)):
            pos = vector2(move_lengths[i][2], move_lengths[i][3])

            for j in range(len(move_lengths[i][1])):
                node_board.move(pos, move_lengths[i][1][j])
                result = self.search_node(node_board, depth + 1, gui)
                if result:    # 성공했으면
                    self.answer.append((pos, move_lengths[i][1][j]))
                    return True

            node_board.move(pos, 0)


    def solve(self, gui:gui):
        self.search_node(self.board,0, gui)


