class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        table = [[1 if (j==n-1 or i==m-1) else 0 for j in range(n)] for i in range(m)]
        for row in range(m-2,-1,-1):
            for col in range(n-2,-1,-1):
                table[row][col] = table[row+1][col]+table[row][col+1]
        return table[0][0]