## conditions:

from time import sleep
while(True):
   print('Menu:\n1. Insert number and ** it by 3\n2. Insert 4 IPs to a list and print it\n3. Insert 4 entries to DNS_dictionary and print it\n4. Check if a string is Polindrom\n' )
   choice=input('Please choose the service you would like to receive: ')
   if(choice=="1"):
      num=int(input('Please choose a number: '))
      print('\nCalculating number...' )
      sleep(2)
      print('\nYour number is: ' + str(num**3))
   elif(choice=="2"):
      ip_list=[]
      ip_list.append(input("Enter new IP address: "))
      ip_list.append(input("Enter new IP address: "))
      ip_list.append(input("Enter new IP address: "))
      ip_list.append(input("Enter new IP address: "))
      print('\nInserting IP addresses into a new list...\n')
      sleep(2)
      print(ip_list)
   elif(choice=="3"):
      dns_dict={}
      dns_dict.update({input('Enter new URL: '): input('Enter new IP: ')})
      dns_dict.update({input('Enter new URL: '): input('Enter new IP: ')})
      dns_dict.update({input('Enter new URL: '): input('Enter new IP: ')})
      dns_dict.update({input('Enter new URL: '): input('Enter new IP: ')})
      print('\nInserting entries into a new dictionary...\n')
      sleep(2)
      print('The new DNS dictionary:\n-----------------------\n' + str(dns_dict))
   elif(choice=="4"):
      string1=input('Please enter your string: ')
      print(string1[::-1])
      if(string1==(string1[::-1])):
         print('Your string is a palindrome. ')
      else:
         print('\nYour string is not a palindrome.')
   else:
      print('\nPlease choose only between 1-4! ')
   exit=input('\nDo you wish to exit the service menu? y/n ')
   if(exit=='y') or(exit=='yes'):
      break
      print('Thank you and goodbye! ')

