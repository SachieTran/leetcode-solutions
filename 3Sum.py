s = [0, -1, 2, -3, 1] 
hash = {}
for i in range(len(s)-2):
	for j in range(i+1,len(s)-1):
		if -(s[i]+s[j]) in hash:
			print s[i], s[j], -(s[i]+s[j])
		else:
			hash[-(s[i]+s[j])]


