class TrieNode(object):
	def __init__(self, data):
		self.data = data
		self.children = {}
		self.end = False

class Trie(object):
	def __init__(self):
		self.root = {}

	def addWord(self, word):
		
		start = word[0]
		ptr = None
		if start in self.root:
			ptr = self.root[start]
		else:
			node = TrieNode(start)
			self.root[start] = node
			ptr = node
		
		for c in word[1:]:
			if c in ptr.children:
				ptr = ptr.children[c]
			else:
				node = TrieNode(c)
				ptr.children[c] = node
				ptr = node
		ptr.end = True


	def displayUtil(self, ptr, s):
		if ptr.end == True:
			print s+ptr.data
			return
		else:
			for c in ptr.children:
				self.displayUtil(ptr.children[c],s+ptr.data)

	def displayTrie(self):
		for c in self.root:
			self.displayUtil(self.root[c],"")


trie = Trie()
trie.addWord("bye")
trie.addWord("ball")
trie.displayTrie()




