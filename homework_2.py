# rock paper scissors
# Write a set of if/else/elif statements that compare two variables 'user_input' and 'computer_input'
# These variables contain the strings `rock`, `paper', or 'scissors'
# Implement the rules as if/else/elif statements after line 10 with an indentation of 4 spaces, see example (line 10+11)
# Return a string saying 'tied game', 'you win', or 'computer wins' after every statement
# If there is no error when you run the script, you succeeded
# Push the solution in your repo

rules = {'rock': {'paper': 'computer wins', 'scissors': 'you win'},
         'paper': {'scissors': 'computer wins', 'rock': 'you win'},
         'scissors': {'rock': 'computer wins', 'paper': 'you win'}}
def rock_paper_scissors(user_input, computer_input):
    if user_input is computer_input:
        return 'tied'
    else:
        return rules[user_input][computer_input]


if __name__ == "__main__":
    possibilities = ['rock', 'paper', 'scissors']
    for user_choice in possibilities:
        for computer_choice in possibilities:
            print(user_choice + '\t' + computer_choice)
            print(rock_paper_scissors(user_choice, computer_choice))
            if user_choice == computer_choice:
                assert rock_paper_scissors(user_choice, computer_choice) is 'tied'
