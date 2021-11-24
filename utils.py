def printNumbersAsSudokuBoard(numbers):
    newLine = "\n"
    columnSeparator = "\t"
    numberSeparator = " "
    horizontalCells = 3
    hLen = 3
    vLen = 3

    horizontalLine = ""

    cellStart = 0
    cellEnd = 0

    cellHeight = 0

    while (cellEnd < len(numbers)):

        for hCell in range(0, horizontalCells):
            cellStart = cellEnd
            cellEnd += hLen

            cellLine=""
            for number in numbers[cellStart:cellEnd]:
                
                cellLine += number
                if(len(cellLine) <= hLen):
                    cellLine += numberSeparator

            horizontalLine+=cellLine
            if hCell <= horizontalCells:
                horizontalLine+=columnSeparator
        
        horizontalLine+=newLine
        cellHeight+=1

        if(cellHeight == vLen):
            horizontalLine+=newLine
            cellHeight=0

    print(horizontalLine)   

def getNumberList(string):
    numbers = []
    for letter in string:
        numbers.append(int(letter))

    return numbers

def getFirstLine(fileName):
    with open(fileName) as file_object:
        lines = file_object.readlines() 

    for line in lines:
        return line
    return []