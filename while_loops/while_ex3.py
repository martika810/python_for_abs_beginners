# Find sum of all natural numbers between 1 to n
num = int(input('Please enter a number:'))
total = 0
index = 1
while(index < num+1):
    total = total + index
    index=index+1
print('Total : '+str(total))
