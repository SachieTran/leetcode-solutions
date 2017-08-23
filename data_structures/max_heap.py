## Max - Heap
arr = [1,12,9,5,6,10]

def heapify(i, n):
	#print arr, i
	largest = i
	l = i*2+1
	r = i*2+2

	if l<n and arr[l]>arr[largest]:
		largest = l

	if r<n and arr[r]>arr[largest]:
		largest = r

	if largest!=i:
		temp = arr[i]
		arr[i] = arr[largest]
		arr[largest] = temp
		heapify(largest, n)

def buidHeap():
	for i in range(len(arr)/2-1,-1,-1):
		heapify(i, len(arr))


print arr
buidHeap()
print arr


