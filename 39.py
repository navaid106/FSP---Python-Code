#Check digit Alpha and Symb

store=input('Enter any input: ') #A


if store>='A' and store<='Z' or store>='a' and store<='z':
    print('Alphabet')
elif store>='0' and store<='9':
    print('Number')
else:
    print('Symbol')
