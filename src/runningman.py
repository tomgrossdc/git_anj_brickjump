# runningman.py
#
# Copyright (C) 2017 -  Tom Gross
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
import pygame
import sys
from pygame.sprite import Sprite

class RunningMan(Sprite):
	def __init__(self,bj_settings,screen):
		super(RunningMan,self).__init__()
		self.screen = screen
		self.bj_settings=bj_settings
		#self.image=pygame.image.load('images/alien75.bmp')
		self.image=pygame.image.load('images/runningman/runningman_0.bmp')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()

		# Start in left corner
		#self.rect.centerx= self.screen_rect.centerx
		#self.rect.centery=self.screen_rect.centery
		self.rect.y = self.screen_rect.height-6*bj_settings.brick_height
		self.rect.centerx = bj_settings.brick_width*2
		self.center = float(self.rect.centerx)
		self.man_forward_speed = 2
		self.man_up_speed = 1
		self.Front = False
		self.Floor = True
		self.climbing_time = 0
		self.state="Falling"  # or Falling  or Climbing


	def update(self,bj_settings,bricks):
		self.changestate(bj_settings,bricks)
		self.moveman(bj_settings)

	def changestate(self,bj_settings,bricks):
		# Check collisions to decide transition to a new state
		# Reset the state to Climbing, Running or Falling
		collisions = pygame.sprite.spritecollide(self,bricks,False)
		#Front=False
		#Floor=False
		i=0
		minx= 15
		miny=15
		d1y=1000
		d3x=1000
		dx=20000
		dy=20000
		FRT=False
		FLR=False
		lencol=len(collisions)
		for col in collisions :
			if col.pickedbrick:
				lencol-=1
				continue
			#i+=1
			dx=min(dx,abs(self.rect.centerx-col.rect.centerx))
			dy=min(dy,abs(self.rect.centery-col.rect.centery))
			d1y=self.rect.y-col.rect.y
			if col.rect.y < self.rect.y :
				# col box is above runningman (ie colboxy is smaller than selfy) must be a wall
				#sign of d3x indicates: box in front - (climb) box behind + (run away)
				d3x=self.rect.x-col.rect.x
			#print (i,"lencol=",lencol," self,col=",self.rect.x,self.rect.y,col.rect.x,col.rect.y,dx,dy,d1y,d3x)
		#lencol=len(collisions)
		if lencol==0:
			#mid air, fall down till hit a floor
			if self.state=="Climbing":
				# climbed into the air. drop a bit and start running
				self.state="Running"
				self.rect.y+=self.man_up_speed
			else:
				self.state="Falling"
				#print("else",self.state)
				
			#print("0 overlap ",d1y,dx,dy,self.state)
		elif lencol==1:
			# straddling a top box corner or all floor or all front
			# if all floor or all front, dont change
			# if dy is equal to halfwidths then run forward (into air if needed)
			#if d1y==(bj_settings.brick_height-self.rect.height)/2:
			#	self.state="Running"

			# if falling goes to only one overlap, it must have hit a floor
			if self.state=="Falling":
				self.state="Running"
			#print("1 overlap ",d1y,dx,dy)
		elif lencol==2:
			# either all floor or all front. Dont change
			if self.state=="Falling":
				self.state="Running"
			i=1
		elif lencol==3 or lencol==4 :	
			#print("3or4 ",d3x,d1y,self.state," lencol=",lencol)
# corner. move up or forward, depending on min dx<0 for the brick which has highest y (min up)
			#sign of d3x indicates: box in front - (climb) box behind + (run away)
			if d3x<0 :
				self.state="Climbing"
			else:
				self.state="Climbing" # was Running
		else:
			# touching four at once? Already bad
			print("Five touchs",self.rect.x,self.rect.y,self.state," lencol=",lencol)
			self.state="Climbing"
			#sys.exit()
		
			

	def moveman(self,bj_settings):
		# Move the man according to self.state = Climbing, Running or Falling
		#print(self.rect.x,self.rect.y, self.state, self.climbing_time, lencol,self.rect.height,bj_settings.brick_height)

		bj_settings.timecounter+=1
		imagenumber=(bj_settings.timecounter/4)%8
		imagename='images/runningman/runningman_%d.bmp' % (imagenumber)
		self.image=pygame.image.load(imagename)
		if self.state=="Climbing":
			self.climbing_time +=1
			if self.climbing_time > bj_settings.max_brick_steps:
				self.climbing_time=0
				self.state="Falling"
				self.rect.x-=5*bj_settings.brick_speed_factor
			else:
				self.rect.y-=self.man_up_speed
				self.rect.x-=bj_settings.brick_speed_factor
		if self.state=="Running":
			# no wall in front, but a good floor, go forward
			self.climbing_time=0
			self.rect.x+=self.man_forward_speed
		if self.state=="Falling":
			self.climbing_time=0
			# no floor, fall
			self.rect.y+=self.man_up_speed
			self.rect.x-=bj_settings.brick_speed_factor
			
	def blitme(self):
		""" Draw brick at its current location """
		self.screen.blit(self.image, self.rect)
		
