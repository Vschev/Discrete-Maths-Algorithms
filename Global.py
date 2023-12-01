# put your python code here
seq1 = input()
seq2 = input()
out1, out2 = "", ""


#скоры

matched = 1
mismatched = -1
gap = -2

#инициализация

matrix = [[0 for j in range(len(seq1)+1)] for i in range(len(seq2)+1)]
matways = [['' for j in range(len(seq1)+1)] for i in range(len(seq2)+1)]
for j in range(len(matrix[0])):
    matrix[0][j]= -2*j
    matways[0][j] = 'high'
for i in range(len(matrix)):
    matrix[i][0]= -2*i
    matways[i][0]= 'edge'



#заполняет матрицу чисел
    
for row in range(1, len(matrix)):                   
    for col in range(1, len(matrix[row])):
        left = matrix[row][col-1] + gap
        up = matrix[row-1][col] + gap
        if seq1[col-1] == seq2[row-1]:
            diag = matrix[row-1][col-1] + matched
        else:
            diag = matrix[row-1][col-1] + mismatched
        best = max(left,up,diag)
        matrix[row][col] = best

        #проставляет путевые метки
        
        if diag == best:                            
            matways[row][col] = "diag"
        if up == best:
            matways[row][col] = "upup"
        if left == best:
            matways[row][col] = "left"

#возвращается по меткам
            
x, y = len((matrix)[0]) - 1, len(matrix) - 1

while x!=0 and y!=0:
    if matways[y][x] == "diag":
        out2 += seq2[y-1]
        out1 += seq1[x-1]
        x -= 1
        y -= 1
    elif matways[y][x] == "upup":
        out2 += seq2[y-1]
        out1 += "-"
        y -= 1
    elif matways[y][x] == "left":
        out2 += "-"
        out1 += seq1[x-1]
        x -= 1     
#добивает гэпы
        
if x == 0:
    while y!=0:
        out2 += seq2[y-1]
        out1 += "-"
        y -= 1
elif y == 0:
    while x!=0:
        out2 += "-"
        out1 += seq1[x-1]
        x -= 1

#переворачивает строки
        
out1 = out1[::-1]
out2 = out2[::-1]

print(out1)
print(out2)
