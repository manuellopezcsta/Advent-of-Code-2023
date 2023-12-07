def OpenFile(dayN):
    print('Leyendo Datos')
    with open('Day ' + str(dayN) + '/input.txt') as f:
        lines = f.readlines()
    
    output = []
    for line in lines:
        new_line = line.strip()
        output.append(new_line)
    return output

def GetHandsAndBids(lines):
    hands = {}
    for line in lines:
        cards = line.strip().split(" ")[0]
        bid = line.strip().split(" ")[1]
        hands[cards] = int(bid) 
        #print(str(cards) + " " + str(bid))
    return hands

def GetHandType(cards):
    # We analyze the card counts and we can find which hand it is..
    # We return a number according to the hand type
    handValue = []
    # We count how many times each hand appears
    for c in cards:
        handValue.append(cards.count(c))
    #We sort them to compare them to different hands
    handValue.sort()
    if(handValue == [1,1,1,1,1]): # High Card
        print(str(cards) + " High Card")
        return 1
    if(handValue == [1,1,1,2,2]): # One Pair
        print(str(cards) + " One Pair")
        return 2
    if(handValue == [1,2,2,2,2]): # Two Pair
        print(str(cards) + " Two Pair")
        return 3
    if(handValue == [1,1,3,3,3]): # Three of a Kind
        print(str(cards) + " Three of a Kind")
        return 4
    if(handValue == [2,2,3,3,3]): # Full House
        print(str(cards) + " Full House")
        return 5
    if(handValue == [1,4,4,4,4]): # Four of a Kind
        print(str(cards) + " Four of a Kind")
        return 6
    if(handValue == [5,5,5,5,5]): # Five of a Kind
        print(str(cards) + " Five of a Kind")
        return 7
    else:
        print("ERROOOOOOOOOOOOOR")
        return 0

def ValueAndOrder(hands):
    print("Ordering the cards by value")
    max_points = len(hands)
    print("Max Points: " + str(max_points))
    output = []
    for h in hands:
        value = GetHandType(h)
        output.append((h, value)) # we append a tuple so we can sort em by value and check the bid by the h
    output.sort(key=lambda x: x[1], reverse = True)
    #print("OUTPUT VAO: " + str(output))

    # We now how to check for each type if 2 have the same for priorities and reorder them.
    for i in range(1,8): # we value them from 1 to 7
        checking_list = list(map(lambda x: x[1], output))
        # We check if its even in the list, if not we continue to the next
        if i not in checking_list:
            continue
        # If we find only 1 element of that type of hand
        if(checking_list.count(i) == 1):
            continue
        # If there are multiples
        else:
            start_index = checking_list.index(i)
            # Reverse the array and find the index of the first occurrence of "i"
            # which will be the last...
            end_index = len(checking_list) - checking_list[::-1].index(i) - 1
            # We make a new list with this values to organize them
            holder = list(map(lambda x: x[0], output))
            reorganize_list = holder[start_index:end_index + 1]
            # We compare the same cards and reorder them
            result = CompareCardsOfTheSame(reorganize_list)
            # We replace them in the deck 
            for j in range(start_index, end_index +1):
                output[j] = (result[0], i)
                result.pop(0)

    return output

def CompareCardsOfTheSame(deck):
    print("Comparing and ordering cards...")
    # Deck is an array of hands
    prio = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]
    deck_values = []

    # We build the hands values
    for hands in deck:
        hand_values = []
        for c in hands:
            value = prio.index(c)
            hand_values.append(value)
        deck_values.append((hands, hand_values, 0))
        

    # We compare all of them, if they are the same we go to the next, if not the smaller one wins
    # After all the comparations, we order them by points

    for k in range(0, len(deck_values)):
        hand1 = deck_values[k]
        for j in range(0, len(deck_values)):
            hand2 = deck_values[j]

            #If its the same hand we skip
            if(hand1[0] == hand2[0]):
                continue
            # We compare the hands char by char
            for i in range(0, len(hand1[1])):
                if(hand1[1][i] == hand2[1][i]):
                    continue
                else:
                    if(hand1[1][i] > hand2[1][i]):
                        # Hand 2 wins
                        hand2 = (hand2[0], hand2[1], hand2[2] + 1) # hand is ("LETTERS,values,order")
                        deck_values[j] = hand2
                        break
                    else:
                        # Hand 1 wins
                        hand1 = (hand1[0], hand1[1], hand1[2] + 1)
                        deck_values[k] = hand1
                        break
            
    
    # After rating the cards, we can order them based on the new order values we generated
    deck_values.sort(key=lambda x: x[2], reverse = True)
    # We create an output with only the card names
    output = list(map(lambda x: x[0], deck_values))
    #print(output)
    return output    

def GetTotalWinnings(deck,dic):
    # The rank equals the i, and the bid we get from the dic..
    # We just add it to a total
    total = 0
    #print(deck)
    for i in range(len(deck), 0, -1):
        bid = dic[deck[len(deck) - i][0]]
        #print("Adding " + str(bid * i) + " to total.")
        total += (bid * i)
    print("Total is: " + str(total))


#Main code

lines = OpenFile(7)
hands = GetHandsAndBids(lines)
ordered_hands = ValueAndOrder(hands)
#print(ordered_hands)
#test = [ "AAAA6","AAAA3","AAAA4","AAAA5","AAAAK","AAAAQ"]
#sorted_test = CompareCardsOfTheSame(test)
GetTotalWinnings(ordered_hands, hands)


