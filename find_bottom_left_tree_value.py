from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        self.node_list = []
        self.queue = deque()
        self.queue.append(root)
        self.node_list.append(root.val)
        self.node_list.append('#')
        self.queue.append('#')
        while self.queue:
            # self.showQueue()
            current = self.queue.popleft()
            if current == '#':
                if not self.queue:
                    break
                else:
                    self.queue.append('#')
                    self.node_list.append('#')
                continue
            self.node_list.append(current.val)
            if current.left!=None:
                self.queue.append(current.left)
            if current.right!=None:
                self.queue.append(current.right)
            #print self.node_list
            # self.showQueue()

        return self.node_list[len(self.node_list) - 1 - self.node_list[::-1].index('#')+1]

    def showQueue(self):
        print 'Queue:',
        for node in self.queue:
            if node!='#':
                print node.val,
            else:
                print node,
        print ''

