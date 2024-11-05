#Student Details.. name,rollno, 2sub marks
#calculate total & avg using ternary operator


#1. input
name=input("Enter name: ")
rollno=int(input("Enter rollno: "))
sub1=float(input("Enter Python marks: "))
sub2=float(input("Enter Java marks: "))

#2. process
total=sub1+sub2
avg=total/2
result="Pass" if sub1>=40 and sub2>=40 else "Fail"

#3. output
print(f'''
------------------------
{name}, you are {result}
------------------------
Name       : {name}
rollno     : {rollno}
sub1 marks : {sub1}
sub2 marks : {sub2}
Total      : {total}
Average    : {avg}
Result     : {result}
''')
