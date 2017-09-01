a = [2,3,7,8]
s = 21

def checkSum(start, end, target):
	if target==0:
		return True
	if start > end:
		return False
	r1 = checkSum(start+1, end, target) 
	if r1:
		return True
	r2 = checkSum(start+1, end, target-a[start])
	if r2:
		return True


if checkSum(0,len(a)-1,s):
	print "subsequensce with sum", s,"exists"
else:
	print "subsequensce with sum", s," does not exists"