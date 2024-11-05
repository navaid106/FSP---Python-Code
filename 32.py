#check the input character is alphabet or digit
#----------------------------------------------------------

#1. input
ch=input("Enter any alphabet: ") #b

#2. process
check="Alphabet" if ch>='a' and ch<='z' or ch>='A' and ch<='Z' else "digit" if ch>='0' and ch<='9' else "Symbol"

#3. output
print(f"input is : {check}")
