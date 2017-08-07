class Solution(object):

	def findLongestChain(self, pairs):
		self.sorted_pairs = sorted(pairs, key = lambda x : (x[0], x[1]))
		self.table = [1 for i in range(len(self.sorted_pairs))]
		self.longestPair(len(self.sorted_pairs)-1)
		return max(self.table)

	def longestPair(self,n):
		if n==0:
			return 1
		else:
			for i in range(n-1,-1,-1):
				res = self.longestPair(i)
				if res >= self.table[n] and self.sorted_pairs[i][1]< self.sorted_pairs[n][0]:
					self.table[n] = self.table[i] + 1
		return self.table[n]




s = [[1,2], [2,4], [2,3], [3,4]]
s = [[5, 24], [15, 25], [27, 40], [50, 60]]
p = Solution()
print p.findLongestChain(s)