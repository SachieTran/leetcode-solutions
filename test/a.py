class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList():
    def __init__(self):
        self.head = None
    
    def addNode(self, data):
        print data
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        if self.head.next == None:
            self.head.next = node
            return
        print self.head
        ptr = self.head
        while ptr.next!=None:
            ptr = ptr.next
        ptr.next = node
        
    
    def display(self):
        if self.head == None:
            print "Empty list"
        ptr = self.head
        while(ptr):
            print ptr.data,
            ptr = ptr.next
        

ll = LinkedList()
ll.addNode(2)
ll.addNode(4)
ll.addNode(3)
ll.addNode(1)

ll.display()