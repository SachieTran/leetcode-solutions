
def dispMatrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix)):
			print matrix[i][j],
		print ''
	print ''

def rotateMatrix(matrix):
	n = len(matrix)
	for x in range(len(matrix)/2):
		for y in range(x, n-x-1): 
			temp = matrix[x][y]
			matrix[x][y] = matrix[y][n-1-x]
			matrix[y][n-1-x] = matrix[n-1-x][n-1-y]
			matrix[n-1-x][n-1-y] = matrix[n-1-y][x]
			matrix[n-1-y][x] = temp

	return matrix	


matrix = [[i+j for i in range(6)] for j in range(6)]
dispMatrix(matrix)
dispMatrix(rotateMatrix(matrix))

