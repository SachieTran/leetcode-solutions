class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """

        if N==1:
            return 1
        if N==2:
        	return 2

        self.count = 0

       	self.getArrangements(N, [i for i in range(N+1)], [0 for i in range(N+1)],1)

       	return self.count


    def getArrangements(self, N, arr, visited, pos):
    	print arr, visited, pos
    	if pos>N:
    		self.count+=1
    		return
    	for i in range(pos, N+1):
    		if (arr[i]%pos==0 or pos%arr[i]==0) and visited[i]!=1:
    			tmp = arr[i]
    			arr[i] = arr[pos]
    			arr[pos] = tmp
    			visited[pos] = 1
    			self.getArrangements(N, arr, visited, pos+1)
    			visited[pos] = 0
    			tmp = arr[i]
    			arr[i] = arr[pos]
    			arr[pos] = tmp

s = Solution()
print s.countArrangement(7)