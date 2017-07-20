s = [1,2,3,4,4,5,6,3,2,1,3]

def find_peak(a, start, end):
	middle = (start+end)/2
	print middle, a[middle-1]
	if a[middle-1]<=a[middle] and a[middle+1]<=a[middle]:
		return a[middle]
	if start==end:
		return a[start]
	else:
		if a[middle]>a[middle-1] and a[middle]<=a[middle+1]:
			find_peak(a, middle+1, end)
		else:
			find_peak(a, start, middle-1)

print find_peak(s,0,len(s)-1)
