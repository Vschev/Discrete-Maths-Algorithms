import sys

elements = input().split()

neighbours = {}

edges = []
for line in sys.stdin:
    edges.append([int(i) for i in line.split()])
#for i in range(5):
    #edges.append([int(i) for i in input().split()])
    if edges[-1][0] not in neighbours:
        neighbours[edges[-1][0]] = [edges[-1][1]]
    else:
        neighbours[edges[-1][0]].append(edges[-1][1])

answer = []
def Euler(start):
    stack = [start]
    while stack != []:
        v = stack[-1]
        if neighbours[v] == []:
            answer.append(v)
            stack.pop()
        else:
            u = neighbours[v].pop()
            stack.append(u)
    answer.reverse()
    return(answer)

a = Euler(edges[0][0])
a.pop()
b = [str(i) for i in a]
print(' '.join(b))
