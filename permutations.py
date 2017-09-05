class Solution(object):
    
    def perm(self, a, l, r):
		if l==r:
			print a
		else:
			for i in range(l,r+1):
				a[l], a[i] = a[i], a[l]
				print i,l,r 
				self.perm(a, l+1, r)
				a[l], a[i] = a[i], a[l]



    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.perm(nums, 0, len(nums)-1)

s = Solution()
s.permute([1,2,3,4])
