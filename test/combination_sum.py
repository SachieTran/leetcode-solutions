class Node(object):
	def __init__(self, flag):
		self.flag = flag
		self.paths = []


def display(table):
	
	for i in range(len(table)):
		for j in range(len(table[0])):
			if table[i][j].flag:
				print table[i][j].paths,
			else:
				print "0",
		print ""
	print ""

def combinationSum(coins, target):
	coins.insert(0,0)
	
	table = [[Node(False) for j in range(target+1)] for i in range(len(coins))]

	for i in range(len(table)):
		table[i][0].flag = True
	

	for i in range(1,len(table)):
		for j in range(1, target+1):
			#print i,j
			#print coins[i], table[i-1][j].flag
			if coins[i] == j:
				table[i][j].flag = True
			elif table[i-1][j].flag:
				table[i][j].flag = True
			elif (j-coins[i]) > 0:
				if table[i][j-coins[i]].flag:
					table[i][j].flag = True			
			if coins[i] == j:
				table[i][j].paths.append([j])
				
			if table[i-1][j].flag:
				table[i][j].paths += table[i-1][j].paths

			if j-coins[i] > 0:
				if table[i][j-coins[i]].flag:
					for l in table[i][j-coins[i]].paths:
						table[i][j].paths.append(l + [coins[i]])
	return table[len(coins)-1][target]


coins = [2,3,6,7]
target = 7

print combinationSum(coins, target).paths
