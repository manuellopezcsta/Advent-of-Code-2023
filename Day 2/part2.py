def OpenFile(dayN):
    print('Leyendo Datos')
    with open('Day ' + str(dayN) + '/input.txt') as f:
        lines = f.readlines()
    return lines

def GetGameData(line):
    line = line.strip()
    gameNumber = line.split("Game ")[1].split(":")[0]
    #print(gameNumber)
    #print(gameNumber)
    newLine = line[8:] # We get the quantities
    #print(newLine)
    diffDraws = newLine.split(";")
    #print(diffDraws)
    for game in diffDraws:
        colours = game.split(",")
        red = 0
        green = 0
        blue = 0
        #print(colours)
        for c in colours:
            c = c.strip()
            #print(c)
            c = c.strip()
            if(c[1].isdigit()): # If its a 2 digit number
                number = c[0:2]
                if(c[3] == "b"):
                    blue = number
                elif(c[3] == "r"):
                    red = number
                elif(c[3] == "g"):
                    green = number
            else: # if its a 1 digit number
                number = c[0]
                if(c[2] == "b"):
                    blue = number
                elif(c[2] == "r"):
                    red = number
                elif(c[2] == "g"):
                    green = number
        # We build the result
        playedGames.append((int(gameNumber),int(red),int(green),int(blue)))
            
def GetMinimumCubesPerRun(runNumber):
    red = 0
    blue = 0
    green = 0
    for data in playedGames:
        if (data[0] == runNumber):
            if(data[1] > red):
                red = data[1]
            if(data[2] > green):
                green = data[2]
            if(data[3] > blue):
                blue = data[3]

    output = (runNumber,red,green,blue)
    return output

# Main code
lines = OpenFile(2)

playedGames = []

for line in lines:
    GetGameData(line)

#for i in playedGames:
    #print("Game " + str(i))

n_of_runs = playedGames[len(playedGames) -1][0]
print("Number of runs: " + str(n_of_runs))

multiplied_powers = []

for i in range(1, n_of_runs + 1):
    min = GetMinimumCubesPerRun(i)
    multiplied = min[1] * min[2] * min[3]
    multiplied_powers.append(multiplied)


# We get the final result
result = sum(multiplied_powers)
    
print("The result is: " + str(result))





#gameData = (number, red, green, blue) We use only the max values of each game.





