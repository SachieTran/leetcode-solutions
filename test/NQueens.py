cols = {}
rows = {}
left_diagonals = {}
right_diagonals = {}

N = 4
board = [[0 for j in range(N)] for i in range(N)]

def display():
	for i in range(len(board)):
		for j in range(len(board[0])):
			print board[i][j],
		print ""
	print ""

def NQueens(target_row, N):
	
	if target_row >= N:
		display()
		return True
	else:
		for j in xrange(N):
			print "Looking for row", target_row
			print rows,cols,right_diagonals,left_diagonals
			display()
			if not (target_row in rows or j in cols or (target_row+j) in left_diagonals or (target_row-j) in right_diagonals):
				rows[target_row] = 1
				cols[j] = 1
				left_diagonals[target_row+j] = 1
				right_diagonals[target_row-j] = 1
				board[target_row][j] = "Q"
				
				if not NQueens(target_row+1, N):
					del rows[target_row]
					del cols[j]
					del left_diagonals[target_row+j]					
					del right_diagonals[target_row-j]
					board[target_row][j] = 0
				else:
					return True
			else:
				print "Cannot place queen at row",target_row, " column",j
		return False

NQueens(0, N)






