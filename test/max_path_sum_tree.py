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


def maxSumPath(root):
	if root.left == None and root.right == None:
		return root.data, [root.data]
	else:
		rightVal = float("-inf")
		leftVal = float("-inf")
		rightPath = []
		leftPath = []

		if root.right != None:
			rightVal, rightPath = maxSumPath(root.right)
		if root.left != None:
			leftVal, leftPath = maxSumPath(root.left)
		if leftPath == None:
			leftPath = []
		if rightPath == None:
			rightPath = []
		if rightVal>leftVal:
			if root.data > (rightVal+root.data):
				return root.data, [root.data]
			else:
				return rightVal+root.data, rightPath.append(root.data)
		else:
			if root.data > (leftVal+root.data):
				return root.data, [root.data]
			else:
				return leftVal+root.data, leftPath.append(root.data)


root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(10)
root.left.left = TreeNode(20)
root.left.right = TreeNode(1)
root.right.right = TreeNode(-25)
root.right.right.left = TreeNode(3)
root.right.right.right = TreeNode(4)

#inorderTraversal(root)

print maxSumPath(root)



