def print_multiplication_table(num):
    print('----MULTIPLICATION TABLE ----')
    for index in range(0,11):
        print(str(num) + " x "+ str(index)+ " = "+ str(num*index))    
num = 3
print_multiplication_table(num)
num = 4
print_multiplication_table(num)
num = 5
print_multiplication_table(num)
    
