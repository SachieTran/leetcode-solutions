class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=5:
            return n
        table = [i for i in range(n+1)]
        
        for i in range(6,n+1):
            j = i/2
            while(j>1):
            	print i,j,dp[j]
                if (i % j == 0):
                    table[i] = table[j] + (i/j)
                    break
                j-=1
                	
        return dp[n]