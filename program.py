
# %%
from matrix import Matrix
import utils

# %%
firstLine = utils.getFirstLine('puzzle_01.pzl')
numbers =  utils.getNumberList(firstLine)
utils.printNumbersAsSudokuBoard(firstLine)

# %%
matrix = Matrix(3, 3, numbers)
matrix.get()
matrix.numbersInCells()
# %%
matrix2 = Matrix(3, 2, [0, 2, 0,  3, 0, 4,  8, 9, 1,  0, 0, 0,  0, 0, 0,  0, 0, 7,  0, 0, 0,  0, 0, 0,  0, 0, 0,  0, 0, 0,  1, 0, 0,  6, 0, 8])
matrix2.get()
# %%


def solveSudoku(matrix:Matrix):
    """
    Checks if with each direction iteration pair potentials are reduced
    If not stops
    Else goes till none left and isSolved
    """
    isSolved = False
    isStuck = False
    startDirection = 'row'
    direction = startDirection
    iterations = []
    safetySwitch = 1000

    while not isSolved and not isStuck and safetySwitch > 0:
        safetySwitch -= 1
        potentials = iterateInDirection(direction, matrix)
    
        for potentialsForDirection in potentials:
            if len(potentialsForDirection) != 0:
                iterations.append({'direction': direction, 'potentials': potentials})
                isSolved = False

                if direction != startDirection:
                    isStuck = iterations[-2] == iterations[-1]
                    direction = 'column' if direction == 'row' else 'row'
                break
    
    matrix.get()
    


def iterateInDirection(direction: str, matrix: Matrix):
    """
    Get all potentials in given direction
    Iterate all columns/rows
    for each column/row run Solve with given potentials list and missing numbers
    """
    cellsCrosedByDirection = matrix.cellsByColumns() if direction == 'row' else matrix.cellsByRows()
    numbersInCells = matrix.numbersInCells()
    numbersInDirection = matrix.numbersInDirection(direction)
    potentialsInDirection = matrix.potentialsInDirection(direction)
    for idx in matrix.dimension2D():
        numbersByCellInDirection = matrix.
        solvedPotentials = solvePotentials(direction, potentialsInDirection[idx], numbersInDirection[idx], cellsInDirection[idx])

        for solvedPotential in solvedPotentials:
            matrix.solve(direction, idx, solvedPotential)

def solvePotentials(direction, potentialsInDirection, numbersInDirection, cellsInDirection):
    """
    Take each number
    Take copy of potentials
    Try to filteroutpotentials for given number
    if only one potential in scope is left, add potential position and solved value to solved[]
    return solved[]
    """
    solvedPotentials = []

    for number in numbersInDirection:
        filteredPotentials = potentialsInDirection[:]
        filterOutByCells(filteredPotentials, number)
        filterOutByDirection(filteredPotentials, number, direction)
        if len(filteredPotentials) == 1:
            solvedPotentials.append((filteredPotentials[0], number))
    
    return solvedPotentials


def filterOutByCells(potentialsInDirection, number):
    """
    have number
    get list of cells crossed by direction
    get numbers by cell for given cells
    check if any cell contains number
    if so, remove potentials contained in that cell..
    """

def filterOutByDirection(potentialsInDirection, number, direction):
    """
    have number
    get list of cells crossed by direction
    get numbers by cell for given cells
    check if any cell contains number
    if so, remove potentials contained in that cell..
    """