class Solution(object):
	def findDuplicates(self, nums):
		MAX_VAL = len(nums)+1
		result = []
		for i,val in enumerate(nums):
			while val>MAX_VAL:
				val-=MAX_VAL
			if nums[val-1]>MAX_VAL:
				result.append(val)
			nums[val-1] += MAX_VAL
		
		return result

input = [4,3,2,7,8,2,3,1]
s = Solution()
print s.findDuplicates(input)