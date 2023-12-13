def OpenFile(dayN):
    print('Leyendo Datos')
    with open('Day ' + str(dayN) + '/input.txt') as f:
        lines = f.readlines()
    
    output = []
    for line in lines:
        new_line = line.strip()
        output.append(new_line)
    return output

def MakeDir(input):
    print("Making dictionary")
    dic = {}
    starting_point = (0,0)
    for y in range(0,len(input)):
        for x in range(0,len(input[0])):
            dic[(x,y)] = input[y][x]
            if(input[y][x] == "S"):
                starting_point = (x,y)
    print("Starting piece at: " + str(starting_point))
    return dic,starting_point

def FindStartingPiece(start,map,pieces):
    points = [(-1,0),(1,0),(0,-1),(0,1)]
    matches = []
    for p in points:
        point = (start[0] + p[0], start[1] + p[1])
        # we check if its in the dictionary
        if point in map.keys():
            #print("Checking point: " + str(point))
            # If it is we check to what that piece connects.. and if its the position of our start
            #  we save it
            piece = map[point]
            for conn in pieces[piece]:
                #print(conn)
                check = (point[0] + conn[0], point[1] + conn[1])
                #print("Checking: " + str(check))
                if( check == start ):
                    matches.append(conn)
                    print("Matches found with piece: " + str(map[point]))

        # We need to invert the array so it can match with our correct outputs
        correct_matches = []
        for m in matches:
            v = (m[0] * -1, m[1] * -1)
            correct_matches.append(v)

        # After that we find what piece it matches
        for key in pieces.keys():
            counter = 0
            for item in correct_matches:
                if(item in pieces[key]):
                    counter += 1
                    if(counter == 2):
                        print("Starting piece is a : " + str(key))
                        map[start] = key
                        return key
                    continue
                else:
                    break

def TraverseLoop(map, p_map, start):
    # We will traverse the loop and increase +1 for each step we do .
    #The result will be steps divided by 2 +- 1
    steps = 1
    # We start to the first point cause why not..
    starting_piece_first_connection = p_map[map[start]][0]
    current_point = (0,0) # we have nothing at 0,0
    last_connection_value_used = (-99,-99)
    # We travel the loop
    while(current_point != start):
        print("On point: " + str(current_point))
        #First iteration
        if(current_point == (0,0)):
            current_point = (start[0] + starting_piece_first_connection[0], start[1] + starting_piece_first_connection[1])
            last_connection_value_used = starting_piece_first_connection
        else:
            connections = p_map[map[current_point]]
            if(tuple(-1 * elem for elem in last_connection_value_used) == connections[0]):
               print("Connects from 0, using 1..")
               current_point = (current_point[0] + connections[1][0], current_point[1] + connections[1][1])
               last_connection_value_used = connections[1]
               steps +=1
            else:
                print("Connects from 1 , using 0")
                current_point = (current_point[0] + connections[0][0], current_point[1] + connections[0][1])
                last_connection_value_used = connections[0]
                steps +=1
    
    print("Done with the loop, steps: " + str(steps/2))
    return


def MakeAPiecesDic():
    dic = {}
    dic["|"] = [(0,1),(0,-1)]
    dic["-"] = [(-1,0),(1,0)]
    dic["L"] = [(0,-1),(1,0)]
    dic["J"] = [(0,-1),(-1,0)]
    dic["7"] = [(-1,0),(0,1)]
    dic["F"] = [(1,0),(0,1)]
    dic["."] = [(-99,-99)]
    return dic


#Main Code
lines = OpenFile(10)
map,start = MakeDir(lines)
d_pieces = MakeAPiecesDic() 
starting_piece = FindStartingPiece(start,map,d_pieces)
TraverseLoop(map, d_pieces, start)

