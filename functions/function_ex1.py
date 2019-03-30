# Find sum of all natural numbers between 1 to n using functions
def sum_all_number(user_number):
    total = 0
    for index in range(1, num+1):
        total = total + index
    return total   
num = int(input('Please enter a number:'))
total_result = sum_all_number(num)   
print('Total : '+str(total_result))
