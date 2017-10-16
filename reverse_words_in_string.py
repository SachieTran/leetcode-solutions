import re
class Solution(object):
    def _reverse(self, s):
        return s[::-1]
        
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return s
        if s == " ":
            return ""
        if len(s) == 1:
            return s
        s = re.sub(r'\s+',' ',s)
        start = 0
        reverseWords = ""
        i = 0
        while i<len(s):
            if s[i] == " ":
                i+=1
                start+=1
            else:
                break
        while i<len(s):
            if s[i] == " ":
                if start == i:
                    reverseWords = reverseWords + " "
                    start = i+1
                else:
                    word = self._reverse(s[start:i])
                    start = i+1
                    reverseWords = reverseWords + " " + word
            #print i,len(reverseWords)
            i+=1
        #print i,start
        if start <= i:
            word = self._reverse(s[start:i])
            reverseWords = reverseWords + " " + word
        #print reverseWords
        return self._reverse(reverseWords).lstrip().rstrip()
    

input = "   a   b "
s = Solution()
#print s.reverseWords(input)
print s._reverse("a b")