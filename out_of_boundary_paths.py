class Solution(object):
	cnt = 0
	def findPaths(self, m, n, N, i, j):
		self.memo = [[[-1 for k in xrange(N+1)] for col in xrange(n)] for row in xrange(m)]
		self.max = 1000000007
		paths = self.getPath(m, n, N, i, j)
		print Solution.cnt
		return paths

	def getPath(self, m, n, N, i, j):
		Solution.cnt+=1
		if i==m or i<0 or j==n or j<0:
			return 1
		if N<=0:
			return 0
		if self.memo[i][j][N]>=0:
			return self.memo[i][j][N]
		self.memo[i][j][N] = (self.getPath(m,n,N-1,i-1,j)%self.max + self.getPath(m,n,N-1,i+1,j)%self.max + self.getPath(m,n,N-1,i,j-1)%self.max + self.getPath(m,n,N-1,i,j+1)%self.max)%self.max
		return self.memo[i][j][N]

    


s = Solution()
print s.findPaths(30,24,23,26,12)
#print s.findPaths(2,2,2,0,0)