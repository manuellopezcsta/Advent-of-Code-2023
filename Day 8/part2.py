def OpenFile(dayN):
    print('Leyendo Datos')
    with open('Day ' + str(dayN) + '/input.txt') as f:
        lines = f.readlines()
    
    output = []
    for line in lines:
        new_line = line.strip()
        output.append(new_line)
    return output

def BuildMapAndInput(input):
    map = {}
    directions = ""
    starting_index = 0
    for i in range(0, len(input)):
        line = input[i].strip()
        if(line != ""):
            directions += line
        else:
            starting_index = i + 1
            break 

    print("Starting index:" + str(starting_index))

    for i in range(starting_index,len(input)):
        line = input[i].strip()
        key = line.split(" =")[0]
        # We make the tuple
        holder = line.split("= ")[1].replace("("," ").replace(")","").replace(",", "")
        my_choices = (holder.split(" "))[1:]
        # We save it in the dictionary.
        map[key] = my_choices
    return directions, map

def FindStartNodes(map):
    output = []
    for key in map.keys():
        if(key.endswith("A")):
            output.append(key)
    print("Starting keys: " + str(output))
    return output


def CountSteps(startNode,dir,map):
    output = 0
    dir_array = [x for x in dir]
    backupArray = dir_array.copy()
    node = startNode
    while(not node.endswith("Z")):
        # If the array is 0, we rebuild it.
        if(len(dir_array) == 0):
            #print("rellenando a : " + str(len(backupArray)))
            dir_array = backupArray.copy()
        # We check the direction and pop the first element of the array
        value = dir_array.pop(0)
        if(value == "L"): # We go left
            node = map[node][0]
            output += 1
        elif(value == "R"):
            node = map[node][1]
            output += 1
        else:
            print("ERROOOOOOOOOR")
    print("Se encontro la salida en " + str(output) + " pasos.")
    return output

def FindMCM(startingNodes, directions, map):
    # Stuff to calculate it
    def __gcd(a, b):
        if (a == 0):
            return b
        return __gcd(b % a, a)
    
    # recursive implementation
    def LcmOfArray(arr, idx):
    
        # lcm(a,b) = (a*b/gcd(a,b))
        if (idx == len(arr)-1):
            return arr[idx]
        a = arr[idx]
        b = LcmOfArray(arr, idx+1)
        return int(a*b/__gcd(a,b)) # __gcd(a,b) is inbuilt library function
    # This code is contributed by divyeshrabadiya07.

    output = 1
    result = []
    for node in starting_nodes:
        value = CountSteps(node,directions,map)
        result.append(value)
    # We get the minimo comun multiplo.
    output = LcmOfArray(result, 0)
    return output

    

    

#Main Code
lines = OpenFile(8)
directions, map = BuildMapAndInput(lines)
print("Dir: " + str(directions))

#for key in map:
#    print("Key: " + str(key) + " value: " + str(map[key]))

starting_nodes = FindStartNodes(map)

result = FindMCM(starting_nodes, directions, map)
print("The result of the MCM is: " + str(result))