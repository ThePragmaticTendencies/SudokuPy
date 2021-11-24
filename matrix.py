#%%
class Matrix:
    def __init__(self, cellDim, noOfCellsInRow, numbers):
        self.numbers = numbers

        self.cellDim = cellDim
        self.noOfCellsInRow = noOfCellsInRow

        
        self._matrix = None
        self._matrixDimension2D = None
    
    def get(self):
        if (self._matrix):
            return self._matrix

        numbersLen = len(self.numbers)
        numbersToTransform = self.numbers[:]

        matrixDimension = self.dimension2D()

        rows = []
        i = 0
        if(matrixDimension**2 > numbersLen):
            raise ValueError("Matrix dimension is not matching input numbers")

        while(numbersToTransform and i < 20):
            row = numbersToTransform[:matrixDimension]
            del numbersToTransform[:matrixDimension]
            rows.append(row)
            i+=1
        
        self._matrix = rows
        return self._matrix

    def numbersInCells(self):
        cells = [[] for _ in range(self.noOfCellsInRow**2)]

        def appendNumbers(row, column, number):
            if (number != 0): cells[self._cellNumber(row, column)].append(number)

        self._traverseMatrix(appendNumbers)
        
        return cells

    def numbersInDirection(self, direction):
        return self._itemsInDirection(direction, lambda number: number != 0, lambda row, column, number: number)

    def potentialsInDirection(self, direction):
        return self._itemsInDirection(direction, lambda number: number == 0, lambda row, column, number: row if direction == 'row' else column)
    
    def cellsByRows(self):
        rows = []

        for rowNumber in range(self.dimension2D()):
            startingCell = self._cellRow(rowNumber)*self.noOfCellsInRow
            finishCell = startingCell+self.noOfCellsInRow
            cellsInRow = list(range(startingCell,finishCell))
            rows.append(cellsInRow)

        return rows
    
    def cellsByColumns(self):
        columns = []
        meaningfulRows = list(range(0, self.dimension2D(), self.cellDim))

        for column in range(self.dimension2D()):
            columnCells = []
            for row in meaningfulRows:
                columnCells.append(self._cellNumber(row, column))
            columns.append(columnCells)

        return columns

    def dimension2D(self):
        if self._matrixDimension2D == None:
            self._matrixDimension2D = self.cellDim*self.noOfCellsInRow

        return self._matrixDimension2D
    
    def solve(self):
        pass

    def _cellNumber(self, row, position):
        return (self._cellRow(row) * self.noOfCellsInRow) + position//self.cellDim
    
    def _cellRow(self, row):
        return row//self.cellDim
        
    def _traverseMatrix(self, action):
        for idx1, row in enumerate(self.get()):
            for idx2, number in enumerate(row):
                action(idx1, idx2, number)
    
    
    def _itemsInDirection(self, direction, selectorPredicate, propertySelector):
        itemsInDirection = [[] for _ in range(self.dimension2D())]

        def itemAppender(row, column, number):
            if selectorPredicate(number):
                itemsInDirection[row if direction == 'row' else column].append(propertySelector(row, column, number))

        self._traverseMatrix(itemAppender)
        
        return itemsInDirection