class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.s1.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        
        if len(self.s1)==0:
            return None
        if len(self.s1)==1:
            top = self.s1[0]
            self.s1.pop()
            return top
        else:
            s2 =[]
            for i in range(len(self.s1)-1):
                s2.append(self.s1[i])
                self.s1.pop()
            top = self.s1[0]
            self.s1.pop()
            self.s1 = s2
            
            
        

    def top(self):
        """
        :rtype: int
        """
        return self.s1[-1]
        
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.s1)==0:
            return True
        else:
            return False
        