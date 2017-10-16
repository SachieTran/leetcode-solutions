def perm(a, start, end):
	if start>=end:
		print a
	else:
		for i in range(start, end+1):
			tmp = a[start]
			a[start] = a[i]
			a[i] = tmp
			perm(a, start+1, end)
			tmp = a[start]
			a[start] = a[i]
			a[i] = tmp

input = [1,2,3,4 ]
perm(input, 0, len(input)-1)
