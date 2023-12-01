# put your python code here
seq1 = input()
seq2 = input()
out1, out2 = "", ""


#скоры

matched = 1
mismatched = -1
fines = input().split()
gap_open = int(fines[0])
gap = int(fines[1])

#инициализация

main = [[0 for j in range(len(seq1)+1)] for i in range(len(seq2)+1)]
upper = [[0 for j in range(len(seq1)+1)] for i in range(len(seq2)+1)]
lower = [[0 for j in range(len(seq1)+1)] for i in range(len(seq2)+1)]
mainways = [['pass' for j in range(len(seq1)+1)] for i in range(len(seq2)+1)]
upperways = [['pass' for j in range(len(seq1)+1)] for i in range(len(seq2)+1)]
lowerways = [['pass' for j in range(len(seq1)+1)] for i in range(len(seq2)+1)]

main[0][0] = gap_open
upper[0][0] = gap_open
lower[0][0] = gap_open

for j in range(1, len(main[0])):
    main[0][j] = main[0][j - 1] + gap
    lower[0][j] = lower[0][j - 1] + gap
    upper[0][j] = float('-inf')
    upperways[0][j] = 'high'

for i in range(1, len(main)):
    main[i][0] = main[i - 1][0] + gap
    lower[i][0] = float('-inf')
    lowerways[i][0] = 'edge'
    upper[i][0] = upper[i - 1][0] + gap
    
main[0][0] = 0
upper[0][0] = float('-inf')
lower[0][0] = float('-inf')

#заполняет матрицу чисел
#проставляет путевые метки
 
for row in range(1, len(main)):                   
    for col in range(1, len(main[row])):
        
        cont = upper[row - 1][col] + gap
        start = main[row - 1][col] + gap_open + gap
        upper[row][col] = max(cont, start)
        
        if upper[row][col] == cont:
            upperways[row][col] = 'cont'
        else:
            upperways[row][col] = 'jump'
            
        cont = lower[row][col - 1] + gap
        start = main[row][col - 1] + gap_open + gap
        lower[row][col] = max(cont, start)
        
        if lower[row][col] == cont:
            lowerways[row][col] = 'cont'
        else:
            lowerways[row][col] = 'jump'
            
        if seq1[col-1] == seq2[row-1]:
            diag = main[row-1][col-1] + matched
        else:
            diag = main[row-1][col-1] + mismatched
        best = max(upper[row][col], lower[row][col], diag)
        main[row][col] = best
        
        if main[row][col] == diag:
            mainways[row][col] = 'diag'
        elif main[row][col] == upper[row][col]:
            mainways[row][col] = 'upup'
        elif main[row][col] == lower[row][col]:
            mainways[row][col] = 'down'

#возвращается по меткам
           
x, y = len((main)[0]) - 1, len(main) - 1
current = "main"

while x!=0 and y!=0:
    if current == "main":
        if mainways[y][x] == "diag":
            out2 += seq2[y-1]
            out1 += seq1[x-1]
            x -= 1
            y -= 1
        elif mainways[y][x] == "upup":
            current = "upper"
        elif mainways[y][x] == "down":
            current = "lower"
    elif current == "upper":
        if upperways[y][x] == 'jump':
            current = "main"
        out2 += seq2[y-1]
        out1 += "-"
        y -= 1
    elif current == "lower":
        if lowerways[y][x] == 'jump':
            current = "main"
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
