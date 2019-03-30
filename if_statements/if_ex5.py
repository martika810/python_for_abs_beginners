# You are looking for a new member to expand your programming.
# It should be a person from ages 18 to 40
# Write a program to ask the user’s age and whether the user has previous python experience(using 'y' or 'n').
# Display a message indicating whether the person is eligible to join your team.
age = int(input('Please enter your age: '))
previous_python_experience = input('Do you have preivous python experience( y=yes or n=no )?')
if(age>18 and age<41) and previous_python_experience=='y':
    print('Eligible to join the team')
else:
    print("Sorry not eligible")