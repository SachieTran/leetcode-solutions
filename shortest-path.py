import Queue
import networkx as nx
import matplotlib.pyplot as plt

class Node(object):
	def __init__(self, id):
		self.id = id
		self.adjascent = {id:0}

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
		G = nx.Graph()
		for nodeId in self.nodes:
			G.add_node(nodeId)
		for nodeId in self.nodes:
			for adjascentNodeId in self.nodes[nodeId].adjascent.keys():
				G.add_edge(nodeId, adjascentNodeId, weight=self.nodes[nodeId].adjascent[adjascentNodeId])
		pos = nx.spring_layout(G, iterations=50)
		nx.draw(G, pos, with_labels=True)
		labels = nx.get_edge_attributes(G,'weight')
		nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
		plt.show()






	def shortestPath(self, id1, id2):
		if id1==id2:
			return 'You want to go there where you already are'
		shortest_path = []
		distances = {id:float("inf") for id in self.nodes}
		visited = {id1:float("inf")}
		Q = Queue.PriorityQueue()
		Q.put((0,id1))

		while not Q.empty():
			current = Q.get()
			currentNodeId, currentNodeDist = current[1], current[0]
			if currentNodeId == id2:
					print 'Shortest path from %s to %s is %f'%(id1,id2,currentNodeDist)
					break
			visited[currentNodeId] = currentNodeDist
			for adjascentNodeId in self.nodes[currentNodeId].adjascent.keys():
				if adjascentNodeId not in visited:
					if distances[adjascentNodeId] > (currentNodeDist + self.nodes[currentNodeId].adjascent[adjascentNodeId]):
						distances[adjascentNodeId] = currentNodeDist + self.nodes[currentNodeId].adjascent[adjascentNodeId]
					Q.put((distances[adjascentNodeId], adjascentNodeId))



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
g.shortestPath(4,2)
