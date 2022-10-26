import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
Player = "X"
winner = None
game = True


def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])


def playerInput(board):
    inp = int(input("Enter a number between 1-9: "))
    if 1 <= inp <= 9 and board[inp - 1] == "-":
        board[inp-1] = Player
    else:
        print("Sorry that spot is already taken")


def checkupanddown(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def checksideway(board):
    global winner
    if board[0] == board[3] == board[6] and board[1] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True


def checkdiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True


def tie(board):
    global game
    if "-" not in board:
        printBoard(board)
        print("Its a Tie!")
        game = False


def checkWin():
    global game
    if checkupanddown(board) or checksideway(board) or checkdiag(board):
        print(f"The winner is {winner}")
    game = False

def switchPlayer(board):
    global Player
    if Player == "X":
        Player = "0"
    else:
        Player = "X"


def computer(board):
    while Player == "0":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "0"
            switchPlayer(board)


while game:
    printBoard(board)
    playerInput(board)
    checkWin()
    tie(board)
    switchPlayer(board)
    computer(board)
    checkWin()
    tie(board)
