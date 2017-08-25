from collections import defaultdict
s1 = 'abhay'
s2 = 'baahb'

def checkAnagrams(s1,s2):
	if len(s1)!=len(s2):
		return False
	d = defaultdict(int)
	for i in range(len(s1)):
		d[s1[i]]+=1
		d[s2[i]]-=1
	return reduce(lambda x,y: x and y, map(lambda x: x==0, d.values()))

if checkAnagrams(s1,s2):
	print s1, 'and', s2, 'are anagrams'
else:
	print s1, 'and', s2, 'are not anagrams'