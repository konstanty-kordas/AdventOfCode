T = []
with open('day2.txt') as f:
    T = [i.split() for i in f.readlines()]
for i in range(len(T)):
    T[i][1] = int(T[i][1])
depth=0
position = 0
aim=0
for i in T:
    if i[0] == 'forward':
        position+=i[1]
        depth+=aim*i[1]
    elif i[0] == 'down':
        aim+=i[1]
    elif i[0] == 'up':
        aim-=i[1]
print(depth*position)