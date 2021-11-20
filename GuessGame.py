from random import rand

def generate_number(difficulty):
    return randint(1, int(difficulty))

def get_guess_from_user(difficulty):
    return input(f"Guess a number between 1 and {difficulty}: ")

def compare_results(difficulty):
    random_number = generate_number(difficulty)
    user_guess = int(get_guess_from_user(difficulty))
    return [random_number, user_guess]

def guessPlay(difficulty):
    list_random_and_guess = compare_results(difficulty)
    if list_random_and_guess[0] == list_random_and_guess[1]:
        return True

