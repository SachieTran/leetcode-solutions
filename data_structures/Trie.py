class TrieNode(object):
	def __init__(self):
		node_map = {}
		word_end_flag = False


class TrieTree(object):
	def __init__(self):
		self.root = TrieNode()

	def inserWord(self, word):
		ptr = self.root
		new_node = TrieNode()
		for i,ch in enumerate(word):
			if ch not in ptr.node_map:
				ptr.node_map[ch] = new_node
			ptr = new_node
			if i==len(word)-1:
				ptr.word_end_flag = True






