def _lis(arr, n):
	if n == 0:
		return 1
	for i in range(n-1, -1, -1):
		res = _lis(arr,i)
		if res >= table[n] and arr[n] > arr[i]:
			table[n] = res+1
	return table[n]


arr = [1,1,1,1,1,1,1,1,1,1,1,1]
table = [1 for i in range(len(arr))]
_lis(arr, len(arr)-1)
print max(table)