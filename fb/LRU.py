def referencePage(page, hash, dl):
	if page in hash:
		print "*** cache hit ***\n"
		hash[page] = dl.cacheHit(hash[page])
	else:
		print "*** cache miss ***\n"
		hash[page] = dl.cacheMiss(page)

class Node(object):
	def __init__(self, data):
		self.prev = None
		self.next = None
		self.data = data


class DoubleLinkedList(object):
	def __init__(self, size):
		self.head = None
		self.count = 0
		self.MAX_SIZE = size

	def addNode(self, data):
		node = Node(data)
		self.count+=1
		if self.head==None:
			self.head = node
			return
		ptr = self.head
		while ptr.next!=None:
			ptr = ptr.next
		ptr.next = node
		node.prev = ptr

	def display(self):
		if self.head == None:
			print "List is empty"
			return
		ptr = self.head
		while ptr!=None:
			print ptr.data,
			ptr = ptr.next
		print ""

	def cacheHit(self, node):
		if self.head==node:
			return node
		node.prev.next = node.next
		if node.next!=None:
			node.next.prev = node.prev
		node.prev = None
		node.next = self.head
		self.head = node
		return node

	def cacheMiss(self, page):
		node = Node(page)
		if self.head == None:
			self.head = node
			self.count+=1
			return node
		print "Cache count",self.count
		if self.count >= self.MAX_SIZE:
			ptr = self.head
			while ptr.next!=None:
				ptr = ptr.next
			ptr.prev.next = None
		else:
			self.count+=1
		self.head.prev = node
		node.next = self.head
		self.head = node
		return node


dl = DoubleLinkedList(4)

hash = {}
referencePage(1, hash, dl)
dl.display()
referencePage(2, hash, dl)
dl.display()
referencePage(3, hash, dl)
dl.display()
referencePage(1, hash, dl)
dl.display()
referencePage(4, hash, dl)
dl.display()
referencePage(5, hash, dl)
dl.display()
