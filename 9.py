#Write a program to swap two values:

#1. input
buket1=float(input("Enter first value: "))
buket2=float(input("Enter second value: "))

#3. Output
print("Before swaping...")
print(buket1)
print(buket2)

#type checking
print(type(buket1))
print(type(buket2))


#2. Process
empty=buket1
buket1=buket2
buket2=empty

#3. Output
print("After Swaping...")
print(buket1)
print(buket2)

#type checking
print(type(buket1))
print(type(buket2))
