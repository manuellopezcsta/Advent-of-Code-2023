def OpenFile(dayN):
    print('Leyendo Datos')
    with open('Day ' + str(dayN) + '/input.txt') as f:
        lines = f.readlines()
    # We strip spaces
    output = []
    for line in lines:
        new_line = line.strip()
        output.append(new_line)
    return output


# For building 2D grids.
def Build2DMap(list):
    print("Building Dic")
    print("X LEN: " + str(len(list[0])))
    print("Y LEN: " + str(len(list)))
    dic = {}
    for y in range(0, len(list)):
        for x in range(0,len(list[0])):
            print(str(x) + " " + str(y))
            dic[(x,y)] = list[y][x]
    return dic

# For removing repeats of an item from a list, for example spaces..
def remove_items(list, items): 
    # using list comprehension to perform the task
    output = [i for i in list if i not in items]
    return output 