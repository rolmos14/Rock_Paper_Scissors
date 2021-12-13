import random


class RockPaperScissors:

    default_choices = ["rock", "paper", "scissors"]

    def __init__(self):
        self.user_name = ""
        self.user_score = 0
        self.user_choice = ""
        self.com_choice = ""
        self.valid_choices = self.default_choices

    def run(self):
        self.user_name = input("Enter your name: ")
        print(f'Hello, {self.user_name}')
        self.check_existing_score()
        self.select_game_options()
        print("Okay, let's start")
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

    def select_game_options(self):
        game_options = input()
        if game_options != '':
            self.valid_choices = game_options.split(",")

    def user_turn(self):
        while True:
            self.user_choice = input()
            if self.user_choice in [*self.valid_choices, "!exit", "!rating"]:
                break
            print("Invalid input")

    def com_turn(self):
        self.com_choice = random.choice(self.valid_choices)

    def result(self):
        # Options after selected option until half of the length of the list win over
        # selected option, in a circular list. The other half lose.
        user_choice_index = self.valid_choices.index(self.user_choice)
        aux_choices = self.valid_choices[user_choice_index + 1:]
        aux_choices.extend(self.valid_choices[:user_choice_index])
        user_lose_choices = aux_choices[:len(aux_choices) // 2]
        user_win_choices = aux_choices[len(aux_choices) // 2:]
        if self.com_choice in user_win_choices:
            print(f'Well done. The computer chose {self.com_choice} and failed')
            self.user_score += 100
        elif self.com_choice in user_lose_choices:
            print(f'Sorry, but the computer chose {self.com_choice}')
        else:
            print(f'There is a draw ({self.com_choice})')
            self.user_score += 50


game = RockPaperScissors()
game.run()
