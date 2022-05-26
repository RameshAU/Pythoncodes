# multiple inheritance
#two or more base class and 1 derived class
class father:#base class
	def fishing(self):
		print("fishing from father")
	def chess(self):
		print("chess from father")
		
class mother:#base class
	def cooking(self):
		print("cooking from mother")
	def chess(self):
		print("chess from mother")
		
class daughter(mother,father):#1 derived class
	def cricket(self):
		print("she knows cricket")
	
p=daughter()
p.cricket()
p.cooking()
p.fishing()
p.chess()