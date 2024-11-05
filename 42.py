#Generate OTP & Login through OTP

import random

name=input('Enter your name: ')

otp=random.randint(1000,9999)
print(f'Hey! {name}, Login with OTP: {otp}')
password=int(input('Enter OTP: '))

if otp==password:
    print(f'Welcome, {name}')
else:
    print('Get Lost from here, r u trying to hack my system...')


