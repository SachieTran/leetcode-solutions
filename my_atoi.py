def myAtoi(s):
        """
        :type str: str
        :rtype: int
        """
        result = 0
        sign = ''
        if s[0] == '-' or s[0] == '+':
        	sign = s[0]
        	s = s[1:]

        while s:
        	result = result*10 + int(s[0])
        	s = s[1:]

        if sign == '-':
        	result*=-1

        return result



print myAtoi('-100')