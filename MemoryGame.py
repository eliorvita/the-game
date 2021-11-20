import random

def create_list_of_randoms(difficulty):
    return random.sample(range(1, 101), difficulty)

def let_user_guess(difficulty):
    guessed_list = []
    i = 1
    r = range(1, 101)
    print(f"You will be asked to guess {difficulty} numbers between 1 and 101")
    while (i <= difficulty):
        guess_a_number = input(f"{i}: Guess a number: ")
        while guess_a_number == "" or not guess_a_number.isnumeric() or int(guess_a_number) not in r or guess_a_number in guessed_list:
            if guess_a_number in guessed_list:
                guess_a_number = input(f"{i}: You already chose this number, choose another: ")
            else:
                guess_a_number = input(f"{i}: Dont be smart, Guess a number between 1 and 101: ")

        guessed_list.append(guess_a_number)
        i += 1
    return guessed_list

def is_list_equal(difficulty):
    random_list = create_list_of_randoms(difficulty)
    user_guessed_list = let_user_guess(difficulty)
    return [random_list, user_guessed_list]

def memoryPlay(difficulty):
    guess_randoms = is_list_equal(difficulty)
    print(f"The random numbers were {guess_randoms[0]}")
    if guess_randoms[0] == guess_randoms[1]:
        return True

