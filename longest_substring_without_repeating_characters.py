class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #O(n^3) solution
        """
        max_length = 0
        for i in range(len(s)):
            d ={}
            temp_max = 0
            for j in range(i, len(s)):
                if s[j] in d:
                    break
                else:
                    d[s[j]] = 1
                    temp_max += 1
            if temp_max > max_length:
                max_length = temp_max
        return max_length
        """
        
        #O(n) solution
        d = {}
        curr_len = 0
        max_len = 0
        for i in range(len(s)):
            if s[i] in d:
                last_inst = d[s[i]]
                if last_inst >= (i - curr_len):
                    curr_len = i - last_inst
                    d[s[i]] = i
                else:
                    curr_len+=1
                    d[s[i]] = i
            else:
                d[s[i]] = i
                curr_len+=1
            if curr_len > max_len:
                max_len = curr_len
                
        return max_len
        
        
