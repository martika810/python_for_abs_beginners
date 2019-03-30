# Write a program to count total number of notes in given amount 200,100,50,20,10,5

amount = int(input("please enter an amount: "))
notes200 = notes100 = notes50 = notes20 = notes10= notes5 = 0

if(amount>= 200):
    notes200 = int(amount/200)
    amount = amount - (notes200*200)
if(amount>= 100):
    notes100 = int(amount/100)
    amount = amount - (notes100*100)
if(amount>= 50):
    notes50 = int(amount/50)
    amount = amount - (notes50*50)
if(amount>= 20):
    notes20 = int(amount/20)
    amount = amount - (notes20*20)
if(amount>= 10):
    notes10 = int(amount/10)
    amount = amount - (notes10*10)
if(amount>= 5):
    notes5 = int(amount/5)
    amount = amount - (notes5*5)

print('Notes 200: '+ str(notes200))
print('Notes 100: '+ str(notes100))
print('Notes 50: '+ str(notes50))
print('Notes 20: '+ str(notes20))
print('Notes 10: '+ str(notes10))
print('Notes 5 : '+ str(notes5))
