EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9
X = "X" #pierwszy ruch
O = "O"


def new_board():
    """Utwórz nową planszę gry."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Wyświetl planszę gry na ekranie."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

var1 = new_board()
display_board(var1)


