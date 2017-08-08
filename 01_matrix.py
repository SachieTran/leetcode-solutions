class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        height, width = len(matrix), len(matrix[0])
        result = [[-inf if matrix[i][j]!=0 else 0 for i in range(width)] for j in range(height)]
        print result

input = [[0, 0, 0],[0, 1, 0],[1, 1, 1]]
s = Solution()
s.updateMatrix(input)
