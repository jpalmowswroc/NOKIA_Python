X = "X" #pierwszy ruch
O = "O"

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

choice()
