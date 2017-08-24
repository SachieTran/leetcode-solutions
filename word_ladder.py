import Queue

dictionary = ['POON', 'PLEE', 'SAME', 'POIE', 'PLEA', 'PLIE', 'POIN']

def isAdjascent(word1, word2):
	dist = 0
	for i in range(len(word1)):
		if word1[i]!=word2[i]:
			dist+=1

	return dist==1


adj_map = {}

for word in dictionary:
	adj_map[word] = []
	for word2 in dictionary:
		if isAdjascent(word, word2) and word!=word2:
			adj_map[word].append(word2)


visited = {}
min_dist = {word:float("inf") for word in dictionary}
Q = Queue.PriorityQueue()

start = 'TOON'
target = 'POIN'

Q.put((0,start))

flag = False
while not Q.empty():
	queueEnd = Q.get()
	curentDist, currentWord = queueEnd[0], queueEnd[1]
	visited[currentWord] = curentDist
	if currentWord==target:
		print currentWord
		print 'Target reached with distance', curentDist+1 
		flag = True
		break
	for word in dictionary:
		if isAdjascent(currentWord, word) and min_dist[word]>(curentDist+1) and word not in visited:
			print currentWord
			Q.put((curentDist+1, word))

if not flag:
	print 'Target cannot be reached'








