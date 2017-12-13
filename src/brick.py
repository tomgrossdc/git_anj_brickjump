# brick.py
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
from pygame.sprite import Sprite

class Brick(Sprite):
	def __init__(self,bj_settings,screen):
		super(Brick,self).__init__()
		self.screen = screen
		self.bj_settings=bj_settings
		imagename='images/redbrick75%d.bmp' % (bj_settings.brick_pile_number%3)
		self.image=pygame.image.load(imagename)
		#self.image=pygame.image.load('images/redbrick751.bmp')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()

		# Start in lower right corner
		self.rect.x= self.screen_rect.width - self.rect.width
		self.rect.y = self.screen_rect.height -self.rect.height
		self.rect.x = self.screen_rect.width
		self.center = float(self.rect.centerx)
		self.pickedbrick=False

		self.brickserielnumber=bj_settings.brick_pile_number
		bj_settings.brick_pile_number +=1
		bj_settings.brick_width= self.rect.width
		bj_settings.brick_height= self.rect.height
		bj_settings.max_brick_steps = self.rect.height*bj_settings.max_num_brick_climb +2

	def update(self):
		self.rect.x-=self.bj_settings.brick_speed_factor

	
	def blitme(self):
		""" Draw brick at its current location """
		self.screen.blit(self.image, self.rect)
		
		

class Pickup(Sprite):
	def __init__(self,bj_settings,screen):
		super(Pickup,self).__init__()
		self.screen = screen
		self.bj_settings=bj_settings
		self.image=pygame.image.load('images/pickup.bmp')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()

		# Start in lower right corner
		self.rect.x= self.screen_rect.width - self.rect.width
		self.rect.y = self.screen_rect.height -self.rect.height
		self.rect.x = self.screen_rect.width

	def update(self):
		self.rect.x-=self.bj_settings.brick_speed_factor

	
	def blitme(self):
		""" Draw brick at its current location """
		self.screen.blit(self.image, self.rect)
		
		
		
		