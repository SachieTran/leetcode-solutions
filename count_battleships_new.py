class Solution(object):
	def displayBoard(self, board):
		for  i in xrange(len(board)):
			for j in xrange(len(board[0])):
				print board[i][j],
			print ''
		print ''

	def countBattleShips(self, board):
		board = [[str(c) for c in row] for row in board]
		count = 0
		for i in xrange(len(board)):
			for j in xrange(len(board[0])):
				#self.displayBoard(board)
				if board[i][j] == 'X':
					count+=1
					board[i][j]='.'
					ptrX = i
					ptrY = j

					if ptrY+1<len(board[0]) and board[ptrX][ptrY+1]=='X':
						ptrY+=1
						while ptrY<len(board[0]):
							if board[ptrX][ptrY]=='X':
								board[ptrX][ptrY]='.'
								ptrY+=1
							else:
								break
					elif ptrX+1<len(board) and board[ptrX+1][ptrY]=='X':
						ptrX+=1
						while ptrX<len(board):
							if board[ptrX][ptrY]=='X':
								board[ptrX][ptrY]='.'
								ptrX+=1
							else:
								break
		return count

input = ["X..X","...X","...X","XX.."]
s = Solution()
print s.countBattleShips(input)
