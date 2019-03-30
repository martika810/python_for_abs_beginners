# Find sum of all natural numbers between 1 to n
num = int(input('Please enter a number:'))
total = 0
for index in range(1, num+1):
    total = total + index

print('Total : '+str(total))
