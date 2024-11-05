#Write a program to check whether a person is
# eligible or driving a car or not
#Note: age>=18 for male candidate
#Note: age>=22 for female candate

#1. input
age=int(input("Enter your age: "))
gender=input('Enter your gendar: ')

#2. process
checking="Eligible" if age>=18 and gender=='male' or age>=22 and gender=='female' else "Not Eligible"


#3. output
print(f'You are: {checking}')
