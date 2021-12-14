from collections import Counter
import pprint
import copy
rules = {}
polymer = ''
unique = set()
with open('day14.txt') as file:
    polymer = file.readline().strip('\n')
    for line in file.readlines():
        if line!='\n':
            rule = line.strip('\n').split(' -> ')
            rules[rule[0]] = rule[1]
            unique.add(rule[1])

# print(len(unique))
descriptors = list(unique)
descriptors.sort()
population = [[0 for i in range(len(unique))] for j in range(len(unique))]
# print(descriptors)
for i in range(len(polymer)-1):
    duo = ''.join([polymer[i],polymer[i+1]])
    population[descriptors.index(polymer[i])][descriptors.index(polymer[i+1])]+=1
# pprint.pprint(population)


rules2 = {}
for i in sorted(rules):
    rules2[i] = rules[i]
rules = rules2
# print(rules)

# exit()

for day in range(10**4):
    newPolymer = list(polymer)
    nextPopulation = copy.deepcopy(population)
    for i in range(len(unique)):
        for j in range(len(unique)):
            if population[i][j]>0:
                duo = ''.join([descriptors[i],descriptors[j]])
                # print(duo)
                # print(rules[duo])
                nextPopulation[i][j]-=population[i][j]
                nextPopulation[descriptors.index(duo[0])][descriptors.index(rules[duo])]+=population[i][j]
                nextPopulation[descriptors.index(rules[duo])][descriptors.index(duo[1])]+=population[i][j]
    population = copy.deepcopy(nextPopulation)
    # j=0
    # shift = 0
    # while j<len(polymer)-1:
    #     duo = ''.join([polymer[j],polymer[j+1]])
    #     if  duo in rules:
    #         newPolymer.insert(j+1+shift,rules[duo])
    #         shift +=1
    #     j+=1
    # polymer = ''.join(newPolymer)
    # print(polymer)
    # pprint.pprint(population)
    # print(c.most_common())
# pprint.pprint(population)
c2 = []
for p in population:
    c2.append(sum(p))
c3 = []
for i in range(len(population)):
    c3.append(0)
    for j in range(len(population[i])):
        c3[i] += population[j][i]
c4 = []
for i in range(len(c2)):
    c4.append(max(c2[i],c3[i]))
# print(c2)
# print(sum(c3))
print(max(c4)-min(c4))
c = Counter(polymer)

# print(c.most_common()[0][1]-c.most_common()[-1][1])

