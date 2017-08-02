s = [-1, 0, 1, 2, -1, -4]
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.hash = {}
        for i in xrange(len(nums)-1):
        	for j in range(i+1, len(nums)):
        		if -(nums[i]+nums[j]) in self.hash.keys():
        			if sorted([nums[i], nums[j], -(nums[i]+nums[j])]) not in result:
        				result.append(sorted([nums[i], nums[j], -(nums[i]+nums[j])]))
        		else:
        			self.hash[nums[i]] = 0
        return result

p = Solution()
print p.threeSum(s)



