# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def heightNode(self,node):
        if not node:
            return 0
        else:
            lheight = self.heightNode(node.left)
            rheight = self.heightNode(node.right)

            if lheight>rheight:
                return lheight+1
            else:
                return rheight+1
                
    def printGivenLevel(self,root,level,l):
        if root == None:
            return
        if level == 1:
            l.append(root.val)
            return l
        if level>1:
            self.printGivenLevel(root.left,level-1,l)
            self.printGivenLevel(root.right, level-1,l)
            return l
            
    def printTreeAllLevels(self,root):
        h = self.heightNode(root)
        allLevels = []
        for i in range(1,h+1):
            l = []
            allLevels.append(self.printGivenLevel(root,i,l))
        
        return allLevels
        
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        return self.printTreeAllLevels(root)
        