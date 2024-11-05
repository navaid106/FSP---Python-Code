#Take rollno,name,3subject marks
#calculate total,avg

#1. input
rollno=int(input("Rollno: "))
name=input("Name: ")
sub1=float(input("Python Marks: "))
sub2=float(input("Java Marks: "))
sub3=float(input("React Marks: "))

#2. process
total=sub1+sub2+sub3
avg=total/3

#3. output
print(f'''
Student Name:     {name}
---------------------------
Student Rollno:   {rollno}
---------------------------
Total marks:      {total}
---------------------------
Average:          {avg}
---------------------------
''')
