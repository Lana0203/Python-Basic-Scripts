#Cube Game:

from random import randint
from time import sleep
print('Welcome to the cube game!\nEach round costs 3 ILS.\nYou can play as many rounds as you want.\nEnjoy the game and goodluck!\n')
amount=int(input('Enter the amount of money you want to put in: '))
turns=(amount//3)
print('You can play: ' + str(turns) + ' rounds. ' + '\nYour change is: ' + str(amount%3))

for i in range(turns):
    print('\nRound number ' + str(i+1) + ' :\n-----------------' + '\nRolling cubes...')
    sleep(3)
    cube1=randint(1,6)
    cube2=randint(1,6)
    prize=0
    print('\nCube 1: ' + str(cube1) + '\nCube 2: ' + str(cube2))
    if(cube1==cube2) and (cube1==6):
        prize=prize+1000
        print('Congratulations! You won ' + str(prize) + 'ILS! ')
    elif(cube1==cube2):
        prize=prize+100
        print('\nCongratulations! You won ' + str(prize) + 'ILS! ')
    elif(cube1!=cube2) and (cube2==2):
        prize=prize+40
        print('\nCongratulations! You won ' + str(prize) + 'ILS! ')
    elif(cube1!=cube2) and (cube1==1):
        prize=prize+20
        print('\nCongratulations! You won ' + str(prize) + 'ILS! ')
    else:
        print("\nOops, we're sorry ... better luck next time! ")

