import random
# print out game logo
from art import logo
print(logo)

#print greetings
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 0 and 100.")

# set the difficulty from user input
difficulty = input("Choose a difficulty. Type \"easy\" or \"hard\": \n")

# set up the initial attempt number based on the difficulty
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    print("Invalid input. Game Over.")
print(f"You chose the {difficulty} mode. You'll have {attempts} to guess the number.")

# set up the random number
rand_num = random.randint(0,100)

# define a function that reduces life when guess wrong
def reduce_life(attempts):
	return attempts - 1

#input a guess
guess = int(input("Make a guess:\n"))
while guess != rand_num and attempts != 0:
	if guess > rand_num:
		print("Too high.")
		print("Guess again.")
		attempts = reduce_life(attempts)
	elif guess < rand_num:
		print("Too low.")
		print("Guess again.")
		attempts = reduce_life(attempts)
	guess = int(input("Make a guess:\n"))
	print(f"You have {attempts} attempts left.")

if guess == rand_num:
	print(f"You guessed it right! The number is {guess}.")
else:
	print(f"Game Over. You lost. The number is {rand_num}.")
