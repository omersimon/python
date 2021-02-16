# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import playerClass, gamesClass


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

player_name = input("please Enter your name: ")

p1 = playerClass.player(player_name)
p1.hello()
while True:
    try:
        game_number = int(input("Please choose a game to play:\n\n"
                                "1. Memory Game - a sequence of numbers will appear for 1 second and you have toguess it back\n"
                                "2. Guess Game - guess a number and see if you chose like the computer\n"
                                "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"))
        if game_number < 0 or game_number > 3:
            print("out of range")
            continue
        else:
            print(" great choose ")
            break
    except ValueError:
        print("That's not an int!")
while True:
    try:
     difficulty = int(input("please enter difficult between 1-5 : "))
     if difficulty < 0 or difficulty > 5:
         print("out of range")
         continue
     else:
         print(" great choose ")
         break
    except ValueError:
     print("That's not an int!")


game = gamesClass.games(game_number, difficulty)
game.run_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
