import random

def playing_guessing_game(secret_number):
    number_tries = 0
    try:
        user_number = int(input('Please enter a number: '))
        number_tries = number_tries +1
        while(user_number != secret_number) :
            if(secret_number > user_number):
                print('Secret is larger')
            else:
                print('Secret is smaller')
            user_number = int(input('Please enter a number: '))
            number_tries = number_tries +1
    except ValueError:
        print('Please enter only numbers')
        return -1
    return number_tries
        
    
secret_number = random.randint(1,11)
tries = playing_guessing_game(secret_number)
if tries == -1:
    print('Error while running the game')
else:
    print('NUmber of tries: '+ str(tries))
    print('Congratulations')

