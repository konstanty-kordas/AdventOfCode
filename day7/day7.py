import numpy as np
import math
def f(n):
    x = n*(n+1)/2
    return x
crabs = []
with open('day7.txt') as file:
    crabs = np.array([int(c) for c in file.read().split(',')])
value = np.median(crabs)

smallest = min(crabs)
biggest = max(crabs)
result = math.inf
pos=0
for v in range(smallest, biggest):
    cost = 0
    for crab in crabs:
        cost+=f(abs(v-crab))
    result = min(result,cost)
    if result==cost:
        pos=v
print(result)
print(pos)