import sys

counter = 0

sudoku = []

sudoku_string_0 = '0 0 0 0 0 0 5 0 0 0 0 0 0 0 1 0 0 0 0 0 9 0 6 0 0 8 0 0 0 0 5 0 0 0 0 0 0 0 8 0 0 0 0 9 6 0 7 0 3 0 0 0 0 0 0 0 0 0 9 0 0 0 0 0 2 0 0 0 0 3 0 0 0 5 0 0 0 0 7 0 1'
sudoku_string_1 = '0 9 0 5 0 0 8 2 0 4 0 5 0 0 0 0 0 0 0 8 0 0 0 7 0 0 4 9 0 0 0 3 0 7 8 1 0 0 0 0 0 0 0 0 0 5 4 3 0 1 0 0 0 9 7 0 0 8 0 0 0 3 0 0 0 0 0 0 0 1 0 2 0 1 4 0 0 6 0 5 0'
sudoku_string_2 = '1 9 7 5 6 4 8 2 3 4 3 5 1 0 0 0 0 0 0 8 0 0 0 7 0 0 4 9 0 0 0 3 0 7 8 1 0 0 0 0 0 0 0 0 0 5 4 3 0 1 0 0 0 9 7 0 0 8 0 0 0 3 0 0 0 0 0 0 0 1 0 2 0 1 4 0 0 6 0 5 0'
sudoku_string_3 = '6 2 7 0 0 0 4 0 0 0 0 0 0 0 2 0 0 8 0 3 0 0 6 0 0 0 0 0 0 0 0 0 0 2 7 0 1 0 0 2 0 8 0 9 0 0 0 0 0 0 9 1 0 0 2 1 8 5 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 5 4 7 0 8 3 0'
sudoku_string_4 = '0 0 0 0 0 0 0 0 0 0 0 0 0 0 3 0 8 5 0 0 1 0 2 0 0 0 0 0 0 0 5 0 7 0 0 0 0 0 4 0 0 0 1 0 0 0 9 0 0 0 0 0 0 0 5 0 0 0 0 0 0 7 3 0 0 2 0 1 0 0 0 0 0 0 0 0 4 0 0 0 9'


sys.setrecursionlimit(10000)

def convert_string(sudoku, start_string):    
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(int(start_string.split(' ')[j + i * 9]))

        sudoku.append(temp)


def isValid(sudoku, num, row, col):
    for i in range(9):
        if i == row:
            continue

        if sudoku[i][col] == num:
            return False

    for j in range(9):
        if j == col:
            continue

        if sudoku[row][j] == num:
            return False

    for oy in range(3):
        for ox in range(3):
            if int(row / 3) * 3 + oy == row and int(col / 3) * 3 + ox == col:
                continue
            
            if sudoku[int(row / 3) * 3 + oy][int(col / 3) * 3 + ox] == num:
                return False

    return True


def isFull(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return False

    return True


def fullestRow(sudoku):
    maxRow = -1
    maxRowCount = 0
    currentRowCount = 0

    for i in range(9):
        currentRowCount = 0
        for j in range(9):
            if sudoku[i][j] != 0:
                currentRowCount += 1

        if currentRowCount < 9 and currentRowCount > maxRowCount:
            maxRow = i
            maxRowCount = currentRowCount

    return (maxRow, maxRowCount)


def fullestCol(sudoku):
    maxCol = -1
    maxColCount = 0
    currentColCount = 0

    for j in range(9):
        currentColCount = 0
        for i in range(9):
            if sudoku[i][j] != 0:
                currentColCount += 1

        if currentColCount < 9 and currentColCount > maxColCount:
            maxCol = j
            maxColCount = currentColCount

    return (maxCol, maxColCount)


def fullestCell(sudoku):
    return (0, 0), -1
    maxCell = (0, 0)
    maxCellCount = 0
    currentCellCount = 0

    for y in range(3):
        for x in range(3):
            currentCellCount = 0
            for oy in range(3):
                for ox in range(3):
                    if sudoku[y * 3 + oy][x * 3 + ox] != 0:
                        currentCellCount += 1

            if currentCellCount < 9 and currentCellCount > maxCellCount:
                maxCell = (y, x)
                maxCellCount = currentCellCount

    return (maxCell, maxCellCount)


def nextCell(sudoku, row, col):
    nextCol = (col + 1) % 9
    nextRow = row if nextCol != 0 else row + 1

    nCol, nColCount = fullestCol(sudoku)
    nRow, nRowCount = fullestRow(sudoku)
    nCell, nCellCount = fullestCell(sudoku)

    nextRow = 0
    nextCol = 0

##    printSudoku(sudoku)
##    print(nRow, nRowCount, nCol, nColCount)

    if nRowCount >= nColCount and nRowCount >= nCellCount:
        nextCol = 0
        nextRow = nRow

        if nextRow == 9:
            return None

        while sudoku[nextRow][nextCol] != 0:
            nextCol = (nextCol + 1) % 9

            if nextCol == 0:
                nextRow += 1

            if nextRow == 9:
                return None
    elif nColCount >= nRowCount and nColCount >= nCellCount:
        nextRow = 0
        nextCol = nCol

        if nextCol == 9:
            return None

        while sudoku[nextRow][nextCol] != 0:
            nextRow += 1

            if nextRow == 9:
                return None
    else:
        for oy in range(3):
            for ox in range(3):
                if sudoku[nCell[0]*3 + oy][nCell[1]*3 + ox] == 0:
                    return (nCell[0]*3 + oy, nCell[1]*3 + ox)

    return (nextRow, nextCol)


def fillValidNumber(sudoku, row, col):
    global counter

    counter += 1

##    if counter % 1 == 0:
##        printSudoku(sudoku)
##        print()

    if sudoku[row][col] == 0:
        for n in range(1, 10):
            if not isValid(sudoku, n, row, col):
                continue
            
            sudoku[row][col] = n

            if isFull(sudoku):
                return True

            if fillValidNumber(sudoku, *nextCell(sudoku, row, col)):
                return True

            sudoku[row][col] = 0

        return False

    else:
        return fillValidNumber(sudoku, *nextCell(sudoku, row, col))


def printSudoku(sudoku):
    for i in range(9):
        string = ''
        for j in range(9):
            string += str(sudoku[i][j]) + ' '

        print(string)
            


convert_string(sudoku, sudoku_string_4)

printSudoku(sudoku)

print(fillValidNumber(sudoku, 0, 0))

print(counter)

printSudoku(sudoku)




            

    

    
