import abstractGame,random



class guessGame(abstractGame.AbstractGame):
    def __init__(self, diffuclty):
        self.diffuclty = diffuclty


    def get_guess_from_user(self):
       return int(input("Please guess a number between 1 -" + self.diffuclty+": "))


    def playGame(self):
        userGuess=int(self.get_guess_from_user())
        print(userGuess)

        sccretNumberInt = random.randint(1,(int(self.diffuclty)))
        sccretNumberStr = str(sccretNumberInt)
        print("screet number"+sccretNumberStr)
        self.checkResult(userGuess,sccretNumberInt)


    def checkResult(self ,x,sccretNumber):
      if sccretNumber==x:
           print("you are the king  !!")
      else:
          print("boooz")
