from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:
            return []
        self.max_list = []
        max = float("-inf")
        self.queue = deque()
        self.queue.append(root)
        self.queue.append('#')
        while self.queue:
        	#self.showQueue()
        	current = self.queue.popleft()
        	if current=='#':
        		if not self.queue:
        			self.max_list.append(max)
        			break
        		else:
        			self.queue.append('#')
        			self.max_list.append(max)
        			max = float("-inf")
        			continue
        	else:

        		if current.val>max:
        			max = current.val
        	if current.left!=None:
        		self.queue.append(current.left)
        	if current.right!=None:
        		self.queue.append(current.right)
        	#self.showQueue()

        return self.max_list

    def showQueue(self):
    	print 'Queue:',
    	for node in self.queue:
			if node!='#':
				print node.val,
			else:
				print node,
        print ''

