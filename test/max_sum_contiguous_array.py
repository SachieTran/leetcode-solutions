def maxSum(arr):
	currMax = 0
	globalMax = 0
	start = -1
	end = -1

	for i in range(len(arr)):
		if arr[i]+currMax <= 0:
			end = i-1
			if currMax>globalMax:
				globalMax = currMax
				end = i-1
			currMax = 0
			start = i+1
		else:
			currMax += arr[i]
			if currMax>globalMax:
				globalMax = currMax
				end = i

	print arr[start:end+1]

input = [-2,1,-3,4,-1,2,1,-5,4]
maxSum(input)
