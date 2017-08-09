class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ak = float("-inf")
        st = []
        print nums
        for i in reversed(xrange(len(nums))):
            print nums[i], ak, st
            if nums[i] < ak:
                print nums[i], ak, st
                return True
            else:
                while st and nums[i] > st[-1]:
                    ak = st.pop()
            st.append(nums[i])
            print ak, st

            print '##########'
        return False


s = Solution()
input = [1,3,4,2,4,3,2,1,2,3,4,3,2]
print s.find132pattern(input)