# Draw the Finish Line
import pygame




class Finish_Line():
	def __init__(self,settings):
		self.settings=settings
		self.checkerbox=10
		self.Black=(0,0,0)
		self.Blue=(0,0,0)
		self.White=(255,255,255)
		self.xleft=settings.finish_x
            
	def display(self,settings,screen):
		draw_finish_line(settings,screen)
			

def draw_finish_line(settings,screen):
	fl=Finish_Line(settings)
	
	ytop=0
	xleft=settings.finish_x
	widthbox=fl.checkerbox
	height=fl.checkerbox
	chkcolors=(fl.Black,fl.White)
	iclr=0
	
	while ytop<settings.screen_height:
		checkrect=pygame.Rect(xleft,ytop,widthbox,height)
		pygame.draw.rect(screen,chkcolors[iclr%2],checkrect,0)
		checkrect=pygame.Rect(xleft+fl.checkerbox,ytop,widthbox,height)
		pygame.draw.rect(screen,chkcolors[(iclr+1)%2],checkrect,0)
		ytop+=height
		iclr+=1

	