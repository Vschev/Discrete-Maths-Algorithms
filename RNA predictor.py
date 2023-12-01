rna = input()
ans = {}

def tracing(i = 0, j = len(rna) - 1):
    if matways[i][j] == 'put':
        ans[j] = ')'
        ans[i] = '('
        i += 1
        j -= 1
        tracing(i, j)
    elif isinstance(matways[i][j], list):
        tracing(matways[i][j][0], matways[i][j][1])
        tracing(matways[i][j][2], matways[i][j][3])
    else:
        ans[j] = '.'
        
compl = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}


matrix = [[] for i in range(len(rna))]
matways = [[] for i in range(len(rna))]
for i in range(len(rna)):
    for j in range(len(rna)):
        matrix[i].append(0)
        matways[i].append('?')
        
start = 2
while start < len(rna):
    for j in range (start, len(rna)):
        if compl[rna[j - start]] == rna[j]:
            match = 1
        else:
            match = 0
        best = 0
        next_row = 0
        best_i1 = 0
        best_j1 = 0
        best_i2 = 0
        best_j2 = 0
        for split in range(j - start, j):
            next_row += 1
            subset = matrix[j - start][split] + matrix[j - start + next_row][j]
            if subset >= best:
                best = subset
                best_i1 = j - start
                best_j1 = split
                best_i2 = j - start + next_row
                best_j2 = j
        matrix[j-start][j] = max(best, matrix[j-start+1][j-1] + match)
        if matrix[j-start][j] == best:
            matways[j-start][j] = [best_i1, best_j1, best_i2, best_j2]
        elif matrix[j-start][j] == matrix[j-start+1][j-1] + match:
            matways[j-start][j] = 'put'
    start += 1

tracing()

for a in range(len(rna)):
    if a not in ans:
        ans[a] = '.'

structure = [ans[a] for a in range(len(ans))]
print(''.join(structure))
