class Solution(object):
	def findRecurring(self, s):
		print s
		m = {}
		start = 0
		for i,val in enumerate(s):
			if val in m:
				return (s[0:m[val]] + "(" + s[m[val]:i] + ")")
			else:
				m[val] = i
				start+=1
		return s

	def fractionToDecimal(self, numerator, denominator):
	    """
	    :type numerator: int
	    :type denominator: int
	    :rtype: str
	    """
	    if numerator == 0 and denominator == 0:
	    	return "NaN"
	    if numerator == 0:
	    	return "0"
	    if denominator == 0:
	    	return "NaN"
	    sign = 1
	    if numerator < 0:
	    	sign *= -1
	    	numerator *= -1
	    if denominator < 0:
	    	sign *= -1
	    	denominator *= -1

	    result = str(numerator*1.0/denominator)
	    number,decimal = result.split('.')
	    if len(decimal)==1 and decimal == '0':
	    	if sign == -1:
	    		number = "-" + number
	    		return number
	    	return number

	    newDecimal = self.findRecurring(decimal)
	   
	    result = number+'.'+newDecimal

	    if sign == -1:
	    	result = "-" + result
	    return result

s = Solution()
print s.fractionToDecimal(1,333)