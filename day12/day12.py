import copy

nodes = {}
with open('day12.txt') as file:
    for line in file:
        begin,end = line.split('-')
        end = end.strip('\n')
        if begin not in nodes:
            nodes[begin] = []
        if end not in nodes:
            nodes[end] = []
        nodes[begin].append(end)
        nodes[end].append(begin)

paths = []
def f(node,current,twice):
    global nodes
    destinations = nodes[node]
    for d in destinations:
        c = copy.deepcopy(current)
        c.append(d)
        if d=='end':
            paths.append(c)
        elif d==d.lower() and d in current:
            if d=='start' or current.count(d)>1:
                continue
            else:
                if not twice:
                    f(d, c, True)
                else:
                    continue
        else:
            f(d, c,twice)

f('start',['start'],False)

print(len(paths))
