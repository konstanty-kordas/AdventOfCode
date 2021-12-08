TI = []
TO = []
with open('day8.txt') as file:
    for line in file:
        io = line.split('|')
        TI.append([set(k) for k in io[0].split()])
        TO.append([set(k) for k in io[1].split()])
sumAppears = 0
for i in range(len(TO)):
    outNum = ''
    numbers = [set([]) for k in range(10)]
    helper = []
    while sum([len(k) for k in numbers])<45:
        j = 0
        while j<len(TI[i]):
            if numbers[1] and numbers[4]:
                helper = [x for x in numbers[4] if x not in numbers[1]]
                continue
            if len(TI[i][j])==2:
                numbers[1] = TI[i][j]
                TI[i].pop(j)
                continue
            if len(TI[i][j])==3:
                numbers[7] = TI[i][j]
                TI[i].pop(j)
                continue
            if len(TI[i][j])==4:
                numbers[4] = TI[i][j]
                TI[i].pop(j)
                continue
            if len(TI[i][j])==7:
                numbers[8] = TI[i][j]
                TI[i].pop(j)
                continue
            if len(TI[i][j])== 6:
                if numbers[4]:
                    if numbers[4] in TI[i][j]: #WRONG
                        numbers[9] = TI[i][j]
                        TI[i].pop(j)
                        continue
                if numbers[9] and numbers[1]:
                    if numbers[1] in TI[i][j]: #WRONG
                        numbers[0] = TI[i][j]
                        TI[i].pop(j)
                        continue
                if numbers[9] and numbers[0]: 
                    numbers[6] = TI[i][j]
                    TI[i].pop(j)
                    continue
            if len(TI[i][j])== 5:
                if numbers[1]:
                    if numbers[1] in TI[i][j]: #WRONG
                        numbers[3] = TI[i][j]
                        TI[i].pop(j)
                        continue
                if helper:
                    if helper in TI[i][j]:  #WRONG
                        numbers[5] = TI[i][j]
                        TI[i].pop(j)
                        continue
                if numbers[3] and numbers[5]:
                    numbers[2] = TI[i][j]
                    TI[i].pop(j)
                    continue
            j+=1
    print(numbers)
    for j in range(len(TO[i])):
        outNum+=TO[i][j]

print(appears)
