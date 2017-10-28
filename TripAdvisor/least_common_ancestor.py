# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param val1 : integer
    # @param val2 : integer
    # @return an integer
    LCA = -1

    def _lca(self, A, val1, val2):
        if not A:
            return False
        if (not A.left) and (not A.right):
            if (A.val == val1) or (A.val == val2):
                return True
            else:
                return False

        leftFlag = self._lca(A.left, val1, val2)
        rightFlag = self._lca(A.right, val1, val2)

        if leftFlag and rightFlag:
            if self.LCA == -1:
                self.LCA = A.val

        if (A.val == val1) or (A.val == val2):
            if leftFlag or rightFlag:
                if self.LCA == -1:
                    self.LCA = A.val
                    return True

        return (leftFlag or rightFlag or ((A.val == val1) or (A.val == val2)))

    def lca(self, A, val1, val2):
        self._lca(A, val1, val2)
        return self.LCA


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

s = Solution()
print s.lca(root, 5,7)
