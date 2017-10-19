class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 10
        if n == 2:
            return 91
        
        l = [0]*n
        l[0] = 10
        l[1] = 81
        for i in range(2,n):
            cnt = 8
            total = 1
            for j in range(i-1):
                total = total*cnt
                cnt-=1
            total *=81
            l[i] = total
        return sum(l)

s = Solution()
print s.countNumbersWithUniqueDigits(3)