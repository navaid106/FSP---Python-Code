#Write a program to find simple intrest

#1. input
p=float(input("Enter P_Amout: "))
r=float(input("Enter R: "))
t=int(input("Enter T: "))


#2. process
simple_interest=(p*r*t)/100

#3. output
print('*'*66)
print('*'*66)
print(f'''
P_Amount: {p}\n
Rate: {r}\n
Time: {t}\n
Simple Interest is: {simple_interest}
''')
print('*'*66)
print('*'*66)
