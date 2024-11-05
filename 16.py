#Write a program to print deleted digit & and print remaining digits.
	#Number: 12345
	#Deleted: 5
        #newNumber: 1234

#1. input
num=int(input("Enter Number: ")) #int: 12345

#2. process
last=num%10  #storing_last_digit: 5
new=num//10 #remove_last_digit: 1234

#3. output
print(f'Number: {num}\nDeleted: {last}\nnewNumber: {new}')
