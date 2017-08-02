class Solution(object):
    def printA(self, N):
        print N
        max = N
        if N<=6:
            return N
        else:
            for i in range(N-3,2,-1):
                if self.d[i]!=-1:
                    curr = self.d[i]*(N-i-1)
                else:
                    curr = self.printA(i)*(N-i-1)
                    self.d[N] = curr
                if curr>max:
                    max = curr
        return max

    def maxA(self, N):
        self.d = {i:-1 for i in xrange(N+1)}
        return self.printA(N)

s = Solution()
print s.maxA(19)