def create_chess_board():
    helper: str = "abcdefgh"
    board = []
    for row in range(0, 8):
        for col in range(8,0,-1):
            board.append((
                helper[row] + str(col), "", ""
            ))
    return board

def set_up_start_position(board):
    # Weiße Figuren (unten auf dem Brett)
    white_pawn_pos = ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"]
    white_rook_pos = ["a1", "h1"]
    white_knight_pos = ["b1", "g1"]
    white_bishop_pos = ["c1", "f1"]
    white_queen_pos = ["d1"]
    white_king_pos = ["e1"]

    # Schwarze Figuren (oben auf dem Brett)
    black_pawn_pos = ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"]
    black_rook_pos = ["a8", "h8"]
    black_knight_pos = ["b8", "g8"]
    black_bishop_pos = ["c8", "f8"]
    black_queen_pos = ["d8"]
    black_king_pos = ["e8"]

    for field in board:
        # black pawns
        if field[0] == 7:
            field[1] = "pawn"
            field[2] = "black"

        # white pawns
        if field[0] == 2:
            field[1] = "pawn"
            field[2] = "white"


if __name__ == '__main__':
    chessboard = create_chess_board()
    set_up_start_position(chessboard)