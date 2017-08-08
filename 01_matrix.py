from collections import deque
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        height, width = len(matrix), len(matrix[0])
        result = [[float("inf") if matrix[i][j]!=0 else 0 for j in xrange(width)] for i in xrange(height)]
        queue = deque((i,j) for i in xrange(len(matrix)) for j in xrange(len(matrix[0])) if matrix[i][j]==0)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
        	currI, currJ = queue.popleft()
        	for direction in directions:
        		i,j = currI+direction[0], currJ+direction[1]
        		if not(0 <= i < height) or not(0 <= j < width) or result[i][j] <= result[currI][currJ]+1:
        			continue
        		queue.append((i,j))
        		result[i][j] = result[currI][currJ]+1
        #self.display(matrix)
        return result

    def display(self, matrix):
		for i in xrange(len(matrix)):
			for j in xrange(len(matrix[0])):
				print matrix[i][j],
			print ''
		print '' 

input = [[0, 0, 0],[0, 1, 0],[1, 1, 1]]
s = Solution()
s.display(s.updateMatrix(input))
