class Menu:
	
	def __init__(self, lst, index=0):
		self.lst = lst
		self.index = index
	
	def to_the_right(self):
		self.index += 1
		
	def display(self):
		self.index %= len(self.lst)
		new = self.lst.copy()
		new[self.index] = [new[self.index]]
		return str(new)