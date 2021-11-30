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

class ChessPiece: # This is the base class, all the other specific pieces inherit this class.

    def __init__(self, x, y, color):
        if not ((int == type(x)) and (int == type(y))):
            raise TypeError(' x and y should be integers!!')
        elif not ((x in range(8)) and (y in range(8))):
            raise ValueError('x and y positions should be between 0 and 7 inclusive')
        elif not ((str == type(color)) and (color in 'wb')):
            raise ValueError('Color should be "w" or "b"')
        self.pos_x = x
        self.pos_y = y
        self.color = color

    def movepiece(self, i, j, m, n, chessboard):
        self.pos_x = i
        self.pos_y = j
        chessboard[i][j] = 0
        chessboard[m][n] = self

class King(ChessPiece):
    def __init__(self, x, y, color, chessboard):

        ChessPiece.__init__(self, x, y, color)
        self.symbol = 'K'
        self.cn = 0
        chessboard[self.pos_x][self.pos_y] = self

class Queen(ChessPiece):

    def __init__(self, x, y, color, chessboard):

        ChessPiece.__init__(self, x, y, color)
        self.symbol = 'Q'
        chessboard[self.pos_x][self.pos_y] = self

class Rook(ChessPiece):

    def __init__(self, x, y, color, chessboard):

        ChessPiece.__init__(self, x, y, color)
        self.symbol = 'R'
        chessboard[self.pos_x][self.pos_y] = self

class Bishop(ChessPiece):
    def __init__(self, x, y, color, chessboard):

        ChessPiece.__init__(self, x, y, color)
        self.symbol = 'B'
        chessboard[self.pos_x][self.pos_y] = self

class Knight(ChessPiece):
    def __init__(self, x, y, color, chessboard):

        ChessPiece.__init__(self, x, y, color)
        chessboard[self.pos_x][self.pos_y] = self ; self.symbol = 'N'

class Pawn(ChessPiece):

    def __init__(self, x, y, color, chessboard):
        ChessPiece.__init__(self, x, y, color)
        chessboard[self.pos_x][self.pos_y] = self;self.cn = 0;self.symbol = 'P'