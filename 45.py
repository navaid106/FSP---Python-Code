#Match cases

print("******Menu*******")
print("1. Addition")
print("2. Substraction")
print("3. multiplication")

choose=int(input("Enter your choice : ")) #1

num1=int(input('Enter num1: '))
num2=int(input('Enter num2: '))
match(choose):
    case 1:
        print(f'Addition is: {num1+num2}')
    case 2:
        print(f'Substraction is: {num1-num2}')
    case 3:
        print(f'Multiplication is: {num1*num2}')
    case _:
        print(f'R u drunk? Please check the menu again')

print('*'*30)
    
    
