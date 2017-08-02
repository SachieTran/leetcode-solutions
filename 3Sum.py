s = [1,2,-2,-1,0]
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:
        	return []
        result = []
        self.hash = {}
        for i in xrange(len(nums)-1):
        	for j in range(i+1, len(nums)):
        		if -(nums[i]+nums[j]) in self.hash.keys():
        			if sorted([nums[i], nums[j], -(nums[i]+nums[j])]) not in result:
        				result.append(sorted([nums[i], nums[j], -(nums[i]+nums[j])]))
        	
        	self.hash[nums[i]] = 0

        if len(result)==0:
        	return []
        return result

p = Solution()
print p.threeSum(s)



