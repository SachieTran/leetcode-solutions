a = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]

rows = len(a)
cols = len(a[0])

count = 0
i=0
j=0
direction = 0 

while count < rows*cols:
	print a[i][j],
	count+=1
	a[i][j]=-1

	if direction == 0:
		if j+1==cols or a[i][j+1]==-1:
			direction = 1
		else:
			j+=1
	if direction == 1:
		if i+1==rows or a[i+1][j]==-1:
			direction = 2
		else:
			i+=1
	if direction == 2:
		if j-1==-1 or a[i][j-1]==-1:
			direction = 3
		else:
			j-=1
	if direction == 3:
		if i-1==-1 or a[i-1][j]==-1:
			direction = 0
			j+=1
		else:
			i-=1




