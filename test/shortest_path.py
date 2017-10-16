import Queue
class Vertex(object):
	def __init__(self, id):
		self.id = id
		self.adjascent = {}

class Graph(object):
	def __init__(self):
		self.vertices = {}
		self.num_vertices = 0

	def addVertex(self, id):
		v = Vertex(id)
		self.vertices[id] = v
	
	def addEdge(self, a, b, weight):
		if a not in self.vertices:
			v = Vertex(a)
			self.vertices[a] = v
		if b not in self.vertices:
			v = Vertex(b)
			self.vertices[b] = v

		self.vertices[a].adjascent[b] = weight
		self.vertices[b].adjascent[a] = weight

	def shortestPath(self, start, end):
		visited = {}
		distances = {i:float("inf") for i in self.vertices}

		Q = Queue.PriorityQueue()
		Q.put((0, start))
		distances[start] = 0
		while not Q.empty():
			distance, vertext_id = Q.get()
			visited[vertext_id] = True
			if vertext_id == end:
				print "******* Destination found *******"
				print "Shortest path is of length:", distances[vertext_id]
				break
			else:
				vertex = self.vertices[vertext_id]
				for adj in vertex.adjascent:
					if adj not in visited:
						distances[adj] = min(distances[adj], distances[vertext_id]+vertex.adjascent[adj])
						Q.put((distances[adj], adj))


g = Graph()
for i in range(9):
	g.addVertex(i)
g.addEdge(0,1,4)
g.addEdge(0,7,8)
g.addEdge(1,7,11)
g.addEdge(1,2,8)
g.addEdge(7,8,7)
g.addEdge(7,6,1)
g.addEdge(2,3,7)
g.addEdge(2,8,2)
g.addEdge(3,5,14)
g.addEdge(3,4,9)
g.addEdge(5,2,4)
g.addEdge(5,6,2)
g.addEdge(4,5,10)
g.addEdge(8,6,6)

g.shortestPath(0,4)












			





