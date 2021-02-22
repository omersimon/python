# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import playerClass, abstractGame
from currencyGame import currencyGame
from guessGame import guessGame
from memoryGame import memoryGame


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

player_name = input("please Enter your name: ")

print(f"Hello {player_name} and welcome to the World of Games (WoG).Here you can find many cool games to play.")

while True:

    game_number = input("Please choose a game to play:\n\n"
                        "1. Memory Game - a sequence of numbers will appear for 1 second and you have toguess it back\n"
                        "2. Guess Game - guess a number and see if you chose like the computer\n"
                        "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")
    if game_number.isnumeric() == False:
        print("not integer")
        continue

    elif int(game_number) < 0 or int(game_number) > 3:
        print("out of range")
        continue

    break

while True:
    difficulty = input("please enter difficult between 1-5 : ")
    if difficulty.isnumeric() == False:
        print("not integer")
        continue

    elif int(difficulty) < 0 or int(difficulty) > 5:
        print("out of range")
        continue

    else:
        print(" great choose ")
        break

if int(game_number) == 1:
    game = memoryGame(difficulty)
elif int(game_number) == 2:
    game = guessGame(difficulty)
elif int(game_number) == 3:
    game = currencyGame(difficulty)


game.playGame()

