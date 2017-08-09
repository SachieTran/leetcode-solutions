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
        self.node_list = []
        self.queue = deque()
        self.queue.append(root)
        self.queue.append('#')
        while self.queue:
        	#self.showQueue()
        	current = self.queue.popleft()
        	if current=='#':
        		if not self.queue:
        			break
        		else:
        			self.queue.append('#')
        			self.node_list.append('#')
        			continue
        	if current.left!=None:
        		self.queue.append(current.left)
        		self.node_list.append('#')
        	if current.right!=None:
        		self.queue.append(current.right)
        		self.node_list.append('#')
        	print self.node_list
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

