from os import system
from random import choice


def replace_at(string, pos, car):
    lista = list(string)
    lista[pos] = car
    return "".join(lista)


def run():
    MAX_LIVES = 6
    attempts = 0
    lives = 0
    win = False
    # HANGMANG sprites
    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    # List with words of the game
    with open("./data.txt", "r") as f:
        words = [word.replace("\n", "") for word in f]

    # word selected
    word = choice(words)
    # word with spaces
    hidden_word = "*"*len(word)
    # game loop
    def game_ui(lives, attempts, HANGMANPICS, hidden_word):
        game_uii = f"""
    ██   ██  █████  ███    ██  ██████  ███    ███  █████  ███    ██ 
    ██   ██ ██   ██ ████   ██ ██       ████  ████ ██   ██ ████   ██ 
    ███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██ 
    ██   ██ ██   ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██ 
    ██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████

    Intentos fallidos: {lives}
    Intentos Jugados: {attempts}
    {HANGMANPICS[lives]}
    Palabra: {hidden_word}
    """
        print(game_uii)

    while (lives < MAX_LIVES) and not(win):
        system("clear")
        game_ui(lives, attempts, HANGMANPICS, hidden_word)
        # Input
        user_letter = input("Ingrese una letra: ")
        while len(user_letter) > 1:
            user_letter = input(
                "Solo debe ingresar una letra, intentelo de nuevo: ")
        attempts += 1
        # Search letter
        for i in range(len(word)):
            if word[i] == user_letter:
                hidden_word = replace_at(hidden_word, i, word[i])

        if not(user_letter in hidden_word):
            lives += 1

        if hidden_word == word:
            win = True

    if win:
        print(f"¡Ganaste! la palabra era {word}")
    else:
        system("clear")
        game_ui(lives, attempts, HANGMANPICS, hidden_word)
        print(f"Mas suerte la proxima, la palabra era {word}")


if __name__ == '__main__':
    run()
