class TreeNode(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right =None


def inorderTraversal(root):
	if root == None:
		return
	else:
		inorderTraversal(root.left)
		print root.data,
		inorderTraversal(root.right)

def preordertraversal(root):
	if root == None:
		return 
	else:
		print root.data,
		preordertraversal(root.left)
		preordertraversal(root.right)

def postorderTraversal(root):
	if root == None:
		return
	else:
		postorderTraversal(root.left)
		postorderTraversal(root.right)
		print root.data,

def minDepth(root):
	if root.left == None and root.right == None:
		return 1
	else:
		if root.left == None:
			return 1+minDepth(root.right)
		elif root.right == None:
			return 1+minDepth(root.left)
		else:
			return min(minDepth(root.right), minDepth(root.right)) + 1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

#inorderTraversal(root)
print minDepth(root)
