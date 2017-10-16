N = 9
parent = [-1 for i in range(N)]

def findParent(a):
	if parent[a] == -1:
		return a
	else:
		return findParent(parent[a])

def union(a,b):
	x = findParent(a)
	y = findParent(b)
	if x==y:
		print "Cycle detected while connecting ",a," and", b
		return
	parent[x] = y

def addEdge(a,b):
	union(a,b)

print parent
addEdge(7,6)
print parent
addEdge(2,8)
print parent
addEdge(6,5)
print parent
addEdge(0,1)
print parent
addEdge(5,2)
print parent
addEdge(1,2)
print parent
addEdge(8,6)
print parent




