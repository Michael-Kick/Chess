from array import ArrayType
from operator import index


def print_chess_board(board):
    row: str = ""
    counter: int = 1
    for position,piece in board.items():
        if counter % 8 == 0:
            print(row)
            row = ""
        else:
            row = row + "|" + str(position) + str(piece)
        counter = counter + 1


def create_chess_board():
    helper: str = "abcdefgh"
    board = {}
    for col in range(8, 0, -1):
        for row in range(0, 8):
            board[helper[row] + str(col)] = ("", "")
    return board


def set_up_start_position(board):
    chess_pieces = [
        (["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"], "pawn", "white"),
        (["a1", "h1"], "rook", "white"),
        (["b1", "g1"], "knight", "white"),
        (["c1", "f1"], "bishop", "white"),
        (["d1"], "queen", "white"),
        (["e1"], "king", "white"),

        (["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"], "pawn", "black"),
        (["a8", "h8"], "rook", "black"),
        (["b8", "g8"], "knight", "black"),
        (["c8", "f8"], "bishop", "black"),
        (["d8"], "queen", "black"),
        (["e8"], "king", "black")
    ]

    for positions, piece, colour in chess_pieces:
        for position in positions:
            board[position] = (piece, colour)

    print_chess_board(board)


if __name__ == '__main__':
    chessboard = create_chess_board()
    set_up_start_position(chessboard)
