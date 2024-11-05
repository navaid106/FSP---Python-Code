#Bonus to employee

name=input('Enter your name: ')
year = int(input('Enter year: '))
salary = float(input('Enter your salary: '))

if year>10:
    bonus=(salary*10)/100 #10%

elif year>=6 and year<=10:
    bonus=(salary*8)/100 #8%

elif year<6:
    bonus=(salary*5)/100 #5%

else:
    print("Please enter the valid year or get lost")

print(f'''
*******************************
        Diwali Bonus
*******************************
Name   :     {name}
Years  :     {year}
Salary :     {salary}
Bonus  :     {bonus}
Total  :     {salary+bonus}
*******************************
        Enjoy your Bonus
*******************************
        
''')
