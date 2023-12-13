def OpenFile(dayN):
    print('Leyendo Datos')
    with open('Day ' + str(dayN) + " U" + '/input.txt') as f:
        lines = f.readlines()
    
    output = []
    for line in lines:
        new_line = line.strip()
        output.append(new_line)
    return output


def ParseInput(input):
    for line in input:
        p1 = line.split(" ")[0]
        print(p1)
        p2 = line.split(" ")[1].split(",")
        print(p2)




# Main code
lines = OpenFile(12)
ParseInput(lines)