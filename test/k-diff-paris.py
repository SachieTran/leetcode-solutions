class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        table = {}   # store keys in format (a-k):index 
        pairsSet = {}
        count = 0
        for i,n in enumerate(nums):
            #print table, pairsSet
            if n in table:
                for candidate in table[n]:
                    if not frozenset((n, nums[candidate])) in pairsSet:
                        pairsSet[frozenset((n, nums[candidate]))]=1
                
            if n-k in table:
                table[n-k].append(i)
            else:
                table[n-k] = [i]
            if n+k in table:
                table[n+k].append(i)
            else:
                table[n+k] = [i]

        return len(pairsSet)

s = Solution()
input = [1, 3, 1, 5, 4]
print s.findPairs(input, 0)
