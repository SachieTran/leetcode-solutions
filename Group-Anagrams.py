class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            tuple_sorted = tuple(sorted(s))
            if tuple_sorted in d:
                d[tuple_sorted].append(s)
            else:
                d[tuple_sorted] = [s]
        l = []
        for key,val in d.iteritems():
            l.append(val)
        return l
        
        