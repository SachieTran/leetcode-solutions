class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """

    	return sorted(pairs, key = lambda x: (x[0], x[1]))


s = [[1,2], [2,4], [2,3], [3,4]]
p = Solution()
print p.findLongestChain(s)