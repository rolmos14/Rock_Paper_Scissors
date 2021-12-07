class RockPaperScissors:

    def __init__(self):
        self.user_choice = ""
        self.com_choice = ""

    def start_game(self):
        self.user_turn()
        self.com_turn()
        self.result()

    def user_turn(self):
        while True:
            self.user_choice = input()
            if self.user_choice in ["rock", "paper", "scissors"]:
                break
    def com_turn(self):
        if self.user_choice == "rock":
            self.com_choice = "paper"
        elif self.user_choice == "paper":
            self.com_choice = "scissors"
        else:
            self.com_choice = "rock"

    def result(self):
        print(f'Sorry, but the computer chose {self.com_choice}')


game = RockPaperScissors()
game.start_game()
