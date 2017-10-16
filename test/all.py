*********************** Trie **************************

class TrieNode(object):
	def __init__(self, data):
		self.data = data
		self.children = {}
		self.end = False

class Trie(object):
	def __init__(self):
		self.root = {}

	def addWord(self, word):
		
		start = word[0]
		ptr = None
		if start in self.root:
			ptr = self.root[start]
		else:
			node = TrieNode(start)
			self.root[start] = node
			ptr = node
		
		for c in word[1:]:
			if c in ptr.children:
				ptr = ptr.children[c]
			else:
				node = TrieNode(c)
				ptr.children[c] = node
				ptr = node
		ptr.end = True


	def displayUtil(self, ptr, s):
		if ptr.end == True:
			print s+ptr.data
			return
		else:
			for c in ptr.children:
				self.displayUtil(ptr.children[c],s+ptr.data)

	def displayTrie(self):
		for c in self.root:
			self.displayUtil(self.root[c],"")


trie = Trie()
trie.addWord("bye")
trie.addWord("ball")
trie.displayTrie()

*********************** Permutation **************************

def perm(a, start, end):
	if start>=end:
		print a
	else:
		for i in range(start, end+1):
			tmp = a[start]
			a[start] = a[i]
			a[i] = tmp
			perm(a, start+1, end)
			tmp = a[start]
			a[start] = a[i]
			a[i] = tmp

input = [1,2,3,4 ]
perm(input, 0, len(input)-1)

*********************** Max Sub array **************************
a = [0, 13, -3,-25, 20 ,-3 ,-16 ,-23, 18, 20 ,-7, 12 ,-5 ,-22, 15 ,-4, 7]
print a

global_max_sum = 0
curr_sum = 0

left = -1
for i,val in enumerate(a):
	if val+curr_sum>0:
		curr_sum+=val
		if curr_sum>global_max_sum:
			global_max_sum=curr_sum
			right = i
	else:
		curr_sum = 0
		left = i+1

print global_max_sum, a[left:right+1]	

*********************** NQueens **************************
cols = {}
rows = {}
left_diagonals = {}
right_diagonals = {}

N = 4
board = [[0 for j in range(N)] for i in range(N)]

def display():
	for i in range(len(board)):
		for j in range(len(board[0])):
			print board[i][j],
		print ""
	print ""

def NQueens(target_row, N):
	
	if target_row >= N:
		display()
		return True
	else:
		for j in xrange(N):
			print "Looking for row", target_row
			print rows,cols,right_diagonals,left_diagonals
			display()
			if not (target_row in rows or j in cols or (target_row+j) in left_diagonals or (target_row-j) in right_diagonals):
				rows[target_row] = 1
				cols[j] = 1
				left_diagonals[target_row+j] = 1
				right_diagonals[target_row-j] = 1
				board[target_row][j] = "Q"
				
				if not NQueens(target_row+1, N):
					del rows[target_row]
					del cols[j]
					del left_diagonals[target_row+j]					
					del right_diagonals[target_row-j]
					board[target_row][j] = 0
				else:
					return True
			else:
				print "Cannot place queen at row",target_row, " column",j
		return False

NQueens(0, N)

*********************** Phone Letters Normal **************************

kvmap = {
	"1":"abc",
	"2":"def",
	"3":"ght",
	"4":"jkl",
	"5":"mno",
	"6":"pqrs",
	"7":"tuv",
	"8":"wxyz"
}

def wordCombinations(number, result):
	if len(number)==0:
		print result
		return

	for c in kvmap[number[0]]:
		wordCombinations(number[1:], result+c)

wordCombinations("11","")

*********************** Phone Letters Advanced **************************

kvmap = {
	"1":"abc",
	"2":"def",
	"3":"ght",
	"4":"jkl",
	"5":"mno",
	"6":"pqrs",
	"7":"tuv",
	"8":"wxyz"
}


