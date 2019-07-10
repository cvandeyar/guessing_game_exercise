# First attempt at guessing game failed

# import random

# num_to_guess = random.randint(1, 100)

# player_name = input("Welcome, what is your name? ")

# player_guess = int(input(f"""{player_name}, I'm thinking of a number between 1 and 100.
# Try to guess my number.
# Your guess? """))

# def check_guess(guess):
#     """takes player's guess and checks if it's right"""

#     guess_again = input("Your guess? ")

#     if guess < num_to_guess:
#         print("Your guess is too low, try again.")
#         guess_again
#     elif guess > num_to_guess:
#         print("Your guess is too high, try again.")
#         guess_again
#     else:
#         print(f"Well done, {player_name}! You found my number....")

# check_guess(player_guess)

#########################################################
# good working attempted

# import random

# num_to_guess = random.randint(1, 100)

# player_name = input("Welcome, what is your name? ")

# print(f"""{player_name}, I'm thinking of a number between 1 and 100.
# Try to guess my number.""")

# def check_guess():
#     """takes player's guess and checks if it's right"""

#     tries = 0

#     while True:

#         # guess = input("Your guess? ")
#         tries = tries + 1

#         # if isinstance(guess, str): #this doesn't work
#         # if type(guess) is not int:
#         # if guess.isalpha():

#         try: 
#             guess = int(input("Your guess? "))

#         except ValueError:
#             print("Please guess a valid integer")
#             continue

#         if guess < num_to_guess and guess > 0:
#             print("Your guess is too low, try again.")

#         elif guess > num_to_guess and guess < 101:
#             print("Your guess is too high, try again.")

#         elif guess > 100 or guess < 1:
#             print("Please enter a valid number within the given range")

#         else:
#             print(f"Well done, {player_name}! You found my number in {tries} tries")
#             break

# check_guess()

#########################################################
# More advanced version with multiple rounds and best score

# import random

# player_name = input("Welcome, what is your name? ")

# print(f"""{player_name}, I'm thinking of a number between 1 and 100.
# Try to guess my number.""")

# def check_guess():
#     """takes player's guess and checks if it's right"""

#     best_score = 99999

#     while True:

#         tries = 0
#         num_to_guess = random.randint(1, 100)

#         while True:

#             tries = tries + 1

#             try: 
#                 guess = int(input("Your guess? "))

#             except ValueError:
#                 print("Please guess a valid integer")
#                 continue

#             if guess < num_to_guess: #guess < num_to_guess and guess > 0: 
#                 print("Your guess is too low, try again.")

#             elif guess > num_to_guess:
#                 print("Your guess is too high, try again.")

#             elif guess > 100 or guess < 1:
#                 print("Please enter a valid number within the given range")

#             else:
#                 print(f"Well done, {player_name}! You found my number in {tries} tries")
#                 break
                
#         play_again = input("would you like to play again? y or n ")

#         if tries < best_score:
#             best_score = tries

#         if play_again.lower() == "y":
#             continue
#         elif play_again.lower() == "n":
#             print(f"Nice {player_name}! your best score was {best_score}")
#             break

# check_guess()

#########################################################
# Limit the number of guess a user gests

from random import randint

player_name = input("Welcome, what is your name? ")

print(f"""{player_name}, I'm thinking of a number between 1 and 100.
Try to guess my number.""")

number = randint(1,100)

tries = 1
max_tries = 5

while tries <= max_tries:

    guess = int(input("Guess the number: "))
    # tries = tries + 1

    if guess > number:
        
        print("sorry too high")
        print(f"you have {max_tries - tries} tries left")
        tries = tries + 1

    elif guess < number:
        
        print("sorry too low")
        print(f"you have {max_tries - tries} tries left")
        tries = tries + 1

    elif guess == number:
        print(f"good job! took you {tries} tries")
        break

print("game over")


