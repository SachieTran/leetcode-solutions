class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        count = 0
        i = 0
        j = 0
        n = len(matrix)
        temp = matrix[i][j]
        while(count<=n*n):
            print matrix
            new_i = j
            new_j = n-i-1
            new_temp = matrix[new_i][new_j]
            matrix[new_i][new_j] = temp
            temp = new_temp
            i = new_i
            j = new_j
            count+=1
        print "result"
        print matrix
        return matrix

s = Solution()
A = [[1,2,3],[4,5,6],[7,8,9]]
print A
print ""
s.rotate(A)