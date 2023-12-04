def OpenFile(dayN):
    print('Leyendo Datos')
    with open('Day ' + str(dayN) + '/input.txt') as f:
        lines = f.readlines()
    
    output = []
    for line in lines:
        new_line = line.strip()
        output.append(new_line)
    return output

def GetWinnings(list):
    # We will need to calculate points differently.
    output = []
    for line in list:
        numbers = line.split(": ")[1].split(" |")[0].strip()
        card_numbers = numbers.split(" ")
        clean_cn = remove_items(card_numbers, [" ",""])
        # Now we get the winning numbers
        w_numbers = line.split("| ")[1].strip().split(" ")
        clean_wn = remove_items(w_numbers, [" ",""])
        # We get the points
        points = 0
        for num in clean_cn:
            if (num in clean_wn):
                if(points == 0):
                    points += 1
                else:
                    points = points*2
        # We store the points result
        output.append(points)
        #print("NUMS " + str(clean_cn))
        #print("W NUM " + str(clean_wn))
    return output

def remove_items(list, items): 
    # using list comprehension to perform the task
    output = [i for i in list if i not in items]
    return output 

# Main Code
lines = OpenFile(4)
winnings = GetWinnings(lines)
print(winnings)
result = sum(winnings)
print("The sum of all winnings is: " + str(result))