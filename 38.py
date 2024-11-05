#check leap year
# Leap years: 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, and 2036

year=int(input('Enter year: '))

if year%400==0:
    print('Leap year')

elif year%100==0:
    print('Not a leap year')

elif year%4==0:
    print('Leap year')

else:
    print('Not a leap year')
