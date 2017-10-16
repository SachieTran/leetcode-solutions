kvmap = {
	"1":"abc",
	"2":"def",
	"3":"ght",
	"4":"jkl",
	"5":"mno",
	"6":"pqrs",
	"7":"tuv",
	"8":"wxyz"
}


class Node(object):
	def __init__(self, s, number):
		self.s = s
		self.number = number
		self.children = {}
		self.number_of_children = 0
		self.end = False

def hasSameCharacters(s):
	c = s[0]
	flag = True
	for i in range(1, len(s)):
		if s[i]!=c:
			flag = False
	return flag

def isValid(s):
	if s=="":
		return True
	if s[0] not in kvmap:
		return False
	if len(s)==1:
		return True
	if len(s)>4:
		return False
	if not hasSameCharacters(s):
		return False
	else:
		if len(s)==4 and (s[0] in ["1","2","3","4","5","7"]):
			return False
	return True

def evaluate(s):
	if s=="":
		return ""
	if len(s)==1:
		return kvmap[s][0]
	else:
		c = s[0]
		if isValid(s):
			return kvmap[c][len(s)-1]

def displayWords(root, result):
	if root.end:
		print result+root.s
		return
	else:
		for child in root.children:
			displayWords(root.children[child], result+root.s)


def letterCombinations(parent):
	s = parent.number
	for i in range(1,len(s)+1):
		if isValid(s[:i]):
			e = evaluate(s[:i])
			node = Node(e, s[i:])
			parent.number_of_children+=1
			parent.children[parent.number_of_children] = node
			if not s[i:] == "":
				letterCombinations(node)
			else:
				node.end = True

root = Node("","8888")
letterCombinations(root)

displayWords(root,"")


