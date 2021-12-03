import copy

def mostCommon(H):
    zeros = [0 for r in range(len(H[0]))]
    for i in range(len(H)):
        for j in range(len(H[i])):
            if T[i][j]==0:
                zeros[j]+=1
    print(zeros)
    return zeros

T = []

with open('3.txt') as file:
    T = [[int(k) for k in list(l)[:-1]] for l in file.readlines()]
gamma = ''
epsilon = ''

zerosT = mostCommon(T)
for i in range(len(zerosT)):
    gamma += "0" if zerosT[i]>500 else "1"
    epsilon += "1" if zerosT[i]>500 else "0"

# print(int(epsilon,2)*int(gamma,2))



M = copy.deepcopy(T)
oxy = 0
for j in range(len(gamma)):
    if len(M)==1:
        break
    zerosM = mostCommon(M)
    if len(M)//2 !=len(M)/2:
        common=1
    else:
        common = 0 if zerosM[j]>len(M)/2 else 1
    print(common)
    i=0
    while i < len(M):
        if M[i][j] != common:
            M.pop(i)
        else:
            i+=1


oxy = int(''.join([str(r) for r in M[0]]),2)
print(oxy)

M = copy.deepcopy(T)
co2 = 0
for j in range(len(epsilon)):
    if len(M)==1:
        break
    zerosM = mostCommon(M)
    if len(M)//2 !=len(M)/2:
        common=0
    else:
        common = 1 if zerosM[j]>len(M)/2 else 0
    i=0
    while i < len(M):
        if M[i][j] != common:
            M.pop(i)
        else:
            i+=1
    
# print(''.join([str(r) for r in M[0]]))
co2 = int(''.join([str(r) for r in M[0]]),2)
print(co2)
print(oxy*co2)
