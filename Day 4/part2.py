def OpenFile(dayN):
    print('Leyendo Datos')
    with open('Day ' + str(dayN) + '/input.txt') as f:
        lines = f.readlines()
    
    output = []
    for line in lines:
        new_line = line.strip()
        output.append(new_line)
    return output

def BuildResultsDic(list):
    print("Building The starting deck results")
    # We will need to calculate points differently.
    output = {}
    for count, line in enumerate(list, 1): # we tell it to start on 1
        numbers = line.split(": ")[1].split(" |")[0].strip()
        card_numbers = numbers.split(" ")
        clean_cn = remove_items(card_numbers, [" ",""])
        # Now we get the winning numbers
        w_numbers = line.split("| ")[1].strip().split(" ")
        clean_wn = remove_items(w_numbers, [" ",""])
        # We will use the points now to know how much we win per card
        wins = 0
        for num in clean_cn:
            if (num in clean_wn):
                    wins += 1
        # We build the dic entry following this order
        # Key is card N, value is [wins, number_of_cards]
        output[count] = [wins, 1]        
    return output

def remove_items(list, items): 
    # using list comprehension to perform the task
    output = [i for i in list if i not in items]
    return output 

def CalculateWinnings(dic):
    print("Calculating winnings for each card")
    #For each card in the list, we
    for cardN in range(1, len(dic.copy().keys()) + 1):
        # Get the wins
        wins = dic[cardN][0]
        # Add 1 to each of the following cards 
        
        for j in range(0, dic[cardN][1]): # The number of cards
            for i in range(1, wins + 1): # We add 1 to each of the following cards
                value = dic[cardN + i]
                dic[cardN + i] = [value[0], value[1] + 1] # [wins, cardCount]
        
    return dic

def CountTotalCards(dic):
    output = 0
    for key in dic.keys():
        # We just add the wins of all the cards
        output += dic[key][1]
    return output

# Main Code
lines = OpenFile(4)
winnings = BuildResultsDic(lines)
#for key in winnings.keys():
    #print(str(key) + " " + str(winnings[key]))
updated_wins = CalculateWinnings(winnings)
#for key in updated_wins.keys():
    #print(str(key) + " " + str(updated_wins[key]))
result = CountTotalCards(updated_wins)
print("The sum of all cards is: " + str(result))