import random

x = random.randrange(1,20)

y = int(input('Choose a number between 1 and 20 '))

while y != x:
    if y > x:
        print('Too high. Try again')
        y = int(input('Choose a number between 1 and 20 '))
    else:
        print('Too low. Try again.')
        y = int(input('Choose a number between 1 and 20 '))
        
print('Correct! You win!')

