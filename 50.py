#take 3 input from user
#loop: repeating

start=1
s=0
while start<=3:
    data=int(input(f'Enter num{start}: ')) #10
    s=s+data
    start=start+1

print(f'Addition of inputs are: {s}')
