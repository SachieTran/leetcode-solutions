table = {}
class Solution(object):
    def _numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<=0:
            return 0
        elif len(s)==1:
            if int(s[0])==0:
                return 0
            else:
                return 1
        elif len(s)==2:
            if "0" in s:
                return 2-s.count("0")
            if int(s)<=26:
                return 2
            else:
                return 1

        else:
            r2 = self._numDecodings(s[0:2])
            return r2 + self._numDecodings(s[2:])

    
    def numDecodings(self, s):
        if len(s)==0:
            return 0
        if int(s)==0:
            return 0
        else:
            return self._numDecodings(s)


input = "000"
s = Solution()
print s.numDecodings(input)