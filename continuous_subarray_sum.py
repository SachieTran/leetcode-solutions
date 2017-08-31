class Solution(object):
	def checkSubarraySum(self, nums, k):
	    """
	    :type nums: List[int]
	    :type k: int
	    :rtype: bool
	    """
	    current_sum = nums[0]
	    start = 0
	    for i in xrange(1, len(nums)):
	    	current_sum+=nums[i]
	    	while(current_sum>k and start<i-1):
	    		current_sum-=nums[start]
	    		start+=1

	    	if current_sum==k:
	    		print 'subarray found from ',start, 'to', i
	    		return

	    if current_sum==k:
	    	print 'subarray found from ',start, 'to', i
	    else:
	    	print 'No subarray with sum',k,'found'


s = Solution()
a = [15, 2, 4, 8, 9, 5, 10, 23]
sum = 4
s.checkSubarraySum(a,sum)
