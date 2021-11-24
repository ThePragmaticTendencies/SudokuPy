One more time:

Given: list of numbers
When: **Matrix(cellLen, noOfCellsInRow, numbers)**
Then: I have: List of rows as matrix

#Get list of cells
Given: matrix
When: I **martix.numbersInCells()**
Then: I get list of cells left-top -> right-bottom, where cell is a list of exisiting numbers

#Get cells for columns
Given: list of cells []
When: I **martix.cellsByColumns(cells)**
Then: I get list of cells indexed by column numbers [columnNumber][cells]

#Get rows of cell
Given: list of cells []
When: I **martix.cellsByRows(cells)**
Then: I get list of cells index by row numbers [columnNumber][cells]

#GetPotentialFields
Given: matrix(list of rows)
When: **matrix.potentialFields(direction(0, None))**
Then: I scan columns/rows from left to right /Top-Down till first potentialFields is found and continue to list all potentialFields for current column/row.
Return list of potentialFields positions for given direction: direction (0, None), potentialFieldPositions = [0, 1, 2, 3, 5, 6], cahce in matrixPotentialFields{(direction)[fields]}

#Get missing numbers for given direction
Given: (0,None) and matrix
When: I ask for **matrix.missingNumbers(direction)**
Then: I get range 1 - 9 except all non zero values for given direction. This is cached in dictionary (col || None, row || None) = []

#StartSolveIteration
>Start with any direction and get first potentialFields that will be cached
>Then for gien direction run through those fields and then next direction, and next 
>When 1 direction is done (columns or row) change to other direction (column or row) and iterate same way
>when both directions are done go back to first direction and start from beginning running to direction change
>run till there are no potential fields left or num,ber of potential fields has not changed after 2 full cycles

#StartSolveIteration
>control potentialFields and iterations after full cycle get potential feilds from matrix and same/compare to previous
>>run iterate directions (column/row) => return list of potentialFields

 Given: [(0, None) || (None, 0)], matrix
 When: **SolveSudoku()** is started
 Then: changedDirection = False, direction, iteration = []
 Then: **RunIterateDirections(direction, matrix)**
 Then: if **matrix.PotentialFields** is not empty, **-RunIterateSolveColumns(direction, matrix)** and changedDirection = True
 Then: if **matrix.PotentialFields** is not empty, save potyential fields in **iterations.append(matrix.state, potentialFields)**, if iterations[] is greater than 1 compare and if no of potential fields did not change exit or otherwise repeat cycle, changeDirections = 0, etc.
 Then: if potentialFields is empty show solution, number odf iterations

#RunIterateDirections
Given: direction, matrix
When: I start function
Then: I get list of missing numbers
Then: For each missing number I run Solve(currentNumber, direction, matrix) 

#Solve
Given: copy of matrix.potentialFields //[0, 1, 2, 3, 5, 6]]

When: potential fields != 1
Then: Run **matrix.filterOutByCells(2, (0,None), [0, 1, 2, 3, 5, 6])**
Then: From list of cells [columnIndex][cellNumbers] by column I take crossing cells
Then: For given cells [cellNumber] in [cellListI] check if any contains currentNumber
Then: if any contains, I take list of cell.rows() and concat with any other
Then: I remove from potentialFields matching results


Given: previous copy of matrix.potentialFields //[0, 1, 2, 3, 5, 6]]
When: potential fields != 1
Then: matrix.filterOutByRows(2, (0,None), [0, 1, 2, 3, 5, 6])
Then: For each row from potentialFields positions I check if any contains currentNumber
Then: if any contains, I remove this position from potentialFields

Given: previous copy of matrix.potentialFields //[0, 1, 2, 3, 5, 6]]
Then: If potential fields == 1
Then: Update matrix at (direction-potentialField)
Then: Remove currentNumber from missingNumber for given row with matrix.removeFromMissingNumbers(direction-potentialField, currentNumber)

---------------------
OLD

How to solve Sudoku Puzzle?
0 - a. I have a matrix of 9x9 filled with numbers 1-9 and 0.
0 - b. zero is a placeholder for numbers that should meet conditions below:
1. numbers in each vertical line need to be 1-9 without duplicates
2. numbers in each horizontal line need to be 1-9 without duplicates
3. number in each cell 3x3 that are not overlapping must be 1-9 without duplicates
 
Happy path:
I get numbers required to complete cell
I get numbers required to complete horizontal line
I get numbers required to complete vertical line

List of missing numbers in rows (m)
List of missing numbers in columns (n)
f missing numbers in cells (m,n)
list of points eq 0 with position
result matrix to update too and plot each iteration


Given list of numbers
When I run have dimension of cell and number of cell in row
Then I have: List of missing numbers for each row of matrix

Given list of numbers
When I have dimension of cell and number of cell in row
Then I have: List of missing numbers for each column of matrix

Given list of numbers
When I have dimension of cell and number of cell in row
Then I have: List of missing numbers for each cell in matrix and cells are aligned from left bottom to bottom right

Given matrix with sudoku
When I run get

