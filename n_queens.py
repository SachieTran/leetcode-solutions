queens = 4

rows = {}
cols = {}
right_diagonals = {}
left_diagonals = {}
coordinates = {}

def isSafe(row,col):
	if row in rows or col in cols or row+col in left_diagonals or row-col in right_diagonals:
		return False
	return True

def nQueens(n):
	if n==queens:
		print "####### coordinates #######\n",coordinates
		return True
	for i in range(queens):
		print "placing queen at row",n
		print rows,cols,left_diagonals,right_diagonals
		if isSafe(n,i):
			print "safe position ",n,i
			coordinates[(n,i)] = 0
			rows[n] = 1
			cols[i] = 1
			left_diagonals[n+i] = 1
			right_diagonals[n-i] = 1
			if not nQueens(n+1):
				print "no safe position found in row", n+1
				if n in rows:
					del rows[n]
				if i in cols:
					del cols[i]
				if n+i in left_diagonals:
					del left_diagonals[n+i]
				if n-i in right_diagonals:
					del right_diagonals[n-i]
				if (n,i) in coordinates:
					del coordinates[(n,i)]
			else:
				return True
	return False


print nQueens(0)
print coordinates


