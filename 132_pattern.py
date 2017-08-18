class Solution(object):
	def find132pattern(self, nums):
	    a = nums
	    min_list = []
	    for i,val in enumerate(a):
			if len(min_list)==0:
				min_list.append(val)
			else:
				if val<min_list[i-1]:
					min_list.append(val)
				else:
					min_list.append(min_list[i-1])
	    print min_list
	    stack = []
	    flag=False
	    for i in range(len(a)-1,-1,-1):
		    if len(stack)==0:
				stack.append(a[i])
		    else:
				while len(stack)>0:
					#print stack
					if a[i]>stack[0]:
						if min_list[i]<stack[0]:
							return True
							flag = True
							break
						else:
							stack.pop(0)
					else:
						break
				stack = [a[i]] + stack	
	    return False

s = Solution()
print s.find132pattern([2,4,3,4])


