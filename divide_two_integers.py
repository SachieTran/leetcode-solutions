import sys

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0  and divisor == 0:
            return -1
        if divisor == dividend:
            return 1
        MAX_INT = sys.maxint
        sign = 1
        if dividend < 0:
            sign*=-1
            dividend*=-1
        if divisor < 0:
            sign*=-1
            divisor*=-1
        if divisor == 0:
            return -1
        if dividend == 0:
            return 0
        if divisor == 1:
            result = dividend*sign
            if result < -2147483648:
                return -2147483648
            if result > 2147483647:
                return 2147483647
            return result

        result = 0
        shifts = 0
        while divisor <= dividend:
            #print "outer while"
            shifts  = 0
            while (divisor << shifts+1) < dividend:
                #print "inner while"
                shifts+=1
            result+= (2**shifts)
            dividend -= (divisor << shifts)
            #print dividend, result, shifts
        
        result = result*sign
        if result < -2147483648:
            return -2147483648
        if result > 2147483647:
            return 2147483647
        return result

s = Solution()
print s.divide(2,2)
        
        
        