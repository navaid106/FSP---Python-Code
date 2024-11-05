#Write a program to delete last two digits from user's number

#1. input
num1=int(input("Enter a number: "))

#2. process
num2=num1//100

#3. output
print(f'''
Older Number: {num1}
New Number: {num2}
''')
