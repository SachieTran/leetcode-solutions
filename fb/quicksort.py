a = [54,26,93,17,77,31,44,55,20]
def quickSort(left, right):
	if left < right:
		pivot = partition(left, right)
		quickSort(left, pivot-1)
		quickSort(pivot+1, right)

def partition(left, right):
	
	pivotVal = a[left]
	leftPtr = left+1
	rightPtr = right
	while True:
		while a[leftPtr]<pivotVal and leftPtr<=rightPtr:
			leftPtr+=1
		while a[rightPtr]>=pivotVal and leftPtr<=rightPtr:
			rightPtr-=1
		if leftPtr>=rightPtr:
			break
		tmp = a[leftPtr]
		a[leftPtr] = a[rightPtr]
		a[rightPtr] = tmp

	tmp = a[rightPtr]
	a[rightPtr] = a[left]
	a[left] = tmp
	
	return rightPtr


quickSort(0, len(a)-1)
print a



