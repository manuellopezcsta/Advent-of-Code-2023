def OpenFile(dayN):
    print('Leyendo Datos')
    with open('Day ' + str(dayN) + '/input.txt') as f:
        lines = f.readlines()
    
    output = []
    for line in lines:
        new_line = line.strip()
        output.append(new_line)
    return output

def GetSeeds(input):
    print("Getting seeds")
    holder = input[0].split("seeds: ")[1].split(" ")
    seeds = [int(seed) for seed in holder] # we make them ints
    return seeds

def ParseCategories(input):
    # Ill use flags to tell it where to parse #0 is nothing
    print("Parsing Inputs..")
    seed2soil = [] #1
    soil2fer = [] #2
    fer2water = [] #3
    water2light = [] #4
    light2temp = [] #5
    temp2humi = [] #6
    humi2loca = [] # 7

    parsingLocation = 0
    for line in lines:
        if(line.startswith("seed-to-soil map:")):
            parsingLocation = 1
            continue    # We continue so we dont parse the tittle line
        if(line.startswith("soil-to-fertilizer map:")):
            parsingLocation = 2
            continue
        if(line.startswith("fertilizer-to-water map:")):
            parsingLocation = 3
            continue
        if(line.startswith("water-to-light map:")):
            parsingLocation = 4
            continue
        if(line.startswith("light-to-temperature map:")):
            parsingLocation = 5
            continue
        if(line.startswith("temperature-to-humidity map:")):
            parsingLocation = 6
            continue
        if(line.startswith("humidity-to-location map:")):
            parsingLocation = 7
            continue
        # Now we check if the line is not empty.
        if(line.strip() != "" and parsingLocation != 0):
            # We get all the numbers,
            n_line = line.strip()
            holder = n_line.split(" ")
            numbers = [int(n) for n in holder] # we make them ints
            #We store them accordingly.
            if(parsingLocation == 1):
                seed2soil.append(numbers)
            elif(parsingLocation == 2):
                soil2fer.append(numbers)
            elif(parsingLocation == 3):
                fer2water.append(numbers)
            elif(parsingLocation == 4):
                water2light.append(numbers)
            elif(parsingLocation == 5):
                light2temp.append(numbers)
            elif(parsingLocation == 6):
                temp2humi.append(numbers)
            elif(parsingLocation == 7):
                humi2loca.append(numbers)   

    return seed2soil,soil2fer,fer2water,water2light,light2temp,temp2humi,humi2loca

def SolveSteps(seed):
    #print("Trying to Solve Step 1")
    # We check in each line of coords if we can find the seed location..
    v_soil = -69 # values cant be negative.
    for line in arr1:
        # 0 is the position, 1 start, 2 the range
        if((line[1] + line[2] >= seed) and (line[1] <= seed)): # If we have the seed on this line
            v_soil = (seed - line[1]) + line[0] # (seed- comienzo) + soil
            break
    # If its not in any of the lines its the same value
    if(v_soil == -69):
        v_soil = seed
    #print("Trying to Solve Step 2")
    v_fer = -69
    for line in arr2:
        if(line[1] + line[2] >= v_soil and (line[1] <= v_soil)): 
            v_fer = (v_soil - line[1]) + line[0]
            break
    if(v_fer == -69):
        v_fer = v_soil
    #print("Trying to Solve Step 3")
    v_water = -69
    for line in arr3:
        if(line[1] + line[2] >= v_fer and (line[1] <= v_fer)): 
            v_water = (v_fer - line[1]) + line[0]
            break
    if(v_water == -69):
        v_water = v_fer
    #print("Trying to Solve Step 4")
    v_light = -69
    for line in arr4:
        if(line[1] + line[2] >= v_water and (line[1] <= v_water)): 
            v_light = (v_water - line[1]) + line[0]
            break
    if(v_light == -69):
        v_light = v_water
    #print("Trying to Solve Step 5")
    v_temp = -69
    for line in arr5:
        if(line[1] + line[2] >= v_light and (line[1] <= v_light)): 
            v_temp = (v_light - line[1]) + line[0]
            break
    if(v_temp == -69):
        v_temp = v_light
    #print("Trying to Solve Step 6")
    v_humi = -69
    for line in arr6:
        if(line[1] + line[2] >= v_temp and (line[1] <= v_temp)): 
            v_humi = (v_temp - line[1]) + line[0]
            break
    if(v_humi == -69):
        v_humi = v_temp
    #print("Trying to Solve Step 7")
    v_loca = -69
    for line in arr7:
        if(line[1] + line[2] >= v_humi and (line[1] <= v_humi)): 
            v_loca = (v_humi - line[1]) + line[0]
            break
    if(v_loca == -69):
        v_loca = v_humi
    print('Seed: ' + str(seed) + " Soil: " + str(v_soil) + " Fer: " + str(v_fer)
          + " Water: " + str(v_water) + " Light: " + str(v_light) + " Temp: " + str(v_temp)
          + " Humidity: " + str(v_humi) + " Loca: " + str(v_loca))
    
    return v_loca

def FindClosest(seeds):
    holder = []
    for seed in seeds:
        location = SolveSteps(seed)
        holder.append(location)
    result = min(holder)
    print("The closest location is: " + str(result))

# MAIN CODE
lines = OpenFile(5)
seeds = GetSeeds(lines)
print(seeds)
arr1,arr2,arr3,arr4,arr5,arr6,arr7 = ParseCategories(lines)
#print(arr1)
#print(arr2)
#print(arr3)
#print(arr4)
#print(arr5)
#print(arr6)
#print(arr7)

FindClosest(seeds)