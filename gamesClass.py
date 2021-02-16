import os
import time

# i think classes is not a good choice for the 1st part of the project, since it has no added value at all. 
# the classes should be implemented in the 2nd part, where you need to implement the logic of each game.
# it should be as followes: Game class, a generic and abstract class (use abc module), and each game class will inherit from the abstract class
class games:
    def __init__(self, game, difficulty):
        self.game = game
        self.difficulty = difficulty

    def memory_game(self):
        print(" i am 1 ")
        time.sleep(5)
       # self.clear()

        # need to implements

    def guess_game(self):
        print(" i am 2 ")

        # need to implements
    def currency_game(self):
        print(" i am 3 ")
        # need to implements
    def run_game(self):
        if self.game == 1:
            self.memory_game()
        elif self.game == 2:
            self.guess_game()
        elif self.game == 3:
            self.currency_game()
        else:
            print("you ar out of range")
    def clear(self):
      os.system('clear')
