#Q. Delete last digit from user's number

#1. input
num=int(input("Enter number: ")) #int
delete=int(input('How digits you want to delete: ')) 

#2. process
num2=num//(10**delete) # power **


#3. output
print(f'old number: {num}\nNew number: {num2}')
