class Graph(object):
	def __init__(self, vertices):
		self.graph = {i:[] for i in xrange(vertices)}
		self.V = vertices
	
	def addEdge(self, a, b):
		if b in self.graph[a]:
			print "Edge already present"
		self.graph[a].append(b)

	def topologicalSort(self):
		visited = [False]*self.V
		stack = []
		for v in self.graph:
			if not visited[v]:
				self.topologicalSortUtil(v, visited, stack)
		print stack

	def topologicalSortUtil(self, v, visited, stack):
		visited[v] = True
		for adj in self.graph[v]:
			if not visited[adj]:
				self.topologicalSortUtil(adj, visited, stack)
		stack.append(v)


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.topologicalSort()

