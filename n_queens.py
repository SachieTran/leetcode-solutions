queens = 4

rows = {}
cols = {}
diagonals = {}

coordinates = {}
def isSafe(row,col):
	if row in rows or col in cols or row+col in diagonals or row-col in diagonals:
		return False
	return True

def nQueens(n):
	if n==queens:
		return True
	for i in range(queens):
		print "placing queen at row",n
		print rows,cols,diagonals
		if isSafe(n,i):
			print "safe position ",n,i
			coordinates[(n,i)] = 0
			rows[n] = 1
			cols[i] = 1
			diagonals[n+i] = 1
			diagonals[n-i] = 1
			if not nQueens(n+1):
				print "no safe position found in row", n+1
				if n in rows:
					del rows[n]
				if i in cols:
					del cols[i]
				if n+i in diagonals:
					del diagonals[n+i]
				if n-i in diagonals:
					del diagonals[n-i]
				if (n,i) in coordinates:
					del coordinates[(n,i)]
	return False


print nQueens(0)
print coordinates


