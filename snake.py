# Importing the pygame library to help simplify drawing the snake
import pygame as pg  

# Creating the node class that will be used to construct the tail
class node:
	def __init__(self , position):
		self.position = position

# Creating the snake class
class snake:
	def __init__(self , position , size):
		self.position = position
		self.tail = [node([position[0]-1 , position[1]]),node([position[0]-2 , position[1]])]
		self.size = size
		self.direction = [1 , 0]
		self.interval = 0.25
		self.current_time = pg.time.get_ticks()

	def reset(self):
		self.position = [5 , 5]
		self.tail = [node([self.position[0]-1 , self.position[1]]),node([self.position[0]-2 , self.position[1]])]
	
	# This function will be responsible for the snakes movement in the game
	def move(self):
		current_time = pg.time.get_ticks()
		if self.interval <= ((current_time - self.current_time)/1000):
			self.current_time = current_time
			temp_pos = self.position.copy()
			self.position[0] += self.direction[0]
			self.position[1] += self.direction[1]
			if self.position[0] > (800//self.size[0])-1:
				self.position[0] = 0
			elif self.position[0] < 0:
				self.position[0] = (800//self.size[0])-1
			if self.position[1] > (600//self.size[1])-1:
				self.position[1] =0
			elif self.position[1] < 0:
				self.position[1] = (600//self.size[1])-1
			for i in range(len(self.tail)):
				new_temp = self.tail[i].position.copy()
				self.tail[i].position = temp_pos.copy()
				temp_pos = new_temp
	# Function to make the snake grow when it eats something
	def grow(self):
		self.tail.append(node(self.tail[-1].position))
		pass
	# Checking if the snake can eat a fruit.
	def check_eat(self , froot):
		if self.position == froot.position:
			self.grow()
			return True
		else:
			return False
		
	# Checking if the snake bit itself.
	def check_bite(self):
		for point in self.tail:
			if self.position == point.position:
				return True
		return False
	
	# This function will draw the snake on the screen
	def draw(self , screen):
		head_rect = (self.position[0]*self.size[0] , self.position[1]*self.size[1] , self.size[0] , self.size[1])
		pg.draw.rect(screen , (255 , 0 , 0) , head_rect)
		for point in self.tail:
			point_rect = (point.position[0]*self.size[0] , point.position[1]*self.size[1] , self.size[0] , self.size[1])
			pg.draw.rect(screen , (0 , 255 , 0) , point_rect)