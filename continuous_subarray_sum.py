class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainders = {}
        running_sum = 0
        if len(nums)<2:
            return False
        if k == 0 :
            for i in range(len(nums)-1):
                if nums[i]==0 and nums[i+1]==0:
                    return True
            return False
        for i, val in enumerate(nums):
            running_sum+=val
            if running_sum%k==0 and i>0:
                return True
            if k!=0:
                running_sum%=k
            prev = -1
            if running_sum in remainders:
                prev = remainders[running_sum]
            if prev==-1:
                remainders[running_sum] = i
            elif (i-prev>0):
                return True
        return False


s = [1,1]
o = Solution()
print o.checkSubarraySum(s, 2)
