def OpenFile(dayN):
    print('Leyendo Datos')
    with open('Day ' + str(dayN) + '/input.txt') as f:
        lines = f.readlines()
    
    output = []
    for line in lines:
        new_line = line.strip()
        output.append(new_line)
    return output

def FindMinimumLocation(input):
    location = 0
    print("Trying to bruteforce winner seed")
    holder = input[0].split("seeds: ")[1].split(" ")
    n_holder = [int(seed) for seed in holder] # we make them ints

    while(True):
        # We get a value
        testValue = ReverseSteps(location, False)
        # We check it vs the ranges we have

        for i in range(0, len(n_holder), 2): # Will do 0,2,4 etc..
            ranged = n_holder[i+1]
            # If our seed its inside the range
            if(testValue >= n_holder[i] and testValue <= n_holder[i] + ranged - 1):
                print("Seed found!, the minimum location is: " + str(location))
                return location
            
        # If we fail we increase the output by 1 and try again..
        location += 1
        if(location % 50000 == 0):
            print("Atempting Seed " + str(location))
    

def ParseCategories():
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

def ReverseSteps(location, print_seed):
    #print("Trying to Solve Step 7")
    v_humi,v_temp, v_light,v_water,v_fer,v_soil,v_seed = -69,-69,-69,-69,-69,-69,-69
    for line in arr7:
        if(line[0] + line[2] -1 >= location and (line[0] <= location)):    
            v_humi = (location - line[0]) + line[1]
            break
    if(v_humi == -69):
        v_humi = location
    #print("Trying to Solve Step 6")
    for line in arr6:
        if(line[0] + line[2] -1 >= v_humi and (line[0] <= v_humi)):    
            v_temp = (v_humi - line[0]) + line[1]
            break
    if(v_temp == -69):
        v_temp = v_humi
    #print("Trying to Solve Step 5")
    for line in arr5:
        if(line[0] + line[2] -1 >= v_temp and (line[0] <= v_temp)):    
            v_light = (v_temp - line[0]) + line[1]
            break
    if(v_light == -69):
        v_light = v_temp
    #print("Trying to Solve Step 4")
    for line in arr4:
        if(line[0] + line[2] -1 >= v_light and (line[0] <= v_light)):    
            v_water = (v_light - line[0]) + line[1]
            break
    if(v_water == -69):
        v_water = v_light
    #print("Trying to Solve Step 3")
    for line in arr3:
        if(line[0] + line[2] -1 >= v_water and (line[0] <= v_water)):    
            v_fer = (v_water - line[0]) + line[1]
            break
    if(v_fer == -69):
        v_fer = v_water
    #print("Trying to Solve Step 2")
    for line in arr2:
        if(line[0] + line[2] -1 >= v_fer and (line[0] <= v_fer)):    
            v_soil = (v_fer - line[0]) + line[1]
            break
    if(v_soil == -69):
        v_soil = v_fer
    #print("Trying to Solve Step 1")
    for line in arr1:
        if(line[0] + line[2] -1 >= v_soil and (line[0] <= v_soil)):    
            v_seed = (v_soil - line[0]) + line[1]
            break
    if(v_seed == -69):
        v_seed = v_soil
    if(print_seed):
        print('Seed: ' + str(v_seed) + " Soil: " + str(v_soil) + " Fer: " + str(v_fer)
            + " Water: " + str(v_water) + " Light: " + str(v_light) + " Temp: " + str(v_temp)
            + " Humidity: " + str(v_humi) + " Loca: " + str(location))
    
    return v_seed


# MAIN CODE
lines = OpenFile(5)
arr1,arr2,arr3,arr4,arr5,arr6,arr7 = ParseCategories()
location = FindMinimumLocation(lines)
# We just print it to have it
result = ReverseSteps(location,True)