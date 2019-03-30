# Print the multiplication table of any number
#  3 x 0 = 0
#  3 x 1 = 3
#  3 x 2 = 6
#  3 x 3 = 9
#  3 x 4 = 12
#  ......
#  3 x 10 = 30
num = int(input('Please enter a number:'))
index = 0
while(index < 11):
    print(str(num) + " x " + str(index) + " = "+ str(num*index))
    index = index+1