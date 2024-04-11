# ROCK, PAPER , SCISSOR 
import random

#ask the user for the choice

def get_user_choice(choice):
    choice = ('rock','paper','scissor')
    while True:
        user_choice=(input(f'choose any from {choice}: '))
        print(user_choice)
        
#check it is valid or not
        if user_choice in choice:
            return user_choice
        else:
            print("invalid choice")
            
#Generate random choice from the computer
def get_computer_choice(choice):

        computer_choice= random.choice(choice)
        return computer_choice
    
# determine the winner
def deterine_winner(computer_choice,user_choice):
        if computer_choice == user_choice:
            return 'its a tie'
        elif (user_choice == "rock" and computer_choice == "scissor") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissor" and computer_choice == "paper"):
             return 'heyyy you won the game!!!1'
        else:
            return 'you lost the game'
                    
def rock_paper_scissor():
    
    choice = ('rock','paper','scissor')
    
    while True:
        user_choice = get_user_choice(choice)
        computer_choice = get_computer_choice(choice)
        print(deterine_winner(computer_choice,user_choice))
    #Ask the user if they want to play again  
        play_again=(input("do  you want to play again (y/n): "))
        if play_again.lower() != "y":
            break
    print("thank you come again")    
    
rock_paper_scissor()




