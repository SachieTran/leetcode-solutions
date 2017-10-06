class BinaryHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0

	def percUp(self, i):
		while i//2>=1:
			if self.heapList[i]<self.heapList[i//2]:
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[i//2]
				self.heapList[i//2] = tmp
				i = i//2
			else:
				return

	def insert(self, item):
		self.heapList.append(item)
		self.currentSize+=1
		self.percUp(self.currentSize)


	def percDown(self,i):
		while i*2 <= self.currentSize:
			leftVal = 100000
			rightVal = 100000
			minIndex = -1
			if i*2+1 <= self.currentSize:
				rightVal = self.heapList[i*2+1]
			leftVal = self.heapList[i*2]
			if leftVal<rightVal:
				minIndex = 2*i
			else:
				minIndex = 2*i+1
			if self.heapList[i]>self.heapList[minIndex]:
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[minIndex]
				self.heapList[minIndex] = tmp
				i = minIndex
			else:
				break

	def buidheap(self, a):
		i = len(a)//2
		self.heapList = [0] + a
		self.currentSize = len(a)
		while i>0:
			self.percDown(i)
			i-=1

	def delMin(self):
		if self.currentSize==0:
			print "Empty heap"
			return
		minVal = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.heapList.pop()
		self.currentSize -= 1
		self.percDown(1)
		return minVal


	def display(self):
		for i in range(1,self.currentSize+1):
			print self.heapList[i],
		print ''


s = BinaryHeap()
s.buidheap([3,4,6,2,1,5])
s.display()

while s.currentSize>0:
	print s.delMin()




