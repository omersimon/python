import abstractGame, time, os,random

import subprocess as sp


class memoryGame(abstractGame.AbstractGame):
    def __init__(self, diffuclty):
        self.diffuclty = diffuclty

    def playGame(self):
        randomlist = []
        for i in range(0, int(self.diffuclty)):
            n = random.randint(1, 101)
            randomlist.append(n)
        print(" ".join(str(x) for x in randomlist))
        time.sleep(5)
        os.system('clear')
        userList=self.getListFromUser()
        self.checkResult(randomlist,userList)

    def getListFromUser(self):
        userList = []
        for i in range(int(self.diffuclty)):
            userInput=int(input("Please guess  "))
            userList.append(userInput)
        return userList




    def checkResult(self ,userList,randomList):
      if userList==randomList:
           print("you rock!! !!")
      else:
          print("boooz")
