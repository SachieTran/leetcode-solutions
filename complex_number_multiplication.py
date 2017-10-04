class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1,b1 = map(int, a.replace('i','').split("+"))
        a2,b2 = map(int, b.replace('i','').split("+"))
        return str(a1*a2+b1*b2*-1)+'+'+str(a1*b2+a2*b1)+'i'