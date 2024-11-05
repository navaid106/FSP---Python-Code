#2 x 1 = 2
#2 x 2 = 4
#2 x 3 = 6
#2 x 4 = 8
#...........
#...........
#2 x 10 = 20

table=int(input('Enter table: ')) #3
limit=int(input('Enter table limit: '))
start=1
while start <= limit:
    print(f'{table} x {start} = {table*start}')
    start+=1
