# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)<=0:
            return None
        if len(nums)==1:
            return TreeNode(nums[0])
        maxElement = max(nums)
        maxIndex = nums.index(maxElement)
        root = TreeNode(maxElement)
        root.left = self.constructMaximumBinaryTree(nums[:maxIndex])
        root.right = self.constructMaximumBinaryTree(nums[maxIndex+1:])
        
        return root