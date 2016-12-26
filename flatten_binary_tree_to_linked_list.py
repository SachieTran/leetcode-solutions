# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack(object):
    def __init__(self):
        self.top = None
    def push(self, node):
        if self.top == None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
            
    def pop(self):
        if self.top == None:
            print 'stack underflow'
            return
        elif self.top.next == None:
            node = self.top
            self.top = None
            return node.data
        else:
            node = self.top
            self.top = self.top.next
            return node.data

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
            

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = Stack()
        p = root
        
        while p!=None or not stack.isEmpty():
            if p.right!=None:
                node = Node(p.right)
                stack.push(node)
            if p.left!=None:
                p.right = p.left
                p.left = None
            elif not stack.isEmpty():
                temp = stack.pop()
                p.right = temp
            p = p.right
                
        