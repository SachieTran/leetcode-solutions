class Solution(object):
    def checkPalindrome(self, x):
        if len(x) == 1:
            return True 
        elif len(x) == 2:
            if x[0] == x[1]:
                return True
            else:
                return False
        elif len(x)>2:
            if x[0] == x[-1]:
                return True and self.checkPalindrome(x[1:-1])
            else:
                return False
            
        
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        #if x[0] == '-' or x[0] == '+':
        #    x = x[1:]
        return self.checkPalindrome(x)


s = Solution()
print s.isPalindrome(1000021)