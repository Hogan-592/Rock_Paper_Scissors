#This project uses random library that's built in python to play paper scissors rock
import random

def play(): #This function passes in no parameter
    user = input("What's your choice ? 'r' for rock, 'p' for paper, 's' for scissors\n ")
    computer = random.choice(['r', 'p', 's']) #this method allows computer to randomly pick one of the options

    if user == computer:
        return 'It\'s a tie' # \ to diferentate a single quote and '

    if is_win(user, computer):
        return 'You won!'

    #return means the program stops right there, so this line will only be excuted if the above conditions don't return anything
    return 'You lost!'

def is_win(player, opponent):
    #return true if the player wins
    # r > s, p > r, s > p
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
    or (player == 's' and opponent == 'p'):
        return True

print(play())
