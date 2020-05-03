def sendBoard(board):
    boardPrint = ''
    for y in range(0, 3, 1):
        for x in range(0, 3, 1):
            boardPrint = boardPrint + str(board[y][x]) + ' '
        boardPrint = boardPrint + '\n'
    return boardPrint 

def saveBoard(board):
    board_file = open('board.txt', 'w')
    board_file.write(str(board))

def getBoard():
    board_file = open('board.txt', 'r')
    return board_file.read()

def checkMove(move):
    if move == (7 or 8 or 9):
        move_y_pos = 0
    if move == (4 or 5 or 6):
        move_y_pos = 1
    if move == (1 or 2 or 3):
        move_y_pos = 2
    return move_y_pos


def doMove(board, move, player):
    player_dic = {
        ('computer' or 1) : 'x',
        ('human' or 0) : 'o'
    }
    move_x_pos = (move + 2) % 3
    move_y_pos = checkMove(move)
    if str(board[move_y_pos][move_x_pos]) == str(move):
        board[move_y_pos][move_x_pos] = player_dic[player]
        saveBoard(board)
    else:
        return 'Polje je že zasedeno. Poizkusi znova.'
    

def askForMove():
    return 'Ti si na vrsti. Vpiši številko poteze.'

win_comb=((0,1,2),(3,4,5),(6,7,8),(6,3,0),(7,4,1),(8,5,2),(6,4,2),(8,4,0))

def checkWin(board, whowin):
    for each in win_comb:
        if (board[each[0]] == board[each[1]] and board[each[1]]== board[each[2]]):
            if bool(whowin):
                return board[each[1]]
            else:
                return True
    return False

def whoWin(board):
    return checkWin(board, True)

def returnPlayer(player_sig):
    player_dic = {
        'x' : 'computer',
        'o' : 'human'
    }
    return player_dic[player_sig]