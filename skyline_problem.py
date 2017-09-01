import Queue as Q

data_queue = Q.PriorityQueue()

def putDataInQueue(x):
	data_queue.put((x[0],x[2], 's'))
	data_queue.put((x[1],x[2], 'e'))

def dispayQueue(q):
	while not q.empty():
		print q.get()

input = [ [2, 9, 10], [3, 7, 15], [5 ,12 ,12], [15, 20, 10], [19, 24, 8] ]

map(putDataInQueue, input)

dispayQueue(data_queue)
