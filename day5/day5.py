pipelines = []
s=0
with open('day5.txt') as file:
    for line in file.readlines():
        a = []
        for i in line.split(' -> '):
            x= [int(i.split(',')[0]),int(i.split(',')[1])]
            s = max(s,max(x))
            a.append(x)
        pipelines.append(a)
s+=1
floor = [[0 for i in range(s)] for i in range(s)]
for pipe in pipelines:
    x1 = pipe[0][0]
    y1 = pipe[0][1]
    x2 = pipe[1][0]
    y2 = pipe[1][1]
    vertical=False
    horizontal=False
    if x1 == x2:    #vertical
        for i in range(min(y1,y2),max(y1,y2)+1):
            floor[x1][i]+=1
    elif y1 == y2:  #horizontal
        for i in range(min(x1,x2),max(x1,x2)+1):
            floor[i][y1]+=1
    else:           #diagonal

        direction = x1+y1==x2+y2
        for i in range(abs(x1-x2)+1):
            if direction:   #same sum, /
                if x1>x2:   #9,7 -> 7,9
                    floor[x1-i][y1+i]+=1
                else:       #7,9 -> 9,7
                    floor[x1+i][y1-i]+=1
            else:           #same diff, \
                if x1>x2:   #3,3-> 1,1
                    floor[x1-i][y1-i]+=1
                else:       #1,1 -> 3,3
                    floor[x1+i][y1+i]+=1
# print(floor)
result = 0
for i in floor:
    for j in i:
        if j>1:
            result+=1
print(result)
