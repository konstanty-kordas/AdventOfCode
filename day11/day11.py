def flash(T,oi,oj,N,M,flashed):
    flashed[oi][oj]=True
    for i in range(max(0,oi-1),min(oi+2,N)):
        for j in range(max(0,oj-1),min(oj+2,M)):
            if i==oi and j==oj:
                continue
            T[i][j]+=1
            if T[i][j]>9 and not flashed[i][j]:
                flash(T,i,j,N,M,flashed)

octopuses = []
countFlashes = 0
with open('day11.txt') as file:
    for line in file:
        octopuses.append([int(i) for i in list(line) if i!= '\n'])
N = len(octopuses)
M = len(octopuses[0])
day=1
while True:
    for i in range(N):
        for j in range(M):
            octopuses[i][j]+=1
    flashed = [[False for k in range(M)] for l in range(N)]

    for i in range(N):
        for j in range(M):
            if octopuses[i][j]>9 and not flashed[i][j]:
                flash(octopuses,i,j,N,M,flashed)
    flashesSynched = 0
    for i in range(N):
        for j in range(M):
            if flashed[i][j]:
                flashesSynched+=1
                countFlashes+=1
                octopuses[i][j]=0
    if flashesSynched==N*M:
        break
    day+=1
for i in range(N):
    for j in range(M):
        print(octopuses[i][j], end=' ')
    print('')
print(countFlashes)
print(day)