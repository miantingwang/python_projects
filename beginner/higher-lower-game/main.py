import replit

# define a function that pick a random person from the data
def pick_random_person():
    '''pick a random person from the game data'''
    from game_data import data
    from random import choice
    chosen = choice(data)
    return chosen # (f" {chosen['name']}, a {chosen['description']}, from {chosen['country']}.")

# compare A and B and keep the winner
def compare_followers(A, B):
    '''choose the winner between the two and return the winner data'''
    if A['follower_count'] >= B['follower_count']:
        return A
    else:
        return B
score = 0
# keep score
def add_score():
    '''adding 1 to total score'''
    global score
    return score + 1

# print the game logo
from art import logo
print(logo)

# pick a random person A
# print information of person A
chosen_A = pick_random_person()
print(f"Compare A: {chosen_A['name']}, a(n) {chosen_A['description'].lower()}, from {chosen_A['country']}.")

# print the vs logo
from art import vs
print(vs)

gameplay = True

while gameplay == True:
    # pick a random person B
    chosen_B = pick_random_person()
    # print info of person B
    print(f"Against B: {chosen_B['name']}, a(n) {chosen_B['description'].lower()}, from {chosen_B['country']}.")
    
    # ask the user for which person has more followers
    user_answer = input("Who has more followers? Type 'A' or 'B': ")
    if user_answer == 'A':
        user_answer = chosen_A
    elif user_answer == 'B':
        user_answer = chosen_B
    
    winner = compare_followers(chosen_A, chosen_B)
    
    # see if the user chose correctly
    if winner == user_answer:
        score = add_score()
        replit.clear()
        print(logo)
        print(f"You're right. Current score: {score}")
        chosen_A = winner
        print(f"Compare A: {chosen_A['name']}, a(n) {chosen_A['description'].lower()}, from {chosen_A['country']}.")
        print(vs)
        
    else:
        replit.clear()
        print(logo)
        print(f"Sorry, that's wrong. Your final score is {score}")
        gameplay = False
    

# print the logo
# print the resulting score
# ask again

