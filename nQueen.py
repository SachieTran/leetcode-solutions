from collections import defaultdict
rows = {}
cols = {}
left_diagonals = {}
right_diagonals = {}
indexes = {}

def displayBoard(indexes,n):
	for row in range(n):
		for col in range(n):
			if (row,col) in indexes:
				print 'Q',
			else:
				print '*',
		print ''
def isValidPosition(i,j):
	if i in rows or j in cols or i+j in right_diagonals or i-j in left_diagonals:
		return False
	return True

def nQueen(row,n):
	if row>n-1:
		#print "Result found"
		#print indexes
		return True
	else:
		for col in range(n):
			#print "looking at ",row,col
			#print rows,cols,left_diagonals,right_diagonals
			if not (col in cols or row in rows or col+row in right_diagonals or row-col in left_diagonals):
				cols[col]=1
				rows[row]=1
				right_diagonals[row+col]=1
				left_diagonals[row-col]=1
				indexes[(row,col)] = 0

				if not nQueen(row+1,n):
					if col in cols:
						del cols[col]
					if row in rows:
						del rows[row]
					if row+col in right_diagonals:
						del right_diagonals[row+col]
					if row-col in left_diagonals:
						del left_diagonals[row-col]
					del indexes[(row,col)]
				else:
					return True
		return False

n = 8
nQueen(0,n)
displayBoard(indexes,n)



