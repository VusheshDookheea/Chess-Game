import numpy as np
class ChessBoard:
    cn = 0 # track of moves

    def __init__(self):
        self.board = self.make_board()

    def __str__(self):
        s = ''
        board = self.sketch_board(self.board.T) # Transpose is necessary to make the board as we are accustomed to
        for i in reversed(range(8)): s += str(board[i])  + '\n'
        return s

    def make_board(self): # Forms the board and puts the pieces on the respective positions

        board = np.zeros((8,8), dtype = object)
        # black pieces
        BlackRook1 = Rook(0, 7, 'b', board)
        BlackRook2 = Rook(7, 7, 'b', board)
        BlackKnight1 = Knight(1, 7, 'b', board)
        BlackKnight2 = Knight(6, 7, 'b', board)
        BlackBishop1 = Bishop(2, 7, 'b', board)
        BlackBishop2 = Bishop(5, 7, 'b', board)
        BlackQueen = Queen(3, 7, 'b', board)
        BlackKing = King(4, 7, 'b', board)
        # Now we should put the pawns
        for i in range(8):
            exec("BPawn" + str(i+1)  + "= Pawn(i, 6, 'b', board)")


        # Now we should put the pieces on the board
        WhiteRook1 = Rook(0, 0, 'w', board)
        WhiteRook2 = Rook(7, 0, 'w', board)
        WhiteKnight1 = Knight(1, 0, 'w', board)
        WhiteKnight2 = Knight(6, 0, 'w', board)
        WhiteBishop1 = Bishop(2, 0, 'w', board)
        WhiteBishop2 = Bishop(5, 0, 'w', board)
        WhiteQueen = Queen(3, 0, 'w', board)
        WhiteKing = King(4, 0, 'w', board)
        # Now we should put the pawns
        for i in range(8):
            exec("WPawn" + str(i+1)  + "= Pawn(i, 1, 'w', board)")
        return board