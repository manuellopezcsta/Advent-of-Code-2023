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


def GetGearRatios(list):
    #We scan around the * , we save the value, if we find the same value we do nothing
    # if its different we multiply it .
    # When we change to another * we clear the values.
    print("Finding Gear Ratio")
    output = []
    directions = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
    value1 = 9999

    for y in range(0, len(list)):
        for x in range(0,len(list[0])):
            if(list[y][x] == "*"):
                for dir in directions:
                    x_point = x + dir[0]
                    y_point = y + dir[1]
                    point = (x_point,y_point)
                    # First time storing a value
                    if(point in numbers_dic.keys() and value1 == 9999):
                        value1 = numbers_dic[point]
                        #print("Value set to: " + str(value1))
                    if(point in numbers_dic.keys() and numbers_dic[point] != value1):
                        #Si encontramos 2 numeros juntitos!, calculamos el gear
                        print("Se encontro un match entre: " + str(numbers_dic[point]) +  " y " + str(value1))
                        output.append(numbers_dic[point][0] * value1[0])

                        # We clear the numbers from the dic
                        value_on_point = numbers_dic[point]
                        for key in numbers_dic.copy().keys():
                            #print("----------------------------")
                            #print("TESTING KEY> " + str(key))
                            #print("Value 1> " + str(value1) + " POINT> " + str(point))
                            
                            if(numbers_dic[key] == value_on_point or numbers_dic[key] == value1):
                                del numbers_dic[key] # We delete it from the actual dic.
                                #print("Borrando key " + str(key))                             
                # We reset the value.
                        #value1 = 9999
                value1 = 9999
    
    return output


# MAIN CODE

lines = OpenFile(3)
numbers_dic = BuildNumbersMap(lines)
gear_ratios = GetGearRatios(lines)
#print(str(gear_ratios))
result = sum(gear_ratios)
print("The sum of the Gear Ratios is: " + str(result))
