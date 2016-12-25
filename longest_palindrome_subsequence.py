s = "abhayayahba"

def longestPalSubstring(input):
	maxLength = 0
	start = 0
	low = 0 
	high = 0 
	length = len(input)

	for i in range(1,length):
		low = i-1
		high = i
		while low>=0 and high<length and input[low]==input[high]:
			if high-low+1>maxLength:
				maxLength = high-low+1
				start=low
			low-=1
			high+=1

	for i in range(1, length):
		low = i-1
		high = i+1
		while low>=0 and high<length and input[low]==input[high]:
			if high-low+1>maxLength:
				start = low
				maxLength = high-low+1
			low-=1
			high+=1

	return "Maximum pal subtring: ",input[start:start+maxLength]," with length: ",maxLength


print longestPalSubstring(s)




