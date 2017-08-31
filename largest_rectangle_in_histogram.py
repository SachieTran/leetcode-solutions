heights = [2,1,5,6,2,3]
print "########## ", heights
index_stack = [-1]
height_stack = [0]
current_max = -1

for i, val in enumerate(heights):
	print i, val, index_stack, height_stack
	if len(index_stack)==0:
		index_stack.append(i)
		height_stack.append(val)
	elif height_stack[-1] < val:
		index_stack.append(i)
		height_stack.append(val)
	elif height_stack[-1] > val:
		while(height_stack[-1]>=val):
			height = height_stack.pop(-1)
			index = index_stack.pop(-1)
			current_max = max(current_max, height*(i-index))
		index_stack.append(i)
		height_stack.append(val)


if len(height_stack)!=0:
	while len(height_stack)!=0:
		print i, val, index_stack, height_stack
		height = height_stack.pop(-1)
		index = index_stack.pop(-1)
		current_max = max(current_max, height*(i+1-index))


print current_max

		
