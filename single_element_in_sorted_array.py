class Solution(object):
	def singleNonDuplicate(self, nums):
		if len(nums)==1:
			return nums[0]
		else:
			mid = len(nums)/2
			if mid%2!=0:
				if nums[mid-1]==nums[mid]:
					return self.singleNonDuplicate(nums[mid+1:])
				if nums[mid+1]==nums[mid]:
					return self.singleNonDuplicate(nums[0:mid])
				return nums[mid]
			else:
				if nums[mid-1]==nums[mid]:
					return self.singleNonDuplicate(nums[0:mid])
				if nums[mid+1]==nums[mid]:
					return self.singleNonDuplicate(nums[mid+2:])
					
				return nums[mid]

input = [3,3,7,7,10,11,11]
s = Solution()
print s.singleDuplicate(input)


