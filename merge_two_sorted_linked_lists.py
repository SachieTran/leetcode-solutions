s1 = [1,2,3,4,5,6]
s2 = [3,5,7,8,9,]

ptr1 = 0
ptr2 = 0

result = []

while ptr1<len(s1) and ptr2<len(s2):
	if s1[ptr1]<s2[ptr2]:
		result.append(s1[ptr1])
		ptr1+=1
	else:
		result.append(s2[ptr2])
		ptr2+=1

if ptr1<len(s1):
	while ptr1<len(s1):
		result.append(s1[ptr1])
		ptr1+=1

if ptr2<len(s2):
	while ptr2<len(s2):
		result.append(s2[ptr2])
		ptr2+=1

print result


