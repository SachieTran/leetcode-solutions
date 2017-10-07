def sort10(s):
	ptr1 = 0
	ptr2 = len(s)-1

	while ptr1<len(s) and ptr2>0:
		while s[ptr1]==0:
			ptr1+=1
			if ptr1==len(s):
				return s

		while s[ptr2]==1:
			ptr2-=1
			if ptr2==-1:
				return s

		if ptr2<ptr1:
			return s
		else:
			tmp = s[ptr1]
			s[ptr1] = s[ptr2]
			s[ptr2] = tmp
			ptr1+=1
			ptr2-=1

s = [1,0,0,0,1,1,0,0,1,0]
sort10(s)
print s
