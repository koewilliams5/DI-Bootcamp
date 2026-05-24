import random

class Game:

    def get_user_item(self):

        valid_choice =["rock", "paper", "scissors"]

        while True:
            choice = input("Enter your choice : ")
            if choice in valid_choice:
                return choice
            else:
                print("Invalid choice!")
        
    def get_computer_item(self):

        valid_choice =["rock", "paper", "scissors"]
        
        valid = random.choice(valid_choice)
        return valid


    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif user_item == "rock" and computer_item == "paper":
            return "win"
        elif user_item == "rock" and computer_item == "scissors":
            return "win"
        elif user_item == "paper" and computer_item == "scissors":
            return "win"

    def play(self):
        pass 