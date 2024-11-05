#Login by generated OTP
#Nested if => if inside if

import random
username=input('username: ') #shezuka

if username == 'shezuka':
    input('Generate OTP by Pressing Enter key')
    otp=random.randint(1000,9999)
    print(f'Your OTP is: {otp}')
    temp=int(input('Enter OTP: '))

    if otp == temp:
        print(f'Welcome, {username}')
    else:
        print('Invalid OTP')

else:
    print('Invalid username')


    



