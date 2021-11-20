from GuessGame import guessPlay
from MemoryGame import memoryPlay
from Live import load_game, welcome

if __name__ == '__main__':
    while (True):
        print(welcome("Guy"))
        return_game_plus_diff = load_game()

        if return_game_plus_diff[0] == '1':
            was_it_a_win = guessPlay(int(return_game_plus_diff[1]))
        elif return_game_plus_diff[0] == '2':
            was_it_a_win = memoryPlay(int(return_game_plus_diff[1]))
        elif return_game_plus_diff[0] == '3':
            pass

        if was_it_a_win:
            print("YOU WIN THIS GAME")
        else:
            print("This time you lost")

        play_another = input("Want to play another game? [y/n] ")
        if play_another != 'y' and play_another != 'Y':
            break


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