class Node(object):
	def __init__(self, s, number):
		self.s = s
		self.number = number
		self.children = {}
		self.number_of_children = 0
		self.end = False

def hasSameCharacters(s):
	c = s[0]
	flag = True
	for i in range(1, len(s)):
		if s[i]!=c:
			flag = False
	return flag

def isValid(s):
	if s=="":
		return True
	if s[0] not in kvmap:
		return False
	if len(s)==1:
		return True
	if len(s)>4:
		return False
	if not hasSameCharacters(s):
		return False
	else:
		if len(s)==4 and (s[0] in ["1","2","3","4","5","7"]):
			return False
	return True

def evaluate(s):
	if s=="":
		return ""
	if len(s)==1:
		return kvmap[s][0]
	else:
		c = s[0]
		if isValid(s):
			return kvmap[c][len(s)-1]

def displayWords(root, result):
	if root.end:
		print result+root.s
		return
	else:
		for child in root.children:
			displayWords(root.children[child], result+root.s)


def letterCombinations(parent):
	s = parent.number
	for i in range(1,len(s)+1):
		if isValid(s[:i]):
			e = evaluate(s[:i])
			node = Node(e, s[i:])
			parent.number_of_children+=1
			parent.children[parent.number_of_children] = node
			if not s[i:] == "":
				letterCombinations(node)
			else:
				node.end = True

root = Node("","8888	")
letterCombinations(root)

displayWords(root,"")


*********************** Linked List **************************

class Node(object):
	def __init__(self, data):
		self.next = None
		self.data = data

class SingleLinkedList(object):
	def __init__(self):
		self.head = None

	def addNode(self, data):
		node = Node(data)
		if self.head == None:
			self.head = node
			return
		else:
			ptr = self.head
			while ptr.next!=None:
				ptr = ptr.next
			ptr.next = node

	def display(self):
		ptr = self.head
		while ptr!=None:
			print ptr.data,
			ptr = ptr.next
		print ""

	def reverseIterative(self):
		if self.head == None or self.head.next == None:
			return
		else:
			prev = None
			curr = self.head
			while(curr!=None):
				tmp = curr.next
				curr.next = prev
				prev = curr
				curr = tmp
			self.head = prev

	def reverseRecursive(self, ptr):
		if ptr.next == None:
			self.head = None
			self.head = ptr
			return ptr
		else:
			self.reverseRecursive(ptr.next).next = ptr
			ptr.next = None
			return ptr



ll = SingleLinkedList()
ll.addNode(3)
ll.addNode(4)
ll.addNode(8)
ll.addNode(2)
ll.addNode(1)

ll.display()
#ll.reverseIterative()
ll.reverseRecursive(ll.head)
ll.display()

*********************** Union Find **************************

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

*********************** Shortest Path **************************

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



*********************** Topological Sort **************************

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





*********************** Combination Sum **************************

class Node(object):
	def __init__(self, flag):
		self.flag = flag
		self.paths = []


def display(table):
	
	for i in range(len(table)):
		for j in range(len(table[0])):
			if table[i][j].flag:
				print table[i][j].paths,
			else:
				print "0",
		print ""
	print ""

def combinationSum(coins, target):
	coins.insert(0,0)
	
	table = [[Node(False) for j in range(target+1)] for i in range(len(coins))]

	for i in range(len(table)):
		table[i][0].flag = True
	

	for i in range(1,len(table)):
		for j in range(1, target+1):
			#print i,j
			#print coins[i], table[i-1][j].flag
			if coins[i] == j:
				table[i][j].flag = True
			elif table[i-1][j].flag:
				table[i][j].flag = True
			elif (j-coins[i]) > 0:
				if table[i][j-coins[i]].flag:
					table[i][j].flag = True			
			if coins[i] == j:
				table[i][j].paths.append([j])
				
			if table[i-1][j].flag:
				table[i][j].paths += table[i-1][j].paths

			if j-coins[i] > 0:
				if table[i][j-coins[i]].flag:
					for l in table[i][j-coins[i]].paths:
						table[i][j].paths.append(l + [coins[i]])
	return table[len(coins)-1][target]


