#heights = [2,1,5,6,2,3]
heights = [2,1,2]
print "########## ", heights

class Solution(object):
	def largestRectangleArea(self, heights):
	    """
	    :type heights: List[int]
	    :rtype: int
	    """
	    index_stack = [0]
	    height_stack = [-1]
	    max_area = -1
	    if len(heights)==0:
	        return 0
	    if len(heights)==1:
	        return heights[0]
	    for i,height in enumerate(heights):
	        if i==0 or height>height_stack[-1]:
	            index_stack.append(i)
	            height_stack.append(height)

	        elif height<height_stack[-1]:
	            while len(height_stack)>0 and height<height_stack[-1]:
	                temp_height = height_stack.pop(-1)
	                temp_index = index_stack[-1]
	                max_area = max(max_area, temp_height*(i-temp_index))
	                if height_stack[-1]>height:
	                	index_stack.pop(-1)
	            height_stack.append(height)
	            
	    	#print index_stack,height_stack,max_area

	    while len(height_stack)>0:
	        temp_height = height_stack.pop(-1)
	        temp_index = index_stack.pop(-1)
	        max_area = max(max_area, temp_height*(i-temp_index+1))
	    
	    return max_area
	        
	    
	    
s = Solution()
print s.largestRectangleArea(heights)

		
