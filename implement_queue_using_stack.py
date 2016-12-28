class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.stack)==0:
            return
        if len(self.stack)==1:
            top = self.stack[0]
            self.stack.pop()
            return top
        else:
            s2 = []
            for i in range(len(self.stack)-1,0,-1):
                s2.append(self.stack[i])
                self.stack.pop()
            dequeue_element = self.stack[0]
            self.stack.pop()
            for i in range(len(s2)-1,-1,-1):
                self.stack.append(s2[i])
            
            
        

    def peek(self):
        """
        :rtype: int
        """
        if len(self.stack)==0:
            return None
        else:
            return self.stack[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stack)==0:
            return True
        else:
            return False
        