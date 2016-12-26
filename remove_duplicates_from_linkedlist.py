class Node(object):
	def __init__(self,data):
		self.data = data
		self.next = None


class LinkedList(object):
	def __init__(self):
		self.head = None

	def display(self):
		ptr = self.head
		if ptr==None:
			print 'empty list'
			return
		while ptr!=None:
			print ptr.data
			ptr=ptr.next

		print ''

	def delete(self,data):
		curr = self.head
		if curr==None:
			print 'list is empty'
			return
		if self.head.data == data:
			self.head = self.head.next
			return
		prev = None
		while(curr!=None):
			if curr.data == data:
				prev.next = curr.next
			prev=curr
			curr=curr.next

	def deleteDuplicate(self):
		if self.head==None:
			print 'empty list'
			return
		else:
			curr = self.head
			while curr!=None:
				forward = curr.next
				prev = curr
				while forward!=None:
					if forward.data == curr.data:
						prev.next = forward.next
						forward = forward.next
					else:
						prev = forward
						forward = forward.next

				curr = curr.next

	def deleteDuplicateLinear(self):
		d = {}
		if self.head==None:
			print 'empty list'
			return
		else:
			curr = self.head
			prev = curr
			d[curr.data] = 1
			curr = curr.next
			while curr!=None:
				if curr.data in d:
					prev.next = curr.next
				else:
					prev = curr
					d[curr.data] = 1

				curr = curr.next









data = [1,2,1,3,4,3,1,2,4,10]
l = LinkedList()

prev = None
for i in data:
	n = Node(i)
	if l.head==None:
		l.head = n
	else:
		prev.next = n
	prev = n

l.display()
l.deleteDuplicateLinear()
l.display()

