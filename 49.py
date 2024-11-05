#number: 12541
#total digits: 5

num=int(input('Enter a number: '))
count=0
while num > 0:
    num=num//10 #deleting last digit
    count+=1

print(f'Total digits: {count}')
