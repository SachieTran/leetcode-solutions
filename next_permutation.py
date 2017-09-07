#a = [5,1,1]
a = [100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,78,77,76,75,74,73,72,71,70,69,68,67,66,65,64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

class Solution(object):
    def rotate(self, a, start, end):
        while end>start:
            temp = a[start]
            a[start] = a[end]
            a[end] = temp
            start+=1
            end-=1
        return a

    def getIndexAfterRotation(self, i, start, end, n):
        while n>0:
            i-=1
            n-=1
            if i<start:
                i=end
        return i
    
    
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        a = nums
        pivot=len(a)-1
        while pivot>0 and a[pivot]<=a[pivot-1]:
            pivot-=1
        print pivot
        if pivot==0:
            nums = self.rotate(a, 0, len(a)-1)
        else:
	        a = self.rotate(a, pivot,len(a)-1)

	        right_target = pivot
	        while right_target<len(a)-1 and a[right_target]<=a[pivot-1]:
	            right_target+=1

	        temp = a[pivot-1]
	        a[pivot-1] = a[right_target]
	        a[right_target] = temp
	        nums = a
        print nums

s = Solution()
s.nextPermutation(a)

#rotate(0,len(a)-1)
#nextPermutation(a)
#print getIndexAfterRotation(2, 2,4,2)
