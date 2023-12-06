def OpenFile(dayN):
    print('Leyendo Datos')
    with open('Day ' + str(dayN) + '/input.txt') as f:
        lines = f.readlines()
    
    output = []
    for line in lines:
        new_line = line.strip()
        output.append(new_line)
    return output

def ParseRaces(lines):
    time = lines[0].split("Time:")[1].strip().replace(" ","")
    distance = lines[1].split("Distance:")[1].strip().replace(" ","")
    print(time)
    print(distance)
    output = (int(time), int(distance))
    return output


def remove_items(list, items): 
    # using list comprehension to perform the task
    output = [i for i in list if i not in items]
    return output 

def GetPosibleWinSituations(race):
    print("Calculating wins..")
    wins = 0
    time, dis = race[0], race[1]
    for t_pressed in range(1, time): # We dont count case 0 and case full press cause it makes no sense.
        t_remaining = time - t_pressed
        if(t_remaining * t_pressed > dis):
            wins += 1
    print("Finished race " + str(race) + " with a total of " + str(wins) + " wins.")
    return wins




# Main Code
lines = OpenFile(6)
race = ParseRaces(lines)
print(race) # (time, distance)
wins = GetPosibleWinSituations(race)
# We solve it


