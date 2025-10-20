import pygame as pg  
class Button:
	def __init__(self , btn_text , btn_font , btn_position , btn_func):
		self.btn_surface = btn_font.render(btn_text , False , (0 , 0 , 0))
		self.btn_rect = self.btn_surface.get_rect(midbottom=btn_position)
		self.btn_rect.x -= 1
		self.btn_rect.y -= 1
		self.btn_rect.width += 2
		self.btn_rect.height += 2
		self.btn_func = btn_func
	
	def check_hover_button(self):
		mouse_pos = pg.mouse.get_pos()
		return self.btn_rect.collidepoint(mouse_pos)

	def show(self , surface):
		pg.draw.rect(surface  , (255 , 255 , 255),self.btn_rect)
		surface.blit(self.btn_surface , self.btn_rect)

class Label:
	def __init__(self , lbl_text , lbl_font , position):
		self.text_surface = lbl_font.render(lbl_text , False , (0 , 0 , 0))
		self.rect = self.text_surface.get_rect(topleft = position)
	def show(self , surface):
		surface.blit(self.text_surface , self.rect)