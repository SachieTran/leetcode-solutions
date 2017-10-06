def mergesort(a):
	if len(a)<=1:
		return a
	mid = len(a)/2
	left = mergesort(a[:mid])
	right = mergesort(a[mid:])

	return merge(left, right)

def merge(a,b):
	result = []
	i=0
	j=0

	while i<len(a) and j<len(b):
		if a[i]<b[j]:
			result.append(a[i])
			i+=1
		else:
			result.append(b[j])
			j+=1

	if i==len(a):
		while j<len(b):
			result.append(b[j])
			j+=1

	if j==len(a):
		while i<len(a):
			result.append(a[i])
			i+=1

	return result

sorted_array = mergesort([3,2,1,4,5,3,6,7,9])
print sorted_array

