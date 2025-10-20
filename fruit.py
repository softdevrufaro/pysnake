class fruit:
	def __init__(self , position , size):
		self.position = position
		self.rect = (position[0]*size[0] , position[1]*size[1] , size[0] , size[1])
		self.eaten = False