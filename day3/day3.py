import copy

def mostCommon(H):
    zeros = [0 for r in range(len(H[0]))]
    for i in range(len(H)):
        for j in range(len(H[i])):
            if T[i][j]==0:
                zeros[j]+=1
    # print(zeros)
    return zeros

T = []

with open('day3.txt') as file:
    for line in file.readlines():
        T.append([int(k) if k!= '\n' else None for k in list(line)]) #= [[int(k) for k in list(l)] for l in file.readlines()]
gamma = ''
epsilon = ''
for i in range(len(T)):
    for j in range(len(T[i])):
        if T[i][j] == None:
            T[i].pop(j)
zerosT = mostCommon(T)
for i in range(len(zerosT)):
    gamma += "0" if zerosT[i]>500 else "1"
    epsilon += "1" if zerosT[i]>500 else "0"

# print(int(epsilon,2)*int(gamma,2))


M = copy.deepcopy(T)
# oxy = 0
for j in range(len(T[0])):
    if len(M)==1:
        break
    zeros = 0
    ones = 0
    for i in range(len(M)):
        if M[i][j] == 0:
            zeros+=1
        else:
            ones+=1
    common = 0 if zeros>ones else 1
    i=0
    while i < len(M):
        if len(M)==1:
            break
        if M[i][j] != common:
            M.pop(i)
        else:
            i+=1

oxy = int(''.join([str(r) for r in M[0]]),2)
print(oxy)





M = copy.deepcopy(T)
for j in range(len(T[0])):
    if len(M)==1:
        break
    zeros = 0
    ones = 0
    for i in range(len(M)):
        if M[i][j] == 0:
            zeros+=1
        else:
            ones+=1
    common = 0 if ones>=zeros else 1
    i=0
    while i < len(M):
        if len(M)==1:
            break
        if M[i][j] != common:
            M.pop(i)
        else:
            i+=1
co2 = int(''.join([str(r) for r in M[0]]),2)
print(co2)

print(co2*oxy)
# M = copy.deepcopy(T)
# co2 = 0
# for j in range(len(epsilon)):
#     if len(M)==1:
#         break
#     zerosM = mostCommon(M)
#     if len(M)//2 !=len(M)/2:
#         common=0
#     else:
#         common = 1 if zerosM[j]>len(M)/2 else 0
#     i=0
#     while i < len(M):
#         if M[i][j] != common:
#             M.pop(i)
#         else:
#             i+=1
    
# # print(''.join([str(r) for r in M[0]]))
# co2 = int(''.join([str(r) for r in M[0]]),2)
# print(oxy*co2)
