def OpenFile(dayN):
    print('Leyendo Datos')
    with open('Day ' + str(dayN) + '/input.txt') as f:
        lines = f.readlines()
    
    output = []
    for line in lines:
        new_line = line.strip()
        output.append(new_line)
    return output



def GetSequences(input):
    otuput = []
    for line in input:
        holder = line.split(" ")
        nums = [int(x) for x in holder]
        otuput.append(nums)
    #print(otuput)
    return otuput

# Python guarda memory como un puntero entonces no lo puedo hacer 
#un array vacio.. lo tengo que crear x defecto como None asi no cambia.
def SolveSequence(seq, memory = None):
    # We implement a memory for recursive calling
    if(memory == None):
        memory = []
        memory.append(seq.copy())
        print("===========================")
        print("Running for the first time..")
        print("S: " + str(seq))
        #memory.append(seq.copy())
    
    holder = []
    for i in range(0,len(seq) - 1):
        v = seq[i+1] - seq[i]
        holder.append(v)
    # If holder its not all 0s, we call it again
    if(len(holder) != holder.count(0)):
        memory.append(holder)
        #print("Running Again on ..." + str(holder))
        return SolveSequence(holder, memory)
    # If it didnt called itself it finished
    print("Finished Sequence")
    memory.append(holder)
    for e in memory:
        print("MEMORY" +  str(e))
    return memory

def ResolveMemories(sequences):
    # We print the sequences to check em
    print(sequences)
    memories = []
    print("Getting the sequences memories..")
    for seq in sequences:
        value = SolveSequence(seq)
        memories.append(value)
    print("===================================")
    print("Solving the sequences memories")
    total = 0
    for count,mem in enumerate(memories):
        # The memories of each sequence
        # Mem is of the type [[],[],[]]
        print("Solving Sequence N" + str(count))

        # We do an inverted loop to solve the arrays inside each memory.
        for i in range(len(mem)-1, -1, -1):
            current_layer = mem[i]
            # We replace the 1st and 2nd memories with 0, and the same value
            if(current_layer.count(0) == len(current_layer)):
                current_layer.append(0)
                #print("Doing case 0")
                continue
            elif(current_layer.count(current_layer[0]) == len(current_layer)):
                current_layer.append(current_layer[0])
                #print("Doing case 1")
                continue
            else:
                #We just add to the current layer the value based on the last layer spot
                previous_layer = mem[i+1]
                value_to_add = previous_layer[-1] + current_layer[-1]
                current_layer.append(value_to_add)
    # AFTER WE SOLVE THEM ALL we sum the values we added to them.
    print("Finished solving them all")
    total = 0
    for mem in memories:
        #print(mem)
        value = mem[0][-1]
        total += value
        print("Adding: " + str(value) + " to the total")
    print("Total equals: " + str(total))




#Main Code
lines = OpenFile(9)
seq = GetSequences(lines)
ResolveMemories(seq)