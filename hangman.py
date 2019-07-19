import random

def hangman():
    words = ["попкина", "писикот", "лисичка", "финик", "мандаринка"]
    word = random.choice(words)
    wrong = 0
    stages = ["",
            "________        ",
            "|       |       ",
            "|       |       ",
            "|       O       ",
            "|      /|\      ",
            "|      / \      ",
            "|               "]
    rletters = list(word)
    board = ["_"]*len(word)
    win = False
    print("Welcome to execution!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Enter letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("You won! Secret word was: ")
            print(" ".join(board))
            fox = [ "                   /\   /\\",
                    "                  //\\\_//\\\     ____",
                    "                  \_     _/    /   /",
                    "                   / * * \    /^^^]",
                    "                   \_\O/_/    [   ]",
                    "                    /   \_    [   /",
                    "                    \     \_  /  /",
                    "                     [ [ /  \/ _/",
                    "                    _[ [ \  /_/"]
            print("\n".join(fox))
            win = True
            break

    if not win:
        print("\n".join(stages[0: wrong+1]))
        print("You lost! The secret word was: {}.".format(word))
    input()

hangman()
