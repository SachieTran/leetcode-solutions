class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = [0]*len(prices)
        for i in range(1,len(profit)):
        	profit[i] = prices[i] - prices[i-1]

        currentMax = 0
        maxGlobal = 0
        print profit
        for i in profit:
        	if i+currentMax<=0:
        		if currentMax>maxGlobal:
        			maxGlobal = currentMax
        		currentMax = 0
        	else:
        		currentMax+=i
        		if currentMax>maxGlobal:
        			maxGlobal = currentMax

        return maxGlobal

s = Solution()
input = [3,2,6,5,0,3]
print s.maxProfit(input)