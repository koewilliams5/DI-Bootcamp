import random

class Game:

    def get_user_item(self):
        valid_choices = ["rock", "paper", "scissors"]
        while True:
            choice = input("Enter your choice (rock/paper/scissors): ").lower()
            if choice in valid_choices:
                return choice
            else:
                print("Invalid choice! Please try again.")

    def get_computer_item(self):
        valid_choices = ["rock", "paper", "scissors"]
        return random.choice(valid_choices)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (user_item == "rock" and computer_item == "scissors") or \
             (user_item == "scissors" and computer_item == "paper") or \
             (user_item == "paper" and computer_item == "rock"):
            return "win"
        else:
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"\nYou chose: {user_item}")
        print(f"Computer chose: {computer_item}")

        if result == "win":
            print("You won!")
        elif result == "draw":
            print("It's a draw!")
        else:
            print("You lost!")

        return result