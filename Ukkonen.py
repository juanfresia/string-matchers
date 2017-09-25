def ukkonen_preliminary_test():
	st = SuffixTree()
	st.attach("bx",4)
	st.attach("a",0)
	st.attach("xabx",2)
	st.children["a"].attach("xabx",1)
	st.children["a"].attach("bx",3)
	print(st)
	st.append_suffix_extension('Z')
	print(st)
#	st.rule_1("a", "W")
#	st.rule_1("axabx", "W")
	st.rule_1("axabxZ", "W")
	print(st)
		
class SuffixTree():
	
	def __init__(self, pos = -1):
		self.pos = pos
		self.children = {}
		self.size = 0
		
	def __str__(self):
		pos_str = ' Pos:{}'.format(self.pos)
		if self.is_leaf():
			return pos_str + ' , END'
		children_nodes = []
		for edge, child in self.children.items():
			children_nodes.append('(' +edge + ',' + child.__str__() +')' )
		return  pos_str + ', children: ' + str(children_nodes)
		
	def attach(self, suffix, pos):
		self.children[suffix] = SuffixTree(pos)
		self.size += 1
		
	def is_leaf(self):
		return len(self.children) == 0
		
	def append_suffix_extension(self, end_char):
		"""
		Receives a character to be added to every tree leaf: end_char.
		Unconditionally appends the indicated suffix extension to every edge connecting to a leaf node in the suffix tree.
		"""
		old_children = self.children
		self.children  = {}
		for suffix, child in old_children.items():
			if child.is_leaf():
				self.children[suffix + end_char] = child
			else:
				self.children[suffix] = child.append_suffix_extension(end_char)
		return self
	
	def rule_1(self, path, end_char):
		"""
		Receives a string path: path and a character: end_char.
		Appends the indicated end_char to every branch whose path coincides with the given string path.
		"""
		old_children = self.children
		self.children  = {}
#		print("CALLED WITH: path ={}, end_char={}".format(path, end_char))
		for suffix, child in old_children.items():
			if len(suffix) > len(path):
				self.children[suffix] = child
				continue
			else:
				match = (suffix[0] == path[0])
				i = 1
				while match and i < len(suffix):
					match = (suffix[i] == path[i])
					i+=1
				if not match:
#					print("MATCH FAIL: suffix {}, path:{}".format(suffix, path))
					self.children[suffix] = child
				elif not child.is_leaf():
#					print("MATCH AND CONTINUE: suffix {}, path:{}, continue with:{}".format(suffix, path, path[i:len(path)]))
					self.children[suffix] = child.rule_1(path[i:len(path)], end_char)
				else:
#					print("MATCH suffix {}, path:{}".format(suffix, path))
					self.children[suffix + end_char] = child
					
		return self
				
	#def rule_2(self):
	#def rule_3(self):
	
	#	path = suffix_ext[0:-1]
	#	if path in self.children and self.children[path].is_leaf():
	#		self.children[suffix_ext] = self.children.pop(suffix)
		
ukkonen_preliminary_test()
