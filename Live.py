
def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).")
    print("Here you can find many cool games to play.")

def load_game():
    r = range(1, 4)
    print("""Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS""")
    game = input("What is your choice from 1 to 3: ")
    while game == "" or not game.isnumeric() or int(game) not in r:
        game = input("What is your choice from 1 to 3: ")

    r = range(1, 6)
    difficulty = input("Please choose game difficulty from 1 to 5: ")
    while difficulty == "" or not difficulty.isnumeric() or int(difficulty) not in r:
        difficulty = input("Please choose game difficulty from 1 to 5: ")

    return [game, difficulty]