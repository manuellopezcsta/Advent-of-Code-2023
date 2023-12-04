def OpenFile(dayN):
    print('Leyendo Datos')
    with open('Day ' + str(dayN) + '/input.txt') as f:
        lines = f.readlines()
    
    output = []
    for line in lines:
        new_line = line.strip()
        output.append(new_line)
    return output

def BuildNumbersMap(list):
    # We build a coord system with each number and we give each one an id, to delete later
    # After we use it.. without the id, we could have twice the same number and it would
    # delete em both.
    print("Finding Numbers")
    print("X LEN: " + str(len(list[0])))
    print("Y LEN: " + str(len(list)))
    numbers_dic = {}
    holder= ""
    start = (9999,9999)
    end = (0,0)
    id = 0
    for y in range(0, len(list)):
        for x in range(0,len(list[0])):
            #print("PUNTO: " + str((x,y)))
            # If we find a number
            if(list[y][x].isdigit()):
                holder += (list[y][x])
                end = (x,y)
                #print("END: " + str(end))
                if(start == (9999,9999)):
                    start = (x,y)
                    #print("START: " + str(start))
                # IF ITS END OF LINE WE SAVE IT..
                if(x == len(list[0]) -1):
                    for j in range(start[0],end[0] + 1):
                        #print("HOLDER> " + str(holder) + " id: " + str(id))
                        numbers_dic[(j,start[1])] = (int(holder), id)
                        #print("Saved a point at: " + str((j,start[1])))
                    holder = ""
                    start = (9999,9999)
                    end = (0,0)
                    id += 1
                    
            else:
                # We save it and replace holder // if it finds another thing thats not a number
                if(end != (0,0) and holder != ""):
                    #print("START: " + str(start))
                    for j in range(start[0],end[0] + 1):
                        #print("HOLDER> " + str(holder) + " id: " + str(id))
                        numbers_dic[(j,start[1])] = (int(holder), id)
                        #print("Saved a point at: " + str((j,start[1])))
                    holder = ""
                    start = (9999,9999)
                    end = (0,0)
                    id += 1
    print("Saved a total of: " + str(len(numbers_dic.keys())) + " keys.")
                       
    return numbers_dic


def FindTouchingNumbers(list):
    print("Finding Touching Numbers..")
    directions = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
    output = []

    for y in range(0, len(list)):
        for x in range(0,len(list[0])):
            # If we find a symbol
            if(not list[y][x].isdigit() and list[y][x] != "."):
                for dir in directions:
                    x_point = x + dir[0]
                    y_point = y + dir[1]
                    point = (x_point,y_point)
                    #print("POINT> " + str(point) + " is in dic? " + str(point in numbers_dic.keys()))
                    # If it touches the point and its in the dictionary.
                    if(point in numbers_dic.keys()):
                        value_to_append = numbers_dic[point]
                        output.append(value_to_append)
                        # We clear the result from the dictionary..
                        for key in numbers_dic.copy().keys():
                            if(numbers_dic[key] == value_to_append):
                                del numbers_dic[key] # We delete it from the actual dic.
            else:
                continue
    return output

def SumUpTheResult(listOfTuples):
    output = 0
    for item in listOfTuples:
        output += item[0]
    return output




# MAIN CODE

lines = OpenFile(3)
numbers_dic = BuildNumbersMap(lines)
touched_numbers = FindTouchingNumbers(lines)
print(str(touched_numbers))
result = SumUpTheResult(touched_numbers)
print("The sum of the numbers is: " + str(result))
