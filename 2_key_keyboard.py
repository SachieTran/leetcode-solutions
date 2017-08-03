class Solution(object):
    def minSteps(self, n):
        dp = [-1 for i in range(n+1)]

        for i in range(2,n+1):
            dp[i] = i
            for j in range(i-1,1, -1):
                if (i % j == 0):
                    dp[i] = dp[j] + (i/j)
                    break
               
        return dp[n]
    

p = Solution()
print p.minSteps(5)