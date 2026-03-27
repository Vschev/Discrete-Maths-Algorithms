# put your python code here
stayP = 0.9
stayN = 0.8
changeP_N = 0.1
changeN_P = 0.2

emitP = {'A': 0.1, 'T': 0.1, 'G': 0.4, 'C': 0.4}
emitN = {'A': 0.3, 'T': 0.3, 'G': 0.2, 'C': 0.2}

#State: after the letter is emitted, but before promoter change!
current_state = [[0.5, 'P', 'start'], [0.5, 'N', 'start']]
tracer = []

seq = list(input())
for char in range(len(seq)):
    nucl = seq[char]
    
    # new state: checks if the last one is P or NP in order to emit a letter
    for i in current_state:
        if i[1] == 'P':
            i[0] = i[0] * emitP[nucl]
        elif i[1] == 'N':
            i[0] = i[0] * emitN[nucl]

    # Adds a new observed state  
    tracer.append([])
    for i in current_state:
        tracer[-1].append(i.copy())

    # tracker, shows where we came from
    for l in range(len(current_state)):
        current_state[l][2] = l

    # creates a duplicate to change the hidden state; fills the "P -> P or N -> N" situations
    double = []
    for i in current_state:
        double.append(i.copy())
        if i[1] == 'P':
            i[0] = i[0] * stayP
        elif i[1] == 'N':
            i[0] = i[0] * stayN

    # fills the "P -> N or N -> P" situations
    for i in double:
        if i[1] == 'P':
            i[0] = i[0] * changeP_N
            i[1] = 'N'
        elif i[1] == 'N':
            i[0] = i[0] * changeN_P
            i[1] = 'P'

    # Gathers all possible options for a new observed state
    for i in double:
        current_state.append(i.copy())

annot = []
state = []
for i in tracer[-1]:
    state.append(i[0])
prob = max(state)
for i in tracer[-1]:
    if i[0] == prob:
        annot.append(i[1])
        track = i[2]
for l in range(len(tracer)-2, -1, -1):
    annot.append(tracer[l][track][1])
    track = tracer[l][track][2]

annot.reverse()
print(''.join(annot))
