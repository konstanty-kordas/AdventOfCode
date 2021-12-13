import numpy as np
points = []
instructions = []
height = 0
width = 0
with open('day13.txt') as file:
    f = file.readlines()
while f[0]!= '\n':
    line = [int(k) for k in f[0].strip('\n').split(',')]
    height = max(height,line[1])
    width = max(width,line[0])
    points.append(line)
    f.pop(0)
f.pop(0)
while len(f)>0:
    t = f[0].strip('\n').split()[2].split('=')
    t[1]= int(t[1])
    instructions.append(t)
    f.pop(0)
print(height)
print(width)
# size+=1
sheet = np.zeros((width+1,height+1))


for point in points:
    sheet[point[0]][point[1]] +=1
sheet = np.transpose(sheet)
for instruction in instructions:
    axis = 0 if instruction[0]=='y' else 1
    fold1,fold2 = np.split(sheet,[instruction[1]],axis)
    fold2 = np.delete(fold2,0,axis)
    sheet = fold1+ np.flip(fold2,axis)
    # break


dots = 0
for i in range(len(sheet)):
    for j in range(len(sheet[i])):
        if sheet[i][j]>0:
            dots+=1

sheet = np.flip(sheet,1)
sheet = np.rot90(sheet)
from PIL import Image
img = Image.new( 'RGB', (len(sheet),len(sheet[0])), "black") # Create a new black image
pixels = img.load() # Create the pixel map
for i in range(len(sheet)):    # For every pixel:
    for j in range(len(sheet[i])):
        if sheet[i][j]>0:
            pixels[i,j] = (0,255,0)
img.show()
print(sheet)
print(dots)