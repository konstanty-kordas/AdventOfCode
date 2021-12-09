def checkDanger(T,Pi,Pj):
    N=[]
    if Pi != 0:
        N.append(T[Pi-1][Pj])
        if T[Pi][Pj] >= T[Pi-1][Pj]:
            return 0
    if Pj != 0:
        N.append(T[Pi][Pj-1])
        if T[Pi][Pj] >= T[Pi][Pj-1]:
            return 0
    if Pi != len(T)-1:
        N.append(T[Pi+1][Pj])
        if T[Pi][Pj] >= T[Pi+1][Pj]:
            return 0
    if Pj != len(T[Pi])-1:
        N.append(T[Pi][Pj+1])
        if T[Pi][Pj] >= T[Pi][Pj+1]:
            return 0
    # print("NEIGHBOURS:", N)
    # print("OG: ",T[Pi][Pj])
    return T[Pi][Pj]+1

def getNeighbours(T,Pi,Pj):
    N=[]
    if Pi != 0:
        N.append([Pi-1,Pj])
    if Pj != 0:
        N.append([Pi,Pj-1])
    if Pi != len(T)-1:
        N.append([Pi+1,Pj])
    if Pj != len(T[Pi])-1:
        N.append([Pi,Pj+1])
    return N

def paintBasin(basins,map,Li,Lj,paint):
    neighbours = getNeighbours(map,Li,Lj)
    for n in neighbours:
        if map[n[0]][n[1]] > map[Li][Lj] and map[n[0]][n[1]]!=9:
            basins[n[0]][n[1]] = paint
            paintBasin(basins,map,n[0],n[1],paint)

heatmap = []
with open('day9.txt') as file:
    for line in file:
        heatmap.append([int(k) for k in list(line) if k!= '\n'])
basins = [[0 for m in l] for l in heatmap]
danger = 0
lowPoints = []
for i in range(len(heatmap)):
    for j in range(len(heatmap[i])):
        if checkDanger(heatmap,i,j):
            lowPoints.append([i,j])

k = 1
for point in lowPoints:
    basins[point[0]][point[1]]=k
    # print(point)
    paintBasin(basins,heatmap,point[0],point[1],k)
    k+=1

basinSizes = [0 for i in range(k)]
for line in basins:
    for point in line:
        basinSizes[point]+=1
# print(basinSizes)
basinSizes.pop(0)
basinSizes.sort()   
print(basinSizes[-1]*basinSizes[-2]*basinSizes[-3])

with open('output.txt', 'w') as f:
    for l in basins:
        for p in l:
            f.write(str(p)+" ")
        f.write('\n')

from PIL import Image
import random
colors = [(random.randint(40,200),random.randint(40,200),random.randint(40,200)) for i in range(k)]
img = Image.new( 'RGB', (len(basins)*2,len(basins[0])*2), "black") # Create a new black image
pixels = img.load() # Create the pixel map
for i in range(len(basins)):    # For every pixel:
    for j in range(len(basins[i])):
        if(basins[i][j])==0:
            pixels[i,j] = (0,0,0)
            pixels[i+1,j] = (0,0,0)
            pixels[i,j+1] = (0,0,0)
            pixels[i+1,j+1] = (0,0,0)
        else:    
            pixels[i,j] = colors[basins[i][j]]
            pixels[i+1,j] = colors[basins[i][j]]
            pixels[i,j+1] = colors[basins[i][j]]
            pixels[i+1,j+1] = colors[basins[i][j]]


img.show()