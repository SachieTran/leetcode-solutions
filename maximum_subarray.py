a = [0, 13, -3,-25, 20 ,-3 ,-16 ,-23, 18, 20 ,-7, 12 ,-5 ,-22, 15 ,-4, 7]
print a

global_max_sum = 0
curr_sum = 0

left = -1
for i,val in enumerate(a):
	if val+curr_sum>0:
		curr_sum+=val
		if curr_sum>global_max_sum:
			global_max_sum=curr_sum
			right = i
	else:
		curr_sum = 0
		left = i+1

print global_max_sum, a[left:right+1]