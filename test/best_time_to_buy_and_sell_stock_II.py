class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = [0]*len(prices)
        for i in range(1,len(profit)):
        	profit[i] = prices[i] - prices[i-1]
        print profit

        maxSumArray = [0]*len(prices)
        currSum = 0
        for i in range(1, len(profit)):
            if profit[i]+currSum<currSum:
                maxSumArray[i] = 0
                currSum=0
            else:
                maxSumArray[i] = profit[i]+currSum
                currSum+=profit[i]
        print maxSumArray


        maxProfit = 0
        i = 0
        while i<len(maxSumArray):
            while i<len(maxSumArray):
                if maxSumArray[i]==0:
                    i+=1
                else:
                    break
            buy = prices[i-1]
            while i<len(maxSumArray):
                if maxSumArray[i]!=0:
                    i+=1
                else:
                    break
            maxProfit+=(prices[i-1]-buy)
            
        return maxProfit

s = Solution()
input = [1,2,3]
print s.maxProfit(input)