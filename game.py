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

    def sketch_board(self, board):
        func_sym_col = np.vectorize(self.retrieve_piece)
        symbolic_board = func_sym_col(board)
        return symbolic_board

    def retrieve_piece(self, piece):
        if isinstance(piece, ChessPiece):
            return str(piece.symbol+piece.color)
        else:
            return '0 '

    def rules(self, piece, i, j, m, n):
        board = self.board
        #symboard = self.sketch_board(board)
        if ((self.__class__.cn % 2) == 0):
            if (piece.color == 'b'):
                raise Exception('It is Whites turn to play')
        else:
            if (piece.color == 'w'):
                raise Exception('It is Blacks turn to play')
        piece_type = piece.symbol # Rules depend on the piece
        # Implement check
        check_new_pos = 0 # We should modify this write a loop over other pieces
        opponent_king = 0
        auxboard = []
        if ((m - i) >= 0):
            check1 = 1
        else:
            check1 = 0
        if ((n - j) >= 0):
            check2 = 1
        else:
            check2 = 0

        if piece_type == 'K':
            if (abs(i - m) > 1):
                raise Exception('This is not a valid move for the King')
            elif (abs(j - n) > 1) :
                raise Exception('This is not a valid move for the King')
            elif check_new_pos:
                raise Exception('The King cannot move to a threatened square!!!')
            elif opponent_king:
                raise Exception('You cannot go too close to the opponent king')

        elif piece_type == 'Q':
            if not ((abs((i - m) / (j - n)) == 1) or ((i - m) == 0) or ((j - n) == 0)):
                raise Exception('The queen cannot move like this')
            if (i - m) == 0:
                if check2:
                    auxboard = board[i][j+1:n]
                else:
                    auxboard = board[i][n+1:j]
            elif (j - n) == 0:
                if check1:
                    auxboard = board[i+1:m][j]
                else:
                    auxboard = board[m+1:i][j]
            else:
                if check1 and check2:
                    for ct in range(m - i - 1):
                        auxboard.append(board[i + 1 + ct][j + 1 + ct])
                elif check1 and (not check2):
                    for ct in range(m - i  - 1):
                        auxboard.append(board[i + 1 + ct][j + 1 - ct])
                elif (not check1) and check2:
                    for ct in range(i - m - 1):
                        auxboard.append(board[i + 1 - ct][j +1 + ct])
                elif (not check1) and (not check2):
                    for ct in range(i - m - 1):
                        auxboard.append(board[i + 1 - ct][j + 1 - ct])
            if not (all(p == 0 for p in auxboard)):
                raise Exception('The path is obscured')

        elif piece_type == 'R':
            if not (((i - m) == 0) or ((j - n) == 0)):
                raise Exception('The rook cannot move like this')
            if (i - m) == 0:
                if check2:
                    auxboard = board[i][j+1:n]
                else:
                    auxboard = board[i][n+1:j]
            elif (j - n) == 0:
                if check1:
                    auxboard = board[i+1:m][j]
                else:
                    auxboard = board[m+1:i][j]
            if not (all(p == 0 for p in auxboard)):
                raise Exception('The path is obscured')

        elif piece_type == 'B':
            if not (abs((i - m) / (j - n)) == 1):
                raise Exception('The bishop cannot move like this')
            if check1 and check2:
                for ct in range(m - i - 1):
                    auxboard.append(board[i + 1 + ct][j + 1 + ct])
            elif check1 and (not check2):
                for ct in range(m - i  - 1):
                    auxboard.append(board[i + 1 + ct][j + 1 - ct])
            elif (not check1) and check2:
                for ct in range(i - m - 1):
                    auxboard.append(board[i + 1 - ct][j +1 + ct])
            elif (not check1) and (not check2):
                for ct in range(i - m - 1):
                    auxboard.append(board[i + 1 - ct][j + 1 - ct])
                    print(board[i + 1 - ct][j + 1 - ct])
            if not (all(p == 0 for p in auxboard)):
                raise Exception('The path is obscured')
        elif piece_type == 'N': # The path may be obscured this time
            if not (((abs(i - m) == 2) and (abs(j - n) == 1)) or  ((abs(i - m) == 1) and (abs(j - n) == 2))):
                raise Exception('The knight cannot move like this')

        elif piece_type == 'P':
            if piece.color == 'w':
                if piece.cn == 0:
                    if not(((n - j) == 2) or ((n - j) == 1) and ((i - m) == 0)):
                        raise Exception('The pawn cannot move like this')
                elif piece.cn != 0:
                    if not((n - j) == 1):
                        raise Exception('The pawn cannot move like this')
            else:
                if piece.cn == 0:
                    if not(((n - j) == -2) or ((n - j) == -1) and ((i - m) == 0)):
                        raise Exception('The pawn cannot move like this')
                elif piece.cn != 0:
                    if not((n - j) == -1):
                        raise Exception('The pawn cannot move like this')

        # Implement one cannot move to a square containing same color piece
        if board[m][n] != 0: # There is a piece in the final position
            if board[i][j].color == board[m][n].color:# Two pieces are of the same color
                raise Exception("You cannot go to your own pieces location")
            elif board[m][n].symbol == 'K':# The opponent king is in the location
                raise Exception("You cannot eat the KING")
        if ((piece_type == 'P') or (piece_type == 'K')):
            piece.cn += 1
        return 1

    def move(self, position):
        # These two strings are for board coordinates
        letter_log = 'abcdefgh'
        num_log = '12345678'
        board = self.board
        if not (len(position) == 4):
            raise ValueError('The position string should consist of 4 characters');
        # Get the final and initial positions
        init_pos = position[:2]
        fin_pos = position[-2:]
        # First perform the checks
        if not (str == type(init_pos) and (str == type(fin_pos))):     # Check if the arguments are strings
            raise TypeError('The supplied positions should be strings!')
        elif not ((init_pos[0] in letter_log) and (init_pos[1] in num_log)): # Check if they fulfill the condition to be on the board
            raise ValueError('The initial position values should be between a1 and h8')
        elif not ((fin_pos[0] in letter_log) and (fin_pos[1] in num_log)): # Check if they fulfill the condition to be on the board
            raise ValueError('The final position values should be between a1 and h8')
        elif init_pos == fin_pos:
            raise ValueError('Final position should be different from the initial position')
        # Now determine if there is a piece on the initial square
        i = letter_log.index(init_pos[0]) ; j = num_log.index(init_pos[1]) # Numerical initial position
        m = letter_log.index(fin_pos[0]); n = num_log.index(fin_pos[1]) # Numerical final position
        if not (isinstance(board[i][j], ChessPiece)):
            raise Exception('There is no chess piece here')
        piece = board[i][j]
        if self.rules(piece, i, j, m, n) != 1:
            raise('This move is not allowed')
        # Move the piece on the chessboard
        piece.movepiece(i, j, m, n, board)
        self.__class__.cn += 1 # Increment the cner after each allowed move

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