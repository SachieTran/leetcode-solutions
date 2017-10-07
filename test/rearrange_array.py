arr = [3,2,0,1]

print arr
n = len(arr)
for i in range(n):
	arr[i] += (arr[arr[i]]%n)*n
for i in range(n):
	arr[i] /= n

print arr
