from collections import deque
class Solution(object):
	def displayBoard(self, board):
		for i in xrange(len(board)):
			for j in xrange(len(board[0])):
				print board[i][j],
			print ''
		print ''

	def checkNeighbor(self, board, location):
		directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
		number_of_adjascent_mines = 0
		for dir in directions:
			i,j = location[0]+dir[0], location[1]+dir[1]
			if (0<=i<self.height) and (0<=j<self.width):
				if board[i][j]=='M':
					number_of_adjascent_mines+=1
		return number_of_adjascent_mines

	def appendUnrevealed(self, board, location):
		directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
		for dir in directions:
			i,j = location[0]+dir[0], location[1]+dir[1]
			if (0<=i<self.height) and (0<=j<self.width):
				if board[i][j]=='E' and [i,j] not in self.queue:
					self.queue.append([i, j])


	def updateBoard(self, board, click):
	    """
	    :type board: List[List[str]]
	    :type click: List[int]
	    :rtype: List[List[str]]
	    """
	    symbols = ['E', 'M', 'B', 'X']
	    self.queue = deque()
	    self.queue.append(click)
	    self.height = len(board)
	    self.width = len(board[0])
	    while len(self.queue)>0:
	    	#print 'queue length:', len(self.queue)
	    	current_location = self.queue.popleft()
	    	current_val = board[current_location[0]][current_location[1]]
	    	#print current_location
	    	if current_val == 'M':
	    		board[current_location[0]][current_location[1]] = 'X'
	    		break
	    	number_of_adjascent_mines = self.checkNeighbor(board, current_location)
	    	#print 'number of adjascent mines:', number_of_adjascent_mines
	    	if number_of_adjascent_mines == 0:
	    		board[current_location[0]][current_location[1]] = 'B'
	    		self.appendUnrevealed(board, current_location)
	    	else:
	    		board[current_location[0]][current_location[1]] = str(number_of_adjascent_mines)
	    return board





input = [['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

s = Solution()
print 'Original Board'
print '------------------'
print s.displayBoard(input)
print '\n ------------------'
s.displayBoard(s.updateBoard(input,[1,2]))