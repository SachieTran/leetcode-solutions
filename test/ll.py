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
		prev = None
		curr = self.head
		while curr!=None:
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
		self.head = prev


ll = SingleLinkedList()
ll.addNode(3)
ll.addNode(4)
ll.addNode(8)
ll.addNode(2)
ll.addNode(1)

ll.display()
ll.reverseIterative()
ll.display()