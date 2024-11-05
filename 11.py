#1. Program to convert A->a

#1. input
#-----------------
value=input("Enter a uppercase Char: ")

#2. Process
#-----------------
temp=ord(value)
temp+=32 # temp=temp+32 === temp:97
temp2=chr(temp) # temp:a

#3. Output
#-----------------
print(f"{value} ----> {temp2}")

