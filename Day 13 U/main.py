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
    blocks = []
    block = []
    for line in input:
        if(line == ""):
            blocks.append(block)
            block = []
        else:
            block.append(line)
        # For the last line 
        if(input.index(line) == len(line) - 1):
            blocks.append(block)

    return blocks




# Main code
lines = OpenFile(13)
blocks = ParseInput(lines)