class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        max = N
        middle = N/2
        
        if N > 5:
            for i in range(2, middle+1):
                temp = i^(N-2-i)
                if temp>max:
                    max = temp
        
        return max