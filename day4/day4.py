numbers = []
tables = []
with open('day4.txt') as file:
    numbers = [int(i) for i in file.readline().split(',')]
    for line in file.readlines():
        if line=='\n':
            plate = []
            tables.append(plate)
            continue
        plate.append([int(p) for p in line.split()])
        
            
idx=0
condition = True
result = 0
lastNum = 0
last=[]
while condition:
    k=0
    while k< len(tables):
        popped=False
        if not condition:
            break
        for i in range(5):
            for j in range(5):
                if tables[k][i][j]==numbers[idx]:
                    tables[k][i][j]=0
        for i in range(5):
            if sum(tables[k][i]) == 0:
                last= tables.pop(k)
                popped=True
                break
            col=0
            for j in range(5):
                col+=tables[k][j][i]
            if col==0:
                last = tables.pop(k)
                popped=True
                break
        if not popped:
            k+=1
    if len(tables)==0:
        lastNum=numbers[idx]
        break
    idx+=1
print(last)
print(sum([sum(l) for l in last]))
print(lastNum)
print(lastNum*sum([sum(l) for l in last]))