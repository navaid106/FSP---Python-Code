#num: 123
#total: 3 + 2 + 1 = 6
# // remove the last digit
# % store the deleted digit


num = int(input('Enter a number: '))#123
adding=0
while num > 0:
    store=num%10 # taking last digit
    adding+=store
    num=num//10 # deleting last digt

print(f'Addition of all digits are: {adding}')



