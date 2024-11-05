#Calculate Electricity bill

units=int(input('Enter total build units: ')) 

if units <=100:
    amount=0
elif units>100 and units<=200:
    amount=0+(units-100)*5

elif units>200:
    amount=0*100+5*100+(units-200)*10

else:
    print('Invalid units')

print(f'''
***********Electricity Bill***********
Total Build Units    : {units}
Total Amount to Pay  : {amount}

****************************************
''')

    
    
