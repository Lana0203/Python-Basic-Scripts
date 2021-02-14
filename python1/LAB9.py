from time import sleep
from random import randint

def menu():
    while True:
        choice=input('Menu:\n---------------\n1. Dogs Details\n2. Friends List\n3. N Azzeret\n\nPlease choose from the menu above:')
        if(choice=="1"):
            dogs()
        elif(choice=='2'):
            friends()
        elif(choice=='3'):
            azzeret()
        else:
            print('Choose 1-3 only! ')
            continue
        exit=input('Do you wish to exit? y/n\n')
        if(exit=="y" or exit=="yes"):
            print('Thank you and goodbye! ')
            break
        else:
            print('Welcome back!\n')


def dogs():
    dog_name=input("Enter dog's name: ")
    dog_age=int(input("Enter dog's age: "))
    print("\nDog's name: " + dog_name + "\nDog's age: " + str(dog_age*7))


def friends():
    friend_list=[]
    for i in range(5):
        friend_list.append(input("Enter a friend's name: "))
    name=input('Enter a new name: ')
    if(name in friend_list):
        print(name + ' is in this list.\n ')
    else:
            print(name + ' is not in this list.\n ')


def azzeret():
    num=int(input('Enter a number: '))
    sum=1
    for i in range(1,num+1):
        sum=sum*i
    print("\nThe azzeret of " + str(num) + ' is: ' + str(sum) + "\n")



menu()