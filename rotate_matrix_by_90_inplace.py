
def dispMatrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix)):
			print matrix[i][j],
		print ''
	print ''

def rotateMatrixAntiClockWise(matrix):
	n = len(matrix)
	for x in range(len(matrix)/2):
		for y in range(x, n-x-1): 
			temp = matrix[x][y]
			matrix[x][y] = matrix[y][n-1-x]
			matrix[y][n-1-x] = matrix[n-1-x][n-1-y]
			matrix[n-1-x][n-1-y] = matrix[n-1-y][x]
			matrix[n-1-y][x] = temp

	return matrix	

def rotateMatrixClockWise(matrix):
	n = len(matrix)
	for x in range(n/2):
		for y in range(x,n-x-1):
			temp = matrix[x][y]
			matrix[x][y] = matrix[n-1-y][x]
			matrix[n-1-y][x] = matrix[n-1-x][n-1-y]
			matrix[n-1-x][n-1-y] = matrix[y][n-1-x]
			matrix[y][n-1-x] = temp
	return matrix


#matrix = [[i+j for i in range(6)] for j in range(6)]
matrix = [[1,2],[3,4]]
dispMatrix(matrix)
dispMatrix(rotateMatrixClockWise(matrix))

