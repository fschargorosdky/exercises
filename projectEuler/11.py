import operator

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

def prodCol(grid, row, col):
	return grid[row][col] * grid[row - 1][col] * grid[row - 2][col] * grid[row - 3][col]

def prodRow(grid, row, col):
	return prod(grid[row][col-4:col])

def prodLeftDiagonal(grid, row, col):
	return grid[row][col] * grid[row - 1][col - 1] * grid[row - 2][col - 2] * grid[row - 3][col - 3]

def prodRightDiagonal(grid, row, col):
	return grid[row][col] * grid[row - 1][col + 1] * grid[row - 2][col + 2] * grid[row - 3][col + 3]

gridFile = open('11-grid', 'r')
grid = []

for line in gridFile:
	grid.append(map(lambda x: int(x), line.split(' ')))

rowRange = range(0, len(grid))
colRange = rowRange
max4 = 0
for row in rowRange[3:]:
	for col in colRange:
		if prodCol(grid, row, col) > max4:
			max4 = prodCol(grid, row, col)

for row in rowRange:
	for col in colRange[3:]:
		if prodRow(grid, row, col) > max4:
			max4 = prodRow(grid, row, col)

for row in rowRange[3:]:
	for col in colRange[3:]:
		if prodLeftDiagonal(grid, row, col) > max4:
			max4 = prodLeftDiagonal(grid, row, col)

for row in rowRange[3:]:
	for col in colRange[:-3]:
		if prodRightDiagonal(grid, row, col) > max4:
			max4 = prodRightDiagonal(grid, row, col)

print max4
# print gridFile.read()
