import Queue
import networkx as nx
import matplotlib.pyplot as plt
import random

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

	def displayGraph(self, result):
		G = nx.Graph()
		for nodeId in self.nodes:
			G.add_node(nodeId)
		for nodeId in self.nodes:
			for adjascentNodeId in self.nodes[nodeId].adjascent.keys():
				G.add_edge(nodeId, adjascentNodeId, weight=self.nodes[nodeId].adjascent[adjascentNodeId])
		pos = nx.circular_layout(G)
		plt.title(result)
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
					return 'Shortest path from %s to %s is %d'%(id1,id2,currentNodeDist)
			visited[currentNodeId] = currentNodeDist
			for adjascentNodeId in self.nodes[currentNodeId].adjascent.keys():
				if adjascentNodeId not in visited:
					if distances[adjascentNodeId] > (currentNodeDist + self.nodes[currentNodeId].adjascent[adjascentNodeId]):
						distances[adjascentNodeId] = currentNodeDist + self.nodes[currentNodeId].adjascent[adjascentNodeId]
					Q.put((distances[adjascentNodeId], adjascentNodeId))



g = Graph()

# Choose number of nodes and edges in the graph. This will create a graph with given number of nodes and edges
numberOfNodes = 10
numberOfEdges = 20

for nodeId in xrange(1, numberOfNodes+1):
	g.addNode(nodeId)

edgeCount = 0 
while edgeCount<numberOfEdges:
	fromNode = random.randint(1, g.num_vertices)
	toNode = random.randint(1, g.num_vertices)
	if not fromNode==toNode:
		g.addEdge(fromNode, toNode, random.randint(1,100))
		edgeCount+=1


result = g.shortestPath(1,4)
g.displayGraph(result) 


