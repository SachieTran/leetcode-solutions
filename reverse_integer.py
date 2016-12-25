class Solution(object):
    def reverseString(self, s):
        if len(s)==1:
            return s
        else:
            return s[-1]+self.reverseString(s[:-1])


    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = ''
        x = str(x)
        if x[0] == '-' or x[0] == '+':
            sign = x[0]
            x = x[1:]

        x = self.reverseString(x)

        x = int(x)
        x = int(sign+str(x))
        
        return x


s = Solution()
print s.reverse(0)