import random

def play_guessing_game(secret_number, max_tries):
    number_tries = 1
    user_number = int(input('Please enter a number:'))
    while(secret_number != user_number) and number_tries < max_tries:
        if(secret_number > user_number):
            print("The secret number is greater ")
        else:
            print('The secret number is less')

        user_number = int(input('Please enter a number:'))
        number_tries = number_tries + 1
    return number_tries
    
def print_game_results(number_tries, max_tries):
    if(number_tries < max_tries):
        print('***************************************')
        print('Congrats! you found the correct number!')
        print('***************************************')
    else:
        print('***************************************')
        print('   OHHHHH NUMBER NOT FOUND - TRY AGAIN ')
        print('***************************************')
        
# GUESSING NUMBER GAME - 3 tries
secret_number = random.randint(1,11)
max_number_tries = 3
number_tries = play_guessing_game(secret_number, max_number_tries)
print_game_results(number_tries, max_number_tries)


