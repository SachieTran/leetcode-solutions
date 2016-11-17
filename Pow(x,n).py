class Solution(object):
    
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        #return x**n
        print x,n
        if n==0:
            return 1
        temp = 0
        if n>0:
            temp = self.myPow(x,n/2)
        else:
            temp = self.myPow(x,(n+1)/2)
        if n%2==0:
            return temp*temp
        else:
            if n>0:
                return x*temp*temp
            else:
                return (1.0/x)*temp*temp
        
        

s = Solution()
print s.myPow(2,-3)