coins = [2,3,6,7]
target = 7

print combinationSum(coins, target).paths


*********************** Gas Station **************************

public int canCompleteCircuit(int[] gas, int[] cost) {
	int sumRemaining = 0; // track current remaining
	int total = 0; // track total remaining
	int start = 0; 
 
	for (int i = 0; i < gas.length; i++) {
		int remaining = gas[i] - cost[i];
 
		//if sum remaining of (i-1) >= 0, continue 
		if (sumRemaining >= 0) { 
			sumRemaining += remaining;
		//otherwise, reset start index to be current
		} else {
			sumRemaining = remaining;
			start = i;
		}
		total += remaining;
	}
 
	if (total >= 0){
		return start;
	}else{
		return -1;
	}
}


*********************** Rotate Matrix **************************
def Rotate(a):
	N = len(a)
	for i in range(len(a)/2):
		for j in range(i, N-i-1):
			tmp = a[i][j]
			a[i][j] = a[N-j-1][i]
			a[N-j-1][i] = a[N-i-1][N-j-1]
			a[N-i-1][N-j-1] = a[j][N-i-1]
			a[j][N-i-1] = tmp
			display(a)


def display(a):
	for i in range(len(a)):
		for j in range(len(a[0])):
			print a[i][j],
		print ""
	print ""

a = [[1, 2, 3, 4,],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]

display(a)
print ""
Rotate(a)
display(a)


*********************** Knight Problem **************************

// C++ program to find minimum steps to reach to
// specific cell in minimum moves by Knight
#include <bits/stdc++.h>
using namespace std;
 
//  structure for storing a cell's data
struct cell
{
    int x, y;
    int dis;
    cell() {}
    cell(int x, int y, int dis) : x(x), y(y), dis(dis) {}
};
 
//  Utility method returns true if (x, y) lies inside Board
bool isInside(int x, int y, int N)
{
    if (x >= 1 && x <= N && y >= 1 && y <= N)
        return true;
    return false;
}
 
//  Method returns minimum step to reach target position
int minStepToReachTarget(int knightPos[], int targetPos[],
                                                   int N)
{
    //  x and y direction, where a knight can move
    int dx[] = {-2, -1, 1, 2, -2, -1, 1, 2};
    int dy[] = {-1, -2, -2, -1, 1, 2, 2, 1};
 
    //  queue for storing states of knight in board
    queue<cell> q;
 
    //  push starting position of knight with 0 distance
    q.push(cell(knightPos[0], knightPos[1], 0));
 
    cell t;
    int x, y;
    bool visit[N + 1][N + 1];
 
    //  make all cell unvisited
    for (int i = 1; i <= N; i++)
        for (int j = 1; j <= N; j++)
            visit[i][j] = false;
 
    //  visit starting state
    visit[knightPos[0]][knightPos[1]] = true;
 
    //  loop untill we have one element in queue
    while (!q.empty())
    {
        t = q.front();
        q.pop();
        visit[t.x][t.y] = true;
 
        // if current cell is equal to target cell,
        // return its distance
        if (t.x == targetPos[0] && t.y == targetPos[1])
            return t.dis;
 
 
        //  loop for all reahable states
        for (int i = 0; i < 8; i++)
        {
            x = t.x + dx[i];
            y = t.y + dy[i];
 
            // If rechable state is not yet visited and
            // inside board, push that state into queue
            if (isInside(x, y, N) && !visit[x][y])
                q.push(cell(x, y, t.dis + 1));
 
        }
    }
}
 
// Driver code to test above methods
int main()
{
    //  size of square board
    int N = 6;
    int knightPos[] = {4, 5};
    int targetPos[] = {1, 1};
 
    cout << minStepToReachTarget(knightPos, targetPos, N);
 
    return 0;
}



























