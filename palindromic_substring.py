class Solution(object):

	def checkPalindrome(self, s):
		if len(s) == 1:
			return True
		if len(s) == 2:
			if s[0] == s[1]:
				return True
			else:
				return False

		if s[0] == s[-1]:
			return True and self.checkPalindrome(s[1:-1])
		else:
			return False

	def updateHash(self, tempString, startPosition):
		if (tempString,startPosition) in self.is_palindrome:
			self.count += 1
		else:
		 	if (tempString, startPosition) not in self.not_palindrome:
				if self.checkPalindrome(tempString):
					self.is_palindrome[(tempString, startPosition)] = 0
					self.count += 1
    			else:
    				self.not_palindrome[(tempString, startPosition)] = 0


	def countSubstrings(self, s):
		if len(set(s))==1:
			return len(s)*(len(s)+1)/2
		self.is_palindrome = {(val,i):0 for i,val in enumerate(s)}
		self.not_palindrome = {}
		self.count = len(s)
		for i in xrange(len(s)-1):
			for j in range(i+1, len(s)):
				tempString = s[i:j+1]
				self.updateHash(tempString, i)
		return len(self.is_palindrome.keys())


#s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
s = 'aaaa'
print s
p = Solution()
print p.countSubstrings(s)

			
			
			
