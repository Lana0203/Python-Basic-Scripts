
from time import sleep
from random import randint
while True:
    print('\nMenu:\n-----\n1. Print numbers from 1-100\n2. Check list for Fibonacci\n3. Generate random numbers until we get 12 or until 10 raffles were executed.')
    choice = input('\nPlease enter the number from the following menu options: ')
    if choice=="1":
        for i in range(1,101):
            print(i)
    elif choice=="2":
        fibo_list=[]
        for i in range(7):
             fibo_list.append(int(input('Please enter a number: ')))
        boolean = "True"
        for i in range(2, (len(fibo_list))):
            print(fibo_list[i])
            print(fibo_list[i - 1])
            print(fibo_list[i - 2])
            print('\n')
            if (fibo_list[i]) != (fibo_list[i - 1]) + (fibo_list[i - 2]):
                boolean = 'False'
                break
        if (boolean) == 'True':
            print('It is a Fibonacci series. ')
        else:
            print('It is not a Fibonacci series. ')
    elif choice=="3":
        counter=1
        num1=randint(1,12)
        while(num1!=12 and counter<11):
            print('Counter:' + str(counter) + '  Number:' + str(num1) + '\n' )
            counter=counter+1
            num1 = randint(1, 12)
    else:
        print('Please select 1-3 only! ')
        continue
    exit=input('Do you wish to exit? y/n\n ')
    if(exit=='yes' or exit=='y'):
        print('Thank you and goodbye!')
        break

