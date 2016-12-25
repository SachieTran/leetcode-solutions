def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # d = {}
        # for i in range(len(nums)):
        #     val = target - nums[i]
        #     if nums[i] in d:
        #         return [d[nums[i]], i]
        #     else:
        #         d[val] = i
        
        result = [-1,-1]
        d = {val:i for i,val in enumerate(nums)}
        for i in nums:
            search = target - i
            if search in d and d[i]!=d[search]:
                return [d[i],d[search]]

        return result

nums = [0,4,3,0]
target = 0
print twoSum(nums,target)


