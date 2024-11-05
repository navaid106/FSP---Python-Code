#WAP to check number -ve, +ve or zero

#1. input
number=int(input('Enter a number: '))

#2. process
check= "+ve" if number>0 else "-ve" if number<0 else "Zero"

#3. output

print(f'your Number is: {check}')

