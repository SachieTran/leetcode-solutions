def updateChecker(checker, n):
	return checker | int(bin(1),2)<<n

checker = 0
s = 'abhzy'
flag = True
for ch in s:
	n = ord(ch)-ord('a')
	if not int(bin(1),2)<<n & checker:
		checker = updateChecker(checker, n)
	else:
		print 'found duplicate charecter ==>',ch
		flag = False
		break

if flag:
	print 'String contains all unique characters'



