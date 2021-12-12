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
        self.user_name = ""
        self.user_score = 0
        self.user_choice = ""
        self.com_choice = ""

    def run(self):
        self.user_name = input("Enter your name: ")
        print(f'Hello, {self.user_name}')
        self.check_existing_score()
        while True:
            self.user_turn()
            if self.user_choice == "!exit":
                print("Bye!")
                break
            if self.user_choice == "!rating":
                print(f"Your rating: {self.user_score}")
                continue
            self.com_turn()
            self.result()

    def check_existing_score(self):
        with open("rating.txt") as file:
            file_lines = file.read().splitlines()
            for line in file_lines:
                if line.startswith(self.user_name):
                    self.user_score = int(line.split()[1])

    def user_turn(self):
        while True:
            self.user_choice = input()
            if self.user_choice in [*self.valid_choices, "!exit", "!rating"]:
                break
            print("Invalid input")

    def com_turn(self):
        self.com_choice = random.choice(self.valid_choices)

    def result(self):
        if self.results["win"][self.user_choice] == self.com_choice:
            print(f'Well done. The computer chose {self.com_choice} and failed')
            self.user_score += 100
        elif self.results["lose"][self.user_choice] == self.com_choice:
            print(f'Sorry, but the computer chose {self.com_choice}')
        else:
            print(f'There is a draw ({self.com_choice})')
            self.user_score += 50


game = RockPaperScissors()
game.run()
