

from random import randint
from time import sleep

print('Generating random numbers...\n')
sleep(2)
num1=randint(1,7)
num2=randint(1,7)
print('First number: ' + str(num1))
print('Second number: ' + str(num2))
if(num1==num2):
    print('\nCongratulations! You have won 500,000$ ')
else:
    print("\nWe're sorry, this time luck was not on your side. You'll do better next time!")

