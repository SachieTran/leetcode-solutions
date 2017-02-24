class Node(object):
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def preOrder(root):
	if root!=None:
		preOrder(root.left)
		print root.data," ",
		preOrder(root.right)


def constructTrees(start, end):
	l = []
	if start>end:
		l.append(None)
		return l

	for i in range(start,end+1):
		leftTrees = constructTrees(start,i-1)
		rightTrees = constructTrees(i+1,end)

		for j in range(len(leftTrees)):
			print "length of left",len(leftTrees),"length of right",len(rightTrees)
			left = leftTrees[j]
			for k in range(len(rightTrees)):
				right = rightTrees[k]
				#print i
				node = Node(i)
				node.left = left
				node.right = right
				l.append(node)

	return l


for i in constructTrees(1,4):
	preOrder(i)
	print ""




