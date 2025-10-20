# Importing the pygame library 
import pygame as pg  

# Importing other necessary libraries and modules
from sys import exit  
from snake import snake 
from random import randint 
from UI import Button , Label
# Functions to control the game transition from one window to another.
def move_to_help():
	menu_flags["Run"] = False
	menu_flags["Start"] = False
	menu_flags["Help"] = True
	menu_flags["Quit"] = False

def move_to_start():
	menu_flags["Run"] = False
	menu_flags["Help"] = False
	menu_flags["Quit"] = False
	menu_flags["Start"] = True

def quit_game():
	menu_flags['Quit'] = True

def start_game():
	menu_flags["Start"] = False
	menu_flags["Help"] = False
	menu_flags["Quit"] = False
	menu_flags["Run"] = True
#function to restart the game
def game_restart():
	global player 
	global game_over_flag
	global score
	player = snake([5 , 5] , [10 , 10])
	game_over_flag = False
	score = 0

# Initializing pygame
pg.init()

# Creating the display and editing its look
screen = pg.display.set_mode((800 , 600))
pg.display.set_caption("Snake.py")

# Declaring the player
player = snake([5 , 5] , [10 , 10])
# declaring the world variable
world = []
for y in range(60):
	temp = []
	for x in range(80):
		temp.append((x , y))
	world.append(temp)
# Creating the score variable
score = 0
# Creating the fruits list that will contain the location of all fruits
fruits = []
for i in range(5):
	fruits.append((randint(0 , 80) , randint(0 , 60)))
game_over_flag = False
# creating a start time variable to maintain time in the game
start_time = pg.time.get_ticks()
# Creating the games default font
default_font = pg.font.Font(None , 50)
#Menu controls 
menu_flags = {"Run":False ,"Start":True , "Help":False , "Quit":False}
#Start Menu Buttons
start_menu_buttons = [Button("Play" , default_font , (400 , 150),start_game) , Button("Help" , default_font , (400 , 250),move_to_help) , Button("Quit" , default_font , (400 , 350),quit_game)]
# Help menu Buttons
help_menu_elements = [Label("Welcome to my snake game.",default_font , (10 , 60)) , Label("Use the arrow keys to move." , default_font , (10 , 120)) , Label("When the snake its the purple fruit it grows" , default_font , (10 , 180)) , Label("Eat as many fruit as you can without-" , default_font , (10 , 240)),Label("biting yourself" , default_font , (10 , 300)) , Button("Back to Menu" , default_font , (400 , 500) , move_to_start)]

# Game Over Elements
game_over = [Label("Game Over." , pg.font.Font(None , 80) , (200 , 60)) ,Label(f"Score: {score}",pg.font.Font(None , 80),(200,150)) , Button("Restart",default_font , (350 , 270) ,game_restart) , Button("Quit" , default_font , (350 , 400) , quit_game)]
# The main game loop 
while True:
	# Adding background color to the screen
	screen.fill("Yellow")
	# Getting screen input
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			exit()
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_SPACE:
				pg.quit()
				exit()
			if event.key == pg.K_DOWN:
				if player.direction == [0 , -1]:
					pass
				else:
					player.direction = [0 , 1]
			elif event.key == pg.K_UP:
				if player.direction == [0 , 1]:
					pass
				else:
					player.direction = [0 , -1]
			elif event.key == pg.K_LEFT:
				if player.direction == [ 1, 0]:
					pass
				else:
					player.direction = [-1 , 0]
			elif event.key == pg.K_RIGHT:
				if player.direction == [-1 , 0]:
					pass
				else:
					player.direction = [1 , 0]
	if menu_flags["Start"]:
		for element in start_menu_buttons:
			element.show(screen)
			if element.check_hover_button() and pg.mouse.get_pressed()[0]:
				element.btn_func()
	if menu_flags["Quit"]:
		pg.quit()
		exit()
	if menu_flags["Help"]:
		for element in help_menu_elements:
			element.show(screen)
			if type(element) == type(start_menu_buttons[0]):
				if element.check_hover_button() and pg.mouse.get_pressed()[0]:
					element.btn_func()
	if menu_flags["Run"]:
		if game_over_flag:
			for element in game_over:
				element.show(screen)
				if type(element) == type(start_menu_buttons[0]):
					if element.check_hover_button() and pg.mouse.get_pressed()[0]:
						element.btn_func()
		else:
			# Checking if the player ate any fruit
			player_tuple = (player.position[0] , player.position[1])
			if (player_tuple) in fruits:
				player.grow()
				score += 1
				fruits.pop(fruits.index(player_tuple))
			# Adding more fruits if some are eaten 
			current_time = pg.time.get_ticks()
			if (current_time - start_time)//1000 > 5  and len(fruits) < 5: 
				start_time = current_time
				fruits.append((randint(0 , 80) , randint(0,60)))
			# Drawing the fruits in the game.
			for fruit in fruits: 
				fruit_rect = (fruit[0]*10 , fruit[1]*10 , 10 , 10)
				pg.draw.rect(screen , "Purple" , fruit_rect)
			player.draw(screen)

			#Moving the player
			player.move()
			# Checking if the player has lost yet
			game_over_flag = player.check_bite()
			# Drawing the score on the game window
			score_font = pg.font.Font(None , 50)
			score_surface = score_font.render(str(score) , False , (0 , 0 , 0))
			score_rect = score_surface.get_rect(topleft = (0 , 0))
			screen.blit(score_surface , score_rect)
	# Updating the display
	pg.display.update()