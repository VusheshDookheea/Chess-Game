from game import ChessBoard

chessboard = ChessBoard()
print(chessboard)
while True:
    try:
        move = str(input('Move (example : e2e4) : '))
        chessboard.move(move)
        file = open('Chessboard.txt','a')
        file.write(str(chessboard)+'\n')
        file.close()
        print(chessboard)
    except Exception as e:
        print(str(e))
