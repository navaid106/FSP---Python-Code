#Login by nested if

import random

otp=random.randint(1000,9999)
username=input('Enter your name: ')

input('Press Enter to Generate OTP: ')
print(f'Your login otp is: {otp}')

password = int(input('Enter otp: '))
#nested if

if password==otp:
    if username=="raju":
        print('Login Successful!')
    else:
        print('username is invalid')
else:
    print('password is invalid')


