class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<=1:
            return 1
        else:
            if int(s[0:2])<=26:
                return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
            else:
                return self.numDecodings(s[1:])

s = Solution()
input = "1"
print s.numDecodings(input)