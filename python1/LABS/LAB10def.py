def menu():
    while(True):
        choice=input('\nMenu:\n------------\n1. IP System\n2. DNS System\n\nPlease choose one of the above: ')
        if(choice=="1"):
            choice_ip=input('\n1. Search for an IP Address from a list\n2. Add IP Address to a list\n3. Delete IP Address from a list\n4. Print all IP Addresses\n\nPlease choose a service: ')
            if(choice_ip=='1'):
                search_ip()
            elif(choice_ip=='2'):
                add_ip()
            elif(choice_ip=='3'):
                print(1)
            elif(choice_ip=='4'):
                print(1)
            else:
                print(2)

        elif(choice=="2"):
            choice_dns=input('\n1. Search for URL in a dictionary\n2. Add URL + IP Address to a dictionary\n3. Delete URL from a dictionary\n4. Update IP Address of a specific URL\n5. Print all the URL:IP entries\n\nPlease choose a service:')
            if(choice_dns=='1'):
                search_url()
            elif(choice_dns=='2'):
                add_entry()
            elif(choice_dns=='3'):
                del_url()
            elif(choice_dns=='4'):
                update_ip()
            elif(choice_dns=='5'):
                print_entry()

#functions for IP:

def search_ip():
    ip = input('Please enter an IP Address: ')
    filename = 'G:/Ilana/Cyber/hello.txt'
    file = open(filename, 'r')
    if ip in file.read():
        print('IP Address ' + ip + ' is inside list: ' + (filename))
        return True
    else:
        file.close()
        print('IP Address ' + (ip) + ' is not inside list: ' + (filename))
        return False

def add_ip():
    ip = input('Please enter an IP Address: ')
    filename ='G:/Ilana/Cyber/hello.txt'
    file = open(filename, 'a+')
    file.write(ip)
    file.close()

def print_ip():
    filename = 'G:/Ilana/Cyber/hello.txt'
    file = open(filename, 'r')
    print(file.read())
    file.close()

#functions for DNS:

def search_url():
    dict = {'www.google.com':'1.1.1.1','www.youtube.com':'2.2.2.2','www.ynet.co.il':'3.3.3.3','www.netflix.com':'4.4.4.4'}
    url = input('Please enter a URL: ')
    if url in dict:
        print('The input URL: ' + url + ' is already inside the dictionary.')
    else:
        print('The input URL: ' + url + ' is not inside the dictionary.')

def add_entry():
    dict1 = {'www.google.com':'1.1.1.1','www.youtube.com':'2.2.2.2','www.ynet.co.il':'3.3.3.3','www.netflix.com':'4.4.4.4'}
    url = input('Please enter a URL: ')
    ip = input('Please enter an IP address: ')
    dict1.update({url:ip})
    print(dict1)

def del_url():
    dict1 = {'www.google.com': '1.1.1.1', 'www.youtube.com': '2.2.2.2', 'www.ynet.co.il': '3.3.3.3','www.netflix.com': '4.4.4.4'}
    url = input('Please enter a URL: ')
    dict1.pop(url, None)
    print(dict1)

def update_ip():
    dict1 = {'www.google.com': '1.1.1.1', 'www.youtube.com': '2.2.2.2', 'www.ynet.co.il': '3.3.3.3', 'www.netflix.com': '4.4.4.4'}
    url=input('Please enter the URL of which IP address you would like to change: ')
    ip=input('Please enter a new IP address: ')
    dict1[url]=ip
    print(dict1)

def print_entry():