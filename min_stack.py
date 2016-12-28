class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.minData = []
        self.Top = -1
        self.minTop = -1
        
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.Top == -1:
            self.data.append(x)
            self.minData.append(x)
            self.Top += 1
            self.minTop+=1
        else:
            currMin = self.minData[self.minTop]
            if x<currMin:
                self.minData.append(x)
            else:
                self.minData.append(currMin)
            self.minTop+=1
            self.data.append(x)
            self.Top+=1
                
        

    def pop(self):
        """
        :rtype: void
        """
        if self.Top == -1:
            return 
        else:
            self.data.pop()
            self.minData.pop()
            self.Top-=1
            self.minTop-=1
            return
        

    def top(self):
        """
        :rtype: int
        """
        if self.Top == -1:
            return None
        else:
            return self.data[self.Top]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.Top == -1:
            return None
        return self.minData[self.minTop]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()