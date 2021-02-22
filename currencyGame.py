import abstractGame,random



class currencyGame(abstractGame.AbstractGame):
    def __init__(self, diffuclty):
        self.diffuclty = diffuclty


    def get_guess_from_user(self,secretNumber):
       print (f"please guess {secretNumber} to shekel\n")
       return int(input("Please guess a number between 1 -" + self.diffuclty+": "))


    def playGame(self):
        secretNumber = random.randint(1,100)
        userGuess=self.get_guess_from_user(secretNumber)

        self.checkResult(userGuess,secretNumber)


    def checkResult(self ,userGuess,sccretNumber):
      resultOfCurrency= sccretNumber*3.6
      lowInterval= resultOfCurrency-(5-int(self.diffuclty))
      highInterval= resultOfCurrency+(5-int(self.diffuclty))
      if lowInterval<userGuess<highInterval:
           print("you are in the range great job  !!")
      else:
          print("boooz")




# get_money_interval -Will get the current currency rate from USD to ILS and will
# generate an interval as follows:
# a. for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t +
# (5 - d))
#
# 2. get_guess_from_user - A method to prompt a guess from the user to enter a guess of
# value to a given amount of USD
# 3. play - Will call the functions above and play the game. Will return True / False if the user
# lost or won.