T = []
with open('day6.txt') as file:
    T = [int(f) for f in file.read().split(',')]
mod = [0 for j in range(9)]
for fish in T:
    mod[fish%7]+=1
for day in range(2**8):
    current = mod[0]
    for i in range(1,len(mod)):
        mod[i-1] = mod[i]
    mod[6]+=current
    mod[8]=current
print(sum(mod))

