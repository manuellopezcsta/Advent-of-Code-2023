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
    times = lines[0].split("Time:")[1].strip().split(" ")
    n_times = remove_items(times,"")
    distance = lines[1].split("Distance:")[1].strip().split(" ")
    n_distance = remove_items(distance,"")
    print(n_times)
    print(n_distance)
    output = []
    for i in range(0, len(n_times)):
        output.append((int(n_times[i]), int(n_distance[i])))
    return output


def remove_items(list, items): 
    # using list comprehension to perform the task
    output = [i for i in list if i not in items]
    return output 

def GetPosibleWinSituations(race):
    wins = 0
    time, dis = race[0], race[1]
    for t_pressed in range(1, time): # We dont count case 0 and case full press cause it makes no sense.
        t_remaining = time - t_pressed
        if(t_remaining * t_pressed > dis):
            wins += 1
    print("Finished race " + str(race) + " with a total of " + str(wins) + " wins.")
    return wins

def MultiplyThevalues():
    result = 1
    for race in races:
        wins = GetPosibleWinSituations(race)
        result *= wins
    print("The result is: " + str(result))


# Main Code
lines = OpenFile(6)
races = ParseRaces(lines)
print(races) # (time, distance)
# We solve it
MultiplyThevalues()

