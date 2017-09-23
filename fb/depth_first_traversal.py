from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def BFS(self, start_node):
		visited = [False]*len(self.graph)
		q = []
		q.append(start_node)
		while(len(q)>0):
			node = q.pop(0)
			print node
			visited[node] = True
			for adjascent in self.graph[node]:
				if not visited[adjascent]:
					q.append(adjascent)

	def DFS(self, start_node):
		visited = [False]*len(self.graph)
		stack = []
		stack.append(start_node)
		while len(stack)>0:
			node = stack.pop(-1)
			print node
			visited[node] = True
			for adjascent in self.graph[node]:
				if not visited[adjascent]:
					stack.append(adjascent)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(2, 0)
g.addEdge(3, 3)
#g.BFS(2)
g.DFS(2)