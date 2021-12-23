# Tic Tac Toe

import streamlit as st


# 列印方法
def drawBoard(board):
    #這個函數打印出它被傳遞的板。
    # “board”是一個由 10 個字符串組成的列表，代表董事會（忽略索引 0）
    st.write('   |   |')
    st.write(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    st.write('   |   |')
    st.write('-----------')
    st.write('   |   |')
    st.write(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    st.write('   |   |')
    st.write('-----------')
    st.write('   |   |')
    st.write(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    st.write('   |   |')


def inputPlayerLetter():
    # 讓玩家輸入他們想要的字母。
    #返回一個列表，其中玩家的字母作為第一項，計算機的字母作為第二項。
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # 列表中的第一個元素是玩家的字母，第二個元素是計算機的字母。
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    # 隨機選擇先行的玩家。
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def playAgain():
    # 如果玩家想再次玩，此函數返回 True，否則返回 False。
    st.write('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


# 下子
def makeMove(board, letter, move):
    board[move] = letter


# 判斷遊戲是否結束
def isWinner(bo, le):
    # 給定一個棋盤和一個玩家的信，如果該玩家贏了，這個函數將返回 True。
    # 我們使用 bo 代替 board 和 le 代替 letter，所以我們不必輸入那麼多。
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))    # diagonal


def getBoardCopy(board):
    # 複製板列表並將其返回。
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard


# 驗證輸入的list值是否為空
def isSpaceFree(board, move):
    #如果通過的棋盤在通過的棋盤上是空的，則返回 true。
    return board[move] == ' '


# 返回下子位置
def getPlayerMove(board):
    # 讓玩家輸入他們的動作。
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)


# 從這些列表裡面隨機下
def chooseRandomMoveFromList(board, movesList):
    # 從傳遞板上的傳遞列表中返回一個有效的移動。
    # 如果沒有有效的移動，則返回 None。
    possibleMoves = []
    # 獲取空子位置list
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
            # list不為空，隨機選一個
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


# 電腦獲取下子位置
def getComputerMove(board, computerLetter):
    #給定一塊板和計算機的字母，確定移動的位置並返回該移動。
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    # 這個是機器下子的演算法
    # Here is our algorithm for our Tic Tac Toe AI:
    # 首先檢測我們下一步是否能贏
    # First, check if we can win in the next move
    for i in range(1, 10):
        # copy一份目前的下子畫板
        copy = getBoardCopy(board)
        # 如果備份的畫板中內容不為空
        if isSpaceFree(copy, i):
            # 下子
            makeMove(copy, computerLetter, i)
            # 如果下這個位置贏就將這個位置返回
            if isWinner(copy, computerLetter):
                return i
                # 檢測對手下一步是否會贏，會贏的話就堵它
    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

                # 優先下這些位置（優先佔據角落）
    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # 奪取中心點
    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # 在最後的列表中下子
    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    # 如果板上的每個空間都已被佔用，則返回 True。否則返回 False。
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


st.write('Welcome to Tic Tac Toe!')

# 死迴圈，沒有
while True:
    # Reset the board
    # 重置輸出板
    theBoard = [' '] * 10
    # 選棋子
    playerLetter, computerLetter = inputPlayerLetter()
    # 隨機產生誰先下
    turn = whoGoesFirst()
    # 列印是誰先下
    st.write('The ' + turn + ' will go first.')
    # 遊戲開始
    gameIsPlaying = True
    while gameIsPlaying:
        # 人先下
        if turn == 'player':
            # Player’s turn.
            # 列印畫板
            drawBoard(theBoard)
            # 獲取下子位置
            move = getPlayerMove(theBoard)
            # 下子
            makeMove(theBoard, playerLetter, move)
            # 判斷遊戲是否結束
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                st.write('Hooray! You have won the game!')
                # 結束遊戲
                gameIsPlaying = False
            else:
                # 驗證畫板是否畫滿
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    st.write('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer’s turn.
            # 機器獲取下子位置
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                st.write('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    st.write('The game is a tie!')
                    break
                else:
                    turn = 'player'
    # 如果不想玩了就跳出迴圈
    if not playAgain():
        break
