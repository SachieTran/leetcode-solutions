class Solution(object):
	def findLongestWithKUnique(self, s, k=2):
		#print s
		table = {}
		longestSubstring = ""
		start = 0
		end = 0
		for c in s:
			#print c, table, start, end
			if c in table:
				table[c]+=1
			else:
				table[c] = 1
				while len(table)>k:
					table[s[start]]-=1
					if table[s[start]]==0:
						del table[s[start]]
					start+=1
			if (end - start) > len(longestSubstring):
					longestSubstring = s[start:end+1]
			end+=1

		return longestSubstring

input = "abcbbbbcccbdddadacb"
s = Solution()
print "Solution-->",s.findLongestWithKUnique(input)
