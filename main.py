board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9",]

gameStillGoing = True
winner = None
currentPlayer = "X"

def displayBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def playGame():
    displayBoard()

    while gameStillGoing:

        handleTurn(currentPlayer)

        checkIfGameOver()

        flipPlayer()

        if winner == "X" or winner == "O":
            print(winner + " won.")
        elif winner = None:
            print("Tie.")

def handleTurn(player):
    position = input("Choose a position from 1-9: ")
    position = int(position) -1

    board[position] = "X"
    displayBoard()

def checkIfGameOver():
    checkIfWin()
    checkIfTie()

def checkIfWin():

    return

def checkIfTie():

    return

def flipPlayer():

    return

playGame()
