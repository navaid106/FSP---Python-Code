# delete three last digit & print deleted digits & print new number

#1. input
num1=int(input("Enter a number: "))

#2. process
num2=num1//1000
deleted=num1%1000

#3. output
print(f'''
Older Number   : {num1}
New Number     : {num2}
Deleted digits : {deleted}
''')
