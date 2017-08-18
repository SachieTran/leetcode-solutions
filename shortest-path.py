class Node(object):
	def __init__(self, id):
		self.id = id
		self.adjascent = {}

	def displayNode(self):
		print 'Node -->', self.id
		print 'Adjascent Nodes -->', self.adjascent.keys()


class Graph(object):
	def __init__(self):
		self.nodes = {}
		self.num_vertices = 0

	def addNode(self, id):
		self.num_vertices+=1
		node = Node(id)
		self.nodes[id] = node
		return node

	def addEdge(self, id1, id2, dist):
		if id1 not in self.nodes:
			self.addNode(id1)
		if id2 not in self.nodes:
			self.addNode(id2)

		self.nodes[id1].adjascent[id2] = dist
		self.nodes[id2].adjascent[id1] = dist

	def displayGraph(self):
		for node in self.nodes:
			self.nodes[node].displayNode()



g = Graph()
g.addNode(1)
g.addNode(2)
g.addNode(3)
g.addNode(4)
g.addNode(5)

g.addEdge(1,2,2)
g.addEdge(1,3,5)
g.addEdge(1,5,8)
g.addEdge(5,2,1)
g.addEdge(3,4,4)
g.addEdge(3,5,2)

g.displayGraph()
