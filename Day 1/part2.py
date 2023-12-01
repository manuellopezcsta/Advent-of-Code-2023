def OpenFile(dayN):
    print('Leyendo Datos')
    with open('Day ' + str(dayN) + '/input.txt') as f:
        lines = f.readlines()
    for line in lines:
        line.strip()
    return lines

def DecodeLine(line):
    line = line.strip()
    typedNumbers = {"one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7',
                        "eight": '8', "nine": '9'}
    numbers = []

    # Dejamos todo en texto
    for key in typedNumbers.keys():
        line = line.replace(typedNumbers[key], " "+key) # Agregamos un espacio para que no pase el caso
        # ejemplo de tw1nine, q seria 19, pero sin ese espacio seria 219 y se rompe todo.
    #print(line)

    # Buscamos el texto y sacamos las palabras. Importante el usar starts with y no contain. para
    # Evitar duplicados.
    for i in range(0, len(line)):
        cutLine = line[i:i+5] # la palabra mas larga tiene 5 letras.
        for key in typedNumbers.keys():
            if (cutLine.startswith(key)):
                numbers.append(typedNumbers[key])
                break
    cleanedLine = "".join(numbers)
    
    print("Decoded Line, value : "+ cleanedLine)
    return cleanedLine

def BuildNumber(numberString):
    output = "" + numberString[0] + numberString[-1] # -1 is last char
    print("Calibrated value is : " + output)
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







