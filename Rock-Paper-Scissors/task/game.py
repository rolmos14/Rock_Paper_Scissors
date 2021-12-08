import random


class RockPaperScissors:

    valid_choices = ["rock", "paper", "scissors"]
    results = {"win": {"rock": "scissors",
                       "paper": "rock",
                       "scissors": "paper"},
               "lose": {"rock": "paper",
                        "paper": "scissors",
                        "scissors": "rock"}}

    def __init__(self):
        self.user_choice = ""
        self.com_choice = ""

    def run(self):
        while True:
            self.user_turn()
            if self.user_choice == "!exit":
                print("Bye!")
                break
            self.com_turn()
            self.result()

    def user_turn(self):
        while True:
            self.user_choice = input()
            if self.user_choice in [*self.valid_choices, "!exit"]:
                break
            print("Invalid input")

    def com_turn(self):
        self.com_choice = random.choice(self.valid_choices)

    def result(self):
        if self.results["win"][self.user_choice] == self.com_choice:
            print(f'Well done. The computer chose {self.com_choice} and failed')
        elif self.results["lose"][self.user_choice] == self.com_choice:
            print(f'Sorry, but the computer chose {self.com_choice}')
        else:
            print(f'There is a draw ({self.com_choice})')


game = RockPaperScissors()
game.run()
