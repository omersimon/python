from abc import ABC, abstractmethod
class AbstractGame(ABC):
    @abstractmethod
    def playGame(self):
        pass

    @abstractmethod
    def get_guess_from_user(self):
        pass

    def hello(self):
       print(f"Hello {self.name} and welcome to the World of Games (WoG).Here you can find many cool games to play.")
