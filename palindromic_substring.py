class Solution(object):
	def checkPalindrome(self, s):
		if len(s)==1:
			return True
		if len(s)==2:
			if s[0]==s[1]:
				return True
			else:
				return False

		if s[0]==s[-1]:
			return True and checkPalindrome(s[1:-1])
		else:
			return False

	def countSubstrings(self, s):
	    self.is_palindrome = {}
	    self.not_palindrome = {}
	    count = len(s)
	    for i in xrange(len(s)):
	    	for left in xrange(i-1,-1,-1):
	    		tempString = s[left:i+1]
	    		if tempString in self.is_palindrome:
	    			count+=1
	    		else:
	    		 	if tempString not in self.not_palindrome:
						if self.checkPalindrome(tempString):
							self.is_palindrome[tempString] = 0
		    				count+=1
		    			else:
		    				self.not_palindrome[tempString] = 0

	    	for right in xrange(i+1,len(s)):
	    		tempString = s[i:right+1]
	    		if tempString in self.is_palindrome:
	    			count+=1
	    		else:
	    			if tempString not in self.not_palindrome:
						if(self.checkPalindrome(tempString)):
		    				self.is_palindrome[tempString] = 0
		    				count+=1
		    			else:
		    				self.not_palindrome[tempString] = 0


	    return is_palindrome.keys()


p = Solution()
p.countSubstrings('aaa')
