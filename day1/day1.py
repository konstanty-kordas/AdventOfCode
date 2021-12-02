T = []
with open('day1.txt') as file:
    T = [int(l) for l in file.readlines()]
# T =  [199,200,208,210,200,207,240,269,260,263]
numOfIncrease = 0
threes = []
for i in range(3,len(T)+1):
    threes.append(sum(T[i-3:i]))

for i in range(len(threes)-1):
    if threes[i+1]>threes[i]:
        numOfIncrease+=1
print(numOfIncrease)