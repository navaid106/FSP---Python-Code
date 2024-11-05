#take input from user rollno,name, marks of 5 sub. cal total & avg

#1. input
rollno=int(input("Enter Rollno: "))
name=input("Enter Name: ")
print("Enter your 5 subject marks: ")
s1=float(input("Enter Sub1: "))
s2=float(input("Enter Sub2: "))
s3=float(input("Enter Sub3: "))
s4=float(input("Enter Sub4: "))
s5=float(input("Enter Sub5: "))

#2. process
total=s1+s2+s3+s4+s5
avg=total/5

#3. output
print('*'*30)
print(f'''
----------------
Student Details
----------------
Name    : {name}
rollno  : {rollno}
total   : {total}
average : {avg}
''')
print('*'*30)
