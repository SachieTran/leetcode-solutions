a = [1,2,3]

def get_next(start,end):
	if start==end:
		return
	else:
		get_next(start+1,end)
		if a[start]<a[end]:
			temp = a[start]
			a[start] = a[end]
			a[end] = temp
			print a
			return
		else:
			get_next(start,end-1)

get_next(0, len(a)-1)