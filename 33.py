# check vowel or not

#1. input
alpha=input("Enter any character: ")


#2. process
check=alpha in ['a','e','i','o','u']

checked="Vowel" if check==True else "not Vowel"

#3. output
print(f'The given alphabet is: {checked}')
