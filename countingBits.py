class Solution(object):
	def countBits(self, num):
		result = [0 for i in range(num+1)]
		prevRangeVal = 0
		power = 1

		for i in xrange(1,num+1):
			if i==power:
				power*=2
				prevRangeVal=0
			result[i] = result[prevRangeVal]+1
			prevRangeVal+=1

		return result

s = Solution()
print s.countBits(5)