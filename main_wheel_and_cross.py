X = "X"  # pierwszy ruch
O = "O"
EMPTY = " "
TIE = "TIE" #remis
NUM_SQUARES = 9

def display_instruct():
    """Wyświetl instrukcję gry."""
    print(
    """
    Witaj w grze "kółko i krzyżyk". Ty kontra komputer. 
    Swoje posunięcie wskażesz poprzez wprowadzenie liczby z zakresu 0 - 8.
    Liczba ta odpowiada pozycji na planszy zgodnie z poniższym schematem:
    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8
    Przygotuj się. \n
    """
    )

def ask_yes_no(question):
        """Zadaj pytanie, na które można odpowiedzieć tak lub nie."""
        response = None
        while response not in ("t", "n"):
            response = input(question).lower()
            return response

def choice():
        """Ustal, czy pierwszy ruch należy do gracza, czy do komputera."""
        go_first = ask_yes_no("Czy chcesz mieć prawo do pierwszego ruchu? (t/n): ")
        if go_first == "t":
            print("\nPierwszy ruch należy do Ciebie. ")
            human = X
            computer = O
        else:
            print("\nPierwszy ruch wykonuje komputer.")
            computer = X
            human = O
        return computer, human

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

def winner(board):
    """Ustal zwycięzcę gry."""
    WAYS_TO_WIN = ((0, 1, 2),
                    (3, 4, 5),
                    (6, 7, 8),
                    (0, 3, 6),
                    (1, 4, 7),
                    (2, 5, 8),
                    (0, 4, 8),
                    (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
            return None

def human_move(board, human):
    """Odczytaj ruch człowieka."""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Jaki będzie Twój ruch? (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nTo pole jest już zajęte. Wybierz inne.\n")
    return move


def computer_move(board, computer, human):
    """Spowoduje wykonanie ruchu przez komputer."""
    # utwórz kopię roboczą, ponieważ funkcja będzie zmieniać listę
    board = board[:]
    # najlepsze pozycje do zajęcia według kolejności
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Wybieram pole numer", end=" ")
    # jeśli komputer może wygrać, wykonaj ten ruch
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
            # ten ruch został sprawdzony, wycofaj go
        board[move] = EMPTY
    # jeśli człowiek może wygrać, zablokuj ten ruch
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
            # ten ruch został sprawdzony, wycofaj go
        board[move] = EMPTY
    # ponieważ nikt nie może wygrać w następnym ruchu, wybierz najlepsze wolne pole
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def legal_moves(board):
    """Utwórz listę prawidłowych ruchów."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square]==EMPTY:
            moves.append(square)
    return(moves)

def ask_number(question, low, high):
    """Poproś o podanie liczby z odpowiedniego zakresu."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def next_turn(turn):
    """Zmień wykonawcę ruchu."""
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner, computer, human):
    """Pogratuluj zwycięzcy."""
    if the_winner != TIE:
        print(the_winner, "jest zwycięzcą!\n")
    else:
        print("Remis!\n")
    if the_winner == computer:
        print("Wygrał komputer.")
    elif the_winner == human:
        print("Wygrałeś")


display_instruct()
computer, human = choice()
turn = X
board = new_board()
display_board(board)

while not winner(board):
    if turn == human:
        move = human_move(board, human)
        board[move] = human
        display_board(board)
        turn = next_turn(turn)
    else:
        move = computer_move(board, computer, human)
        board[move] = computer
        display_board(board)
        turn = next_turn(turn)

the_winner = winner(board)
congrat_winner(the_winner, computer, human)