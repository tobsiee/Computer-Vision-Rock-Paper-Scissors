import numpy as np
import time
import random
import cv2
from keras.models import load_model

# this python code is created to build the model for the game rock paper scissors

# for milestone 4 : you can creae user score, computer score, number of rounds/run, list of choice (rock, paper, scissors, nothing) in your init method
# also create a get_prediction method and paste the keras model code, little tweaks are needed
# you can use add max under np  to mapp the values 1,2,3,4 to rock, paper, scissors, nothing
# you need to put a countdown timer to the game, so the game ends after a number of runs or time period.

class computer_vision:

    def __init__(self, computer_choice, user_choice, no_rounds, choice_list):
        
        self.computer_choice = computer_choice
        self.user_choice = user_choice
        self.no_rounds = no_rounds
        self.choice_list = choice_list
        

        #computer_wins = 0
        #user_wins = 0

        pass

    def get_computer_choice(self):
        """
        this function is used to get the computer choice from rock, paper or scissors
        """
        #prediction = self.prediction()
        self.computer_choice = random.choice(['rock', 'paper', 'scissors'])

        pass

    #def get_prediction(self):
        #model = load_model('keras_model.h5')
    
        #pass


    def get_user_choice(self):
        """
        this function is used to get the user's choice of rock, paper or scissors
        """
        self.user_choice = input("Please enter your choice (rock, paper or scissors):")

        pass

   


    def get_winner(self):
        """
        this function is used to get the winner of the game
        """
        if self.computer_choice == self.user_choice:
            print( "It's a tie!")
        elif self.computer_choice == 'rock':
            if self.user_choice == 'paper':
                print(f"{self.user_choice} beats {self.computer_choice}, You win!")
            else:
                print(f"{self.computer_choice} beats {self.user_choice}, You lost!")
        elif self.computer_choice == 'paper':
            if self.user_choice == 'scissors':
                print(f"{self.user_choice} beats {self.computer_choice}, You win!")
            else:
                print(f"{self.computer_choice} beats {self.user_choice}, You lost")
        elif self.computer_choice == 'scissors':
            if self.user_choice == "rock":
                print(f"{self.user_choice} beats {self.computer_choice}, You win!")
            else:
               print(f"{self.computer_choice} beats {self.user_choice}, You lost!")
        # no condition true
        else: 
            print( "You have entered an invalid input")

        pass

def play(computer_choice, user_choice, no_rounds, choice_list):
    """
    this function is used to play the game
    """
    no_rounds = 5
    choice_list = ['rock', 'paper', 'scissors','nothing']
    game = computer_vision(computer_choice, user_choice, no_rounds, choice_list )
    computer_choice = game.get_computer_choice()
    user_choice = game.get_user_choice()
    game.get_winner()

    pass

        
            
  

if __name__ == '__main__':
    choice_list = ['rock', 'paper', 'scissors','nothing']
    no_rounds = 5
    computer_choice = ''
    user_choice = ''
    for i in range(no_rounds):
        play(computer_choice, user_choice, no_rounds, choice_list)
        time.sleep(1) # delay for 1 second
        print("\n")
    

        