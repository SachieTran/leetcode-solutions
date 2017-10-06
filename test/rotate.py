def Rotate(a):
	N = len(a)
	for i in range(len(a)/2):
		for j in range(i, N-i-1):
			tmp = a[i][j]
			a[i][j] = a[N-j-1][i]
			a[N-j-1][i] = a[N-i-1][N-j-1]
			a[N-i-1][N-j-1] = a[j][N-i-1]
			a[j][N-i-1] = tmp
			display(a)


def display(a):
	for i in range(len(a)):
		for j in range(len(a[0])):
			print a[i][j],
		print ""
	print ""

a = [[1, 2, 3, 4,],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]

display(a)
print ""
Rotate(a)
display(a)