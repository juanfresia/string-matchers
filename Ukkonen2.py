class SuffixTree():
	
	def __init__(self, text):
		self.text = text	#reference to text
		self.suffix_link = None
		self.len = -1
		self.children = {}
		
	def __str__(self):
		if self.is_leaf():
			return "REACHED LEAF"
		children_nodes = []
		for ref, child in self.children.items():
			#children_nodes.append('(' + self.text[ref[0]:ref[1]] + ',' + child.__str__() +')' )
		return  'children: ' + str(children_nodes)
		
	def attach(self, letter, refs):
		self.children[letter] = (refs, SuffixTree(self.text))
		
	def extend_all(self, ext):
		suffix_present = False
		for letter, child in self.children.items():
			if child.is_leaf():
				#extend suffix by increasing end position
				self.children[letter] = ((ref[0], ref[1]+1), self.children.pop(ref)) #ver si esto se puede hacer mas lindo
				suffix_present = suffix_present or (ext == letter)		
			else:
				return child.extend_all()
		return suffix_present
		
	def is_leaf(self):
		return len(self.children) == 0
	
	def contains_suffix(self, substr):
		if not substr[0] in self.children:
			return False
		suffix = text[self.children[substr[0]][0] : len(substr)]
		return suffix == substr
			
	def match_at_AP(self, edge, active_len, c):
		if edge not in self.children:
			raise ValueError("INVALID EDGE")
		suffix = text[self.children[edge][0][0]:self.children[edge][0][1]]

		if (active_len == len(suffix) -1):
			#The end of this active edge has been reached.
			#We return the next active node together with a boolean
			#that indicates if the character c matches the end of this edge.
			return (suffix[active_len] == c, self.children[edge][2], c, 1)
		#Return a boolean indicating if 'c' matches the character
		#at the active_len position in this edge, and self (because the
		#next active node will still be self since the end of the edge
		#has still not been reached).
		return (suffix[active_len] == c, self, edge, active_len)
		
class Ukkonen(SuffixTree):
	
	def __init__(self, text):#, root = None):
		if (len(text) <= 1):
			raise ValueError("Give me a longer text")
		super(Ukkonen, self).__init__(text + "$")
		self.active_node = self
		self.active_edge = (0, '\0x')
		self.active_length = 0
		self.remainder = 0
	
	
	
	
	
	
	
	def build_tree(self):
		#self.attach(text[0],(0,1))
		for i in range(1, len(self.text)):
			self.remainder += 1
			self.extend_all(text[i])
			while(self.remainder > 0):
				if (self.active_length == 0) and not active_node.contains_suffix(text[i]):
					self.attach(text[i],(i,i+1))	#create new edge from root
					self.remainder -= 1
				elif (self.active_length > 0):
					#find active node:
					match, self.active_node, self.active_edge, self.active_length = self.active_node.match_at_AP(self.active_edge, self.active_length, text[i])
					if not match:
						#create internal node from current active_node
						
					else:
						#continue to the next phase
						self.active_length += 1
						continue
				elif (self.active_length == 0) and (text[i] in self.children):
					#Rule 3 is a show stopper
					#Check whether there is an edge from root starting with
					#the current character text[i]
					self.active_edge = (i, text[i])
					self.active_length += 1
					continue

		return self
		
		
		
		
		
		
		
		
		
		
		
def ukkonen_algorithm(text):
	return Ukkonen(text).build_tree()
		
def test_ukkonen():
#	text_1 = "abc"
	print("STARTING...")
	text_2 = "abcabxabcd"
#	utree = ukkonen_algorithm(text_1)
	utree = ukkonen_algorithm(text_2)
	print(utree.__str__())

test_ukkonen()
