## Max - Heap
arr = [2,1,3,5,1,2,3,6,8,5,3]

def heapify(i, n):
	largest = i
	l = i*2+1
	r = i*2+2

	if l<n and arr[l]>arr[i]:
		largest = l

	if r<n and arr[r]>arr[i]:
		largest = r

	if largest!=i:
		temp = arr[i]
		arr[i] = arr[largest]
		arr[largest] = temp
		heapify(largest, n)


print arr
heapify(0, len(arr))
print arr


