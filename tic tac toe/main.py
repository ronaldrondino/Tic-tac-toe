# functions
def startingSequence():
    print("\nTIC TAC TOE....\n")
    print("|","1","|","2","|","3","|")
    print("|","4","|","5","|","6","|")
    print("|","7","|","8","|","9","|")


def displayBoard():
    print("|",board[0],"|",board[1],"|",board[2],"|")
    print("|",board[3],"|",board[4],"|",board[5],"|")
    print("|",board[6],"|",board[7],"|",board[8],"|")


def gameplay():
    global selectedCell
    selectedCell = input()
    
    if int(selectedCell)-1 >= 0 and int(selectedCell)-1 <= 8:
        if int(selectedCell) in takenCell:
            print("\nCell already selected, Choose another cell")
            gameplay()
        else:
            takenCell.append(int(selectedCell))
            addSelection()
    else:
        print("\nInvalid cell, Choose another cell")
        gameplay()


def playerSelector():
    global selectedPlayer
    if int(playerVar) % 2 == 0:
        selectedPlayer = "O"
    else:
        selectedPlayer = "X"


def playerDisplay():
    print("\nPlayer ",selectedPlayer," choose a cell")

def addSelection():
    if int(selectedCell) == 1:
        board[int(selectedCell)-1] = selectedPlayer
    elif int(selectedCell) == 2:
        board[int(selectedCell)-1] = selectedPlayer
    elif int(selectedCell) == 3:
        board[int(selectedCell)-1] = selectedPlayer
    elif int(selectedCell) == 4:
        board[int(selectedCell)-1] = selectedPlayer
    elif int(selectedCell) == 5:
        board[int(selectedCell)-1] = selectedPlayer
    elif int(selectedCell) == 6:
        board[int(selectedCell)-1] = selectedPlayer
    elif int(selectedCell) == 7:
        board[int(selectedCell)-1] = selectedPlayer
    elif int(selectedCell) == 8:
        board[int(selectedCell)-1] = selectedPlayer
    elif int(selectedCell) == 9:
        board[int(selectedCell)-1] = selectedPlayer
    print()
    displayBoard()
    gameResult()
    

def swapPlayer():
    global playerVar
    playerVar = playerVar + 1
    playerSelector()
    playerDisplay()
    gameplay()

def gameResult():

    if int(selectedCell) == 1:
        if board[0] == board[1] == board[2] or board[0] == board[4] == board[8] or board[0] == board[3] == board[6]:
            print("\nPlayer ",selectedPlayer," won")
            exit()
        elif len(takenCell) == 9:
            print("\nGame draw")
            exit()
        else:
            swapPlayer()
    
    elif int(selectedCell) == 2:
        if board[1] == board[4] == board[7] or board[1] == board[2] == board[0]:
            print("\nPlayer ",selectedPlayer," won")
            exit()
        elif len(takenCell) == 9:
            print("\nGame draw")
            exit()
        else:
            swapPlayer()
    
    elif int(selectedCell) == 3:
        if board[2] == board[1] == board[0] or board[2] == board[4] == board[6] or board[2] == board[5] == board[8]:
            print("\nPlayer ",selectedPlayer," won")
            exit()
        elif len(takenCell) == 9:
            print("\nGame draw")
            exit()
        else:
            swapPlayer()

    elif int(selectedCell) == 4:
        if board[3] == board[4] == board[5] or board[3] == board[6] == board[0]:
            print("\nPlayer ",selectedPlayer," won")
            exit()
        elif len(takenCell) == 9:
            print("\nGame draw")
            exit()
        else:
            swapPlayer()

    elif int(selectedCell) == 5:
        if board[4] == board[5] == board[3] or board[4] == board[7] == board[1] or board[4] == board[6] == board[2] or board[4] == board[8] == board[0]:
            print("\nPlayer ",selectedPlayer," won")
            exit()
        elif len(takenCell) == 9:
            print("\nGame draw")
            exit()
        else:
            swapPlayer()

    elif int(selectedCell) == 6:
        if board[5] == board[8] == board[2] or board[5] == board[4] == board[3]:
            print("\nPlayer ",selectedPlayer," won")
            exit()
        elif len(takenCell) == 9:
            print("\nGame draw")
            exit()
        else:
            swapPlayer()

    elif int(selectedCell) == 7:
        if board[6] == board[7] == board[8] or board[6] == board[4] == board[2] or board[6] == board[3] == board[0]:
            print("\nPlayer ",selectedPlayer," won")
            exit()
        elif len(takenCell) == 9:
            print("\nGame draw")
            exit()
        else:
            swapPlayer()

    elif int(selectedCell) == 8:
        if board[7] == board[4] == board[1] or board[7] == board[8] == board[6]:
            print("\nPlayer ",selectedPlayer," won")
            exit()
        elif len(takenCell) == 9:
            print("\nGame draw")
            exit()
        else:
            swapPlayer()

    elif int(selectedCell) == 9:
        if board[8] == board[5] == board[2] or board[8] == board[4] == board[0] or board[8] == board[7] == board[6]:
            print("\nPlayer ",selectedPlayer," won")
            exit()
        elif len(takenCell) == 9:
            print("\nGame draw")
            exit()
        else:
            swapPlayer()

# starting of code

board = [" "," "," "," "," "," "," "," "," "]
takenCell = []
playerVar = 1
selectedPlayer = "X"
selectedCell = 0

# Calling functions
startingSequence()
playerSelector()
playerDisplay()
gameplay()