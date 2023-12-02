def OpenFile(dayN):
    print('Leyendo Datos')
    with open('Day ' + str(dayN) + '/input.txt') as f:
        lines = f.readlines()
    for line in lines:
        line.strip()
    return lines


def DecodeLine(line):
    line = line.strip()
    numbers = []
    #Creamos un string nuevo que elimina las que no son digitos. 
    cleanedLine = ''.join(filter(str.isdigit, line))
    print("Decoded Line, value : " + cleanedLine)
    return cleanedLine

def BuildNumber(numberString):
    output = "" + numberString[0] + numberString[-1] # -1 is last char
    print("Result number is : " + output)
    return output

def SumAllCoords(numbers):
    output = 0
    for n in numbers:
        output += int(n)
    print("Final result is: " + str(output))
    return output





input = OpenFile(1)

numbers = []
for line in input:
    numbers.append(DecodeLine(line))

results = []
for n in numbers:
    results.append(BuildNumber(n))

SumAllCoords(results)








