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
            
def CombineAndLeaveOnlyValidRuns(list):
    max_red = 12
    max_green = 13
    max_blue = 14
    n_of_runs = list[len(list) -1][0]
    bad_run_numbers = set() # We use a set to avoid repeats.
    
    # Encontramos los malos que no cumplen el criterio
    for data in list:
        if(data[1] > max_red): #red
            bad_run_numbers.add(data[0])
            continue
        if(data[2] > max_green): #green
            bad_run_numbers.add(data[0])
            continue
        if(data[3] > max_blue): #blue
            bad_run_numbers.add(data[0])
            continue

    # Los filtramos
    validRuns = []

    for data in list:
        if(data[0] not in bad_run_numbers):
            validRuns.append(data)        

    #print(validRuns)

    # We create a set with only the numbers of the correct runs
    good_run_numbers = set()
    for i in range(1, n_of_runs + 1):
        if(i not in bad_run_numbers):
            good_run_numbers.add(i)
    print("N of runs: " + str(n_of_runs))
    print("BAD: " + str(bad_run_numbers))
    print("GOOD: " + str(good_run_numbers))

    return validRuns, good_run_numbers






# Main code
lines = OpenFile(2)

playedGames = []

for line in lines:
    GetGameData(line)

#for i in playedGames:
    #print("Game " + str(i))

validRuns, goodRuns = CombineAndLeaveOnlyValidRuns(playedGames)

result = sum(goodRuns)
print("The result is: " + str(result))





#gameData = (number, red, green, blue) We use only the max values of each game.





