from getpass import getpass
username=input('Enter Your User Name:')
pwd=getpass('Enter Your Password')

if username=="sai" and pwd=="123":
    print('welcome',username)
else:
    print('Invalid Username or password')
