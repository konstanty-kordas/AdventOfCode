T = []

with open('day10.txt') as file:
    T = [list(i) for i in file.read().split('\n')]
result = 0
scores = []
for line in T:
    # bracketsCount = [0 for i in range(4)]
    corrupted = False
    stack = []
    for character in list(line):
        if character==')':
            if stack[-1] == '(':
                stack.pop()
                continue
            else:
                result+=3
                corrupted = True
                break
        if character==']':
            if stack[-1] == '[':
                stack.pop()
                continue
            else:
                result+=57
                corrupted = True
                break
        if character=='}':
            if stack[-1] == '{':
                stack.pop()
                continue
            else:
                result+=1197
                corrupted = True
                break
        if character=='>':
            if stack[-1] == '<':
                stack.pop()
                continue
            else:
                result+=25137
                corrupted = True
                break
        else:
            stack.append(character)
    if not corrupted:
        score = 0
        stack.reverse()
        for s in stack:
            score*=5
            if s=='(':
                score+=1
            elif s=='[':
                score+=2
            elif s=='{':
                score+=3
            elif s=='<':
                score+=4
        scores.append(score)
import statistics
print(len(scores))
print(statistics.median(scores))
# print(stack)
# print(result)
