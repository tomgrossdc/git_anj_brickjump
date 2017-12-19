#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- 
#
# main.py
# Copyright (C) 2017  Tom Gross <tgrossdc@gmail.com>
# 
# git_anj_jump is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# git_anj_jump is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

print "Hello World! git_anj_jump.py"


import sys
import time

import pygame
from pygame.sprite import Group
from pygame.sprite import LayeredUpdates 
from pygame.time import Clock
from settings import Settings
from brick import Brick
from brick import Pickup
import game_functions as gf
from runningman import RunningMan
import scoreboard as sb
from levels import ReadLevels



def startup_game():
# First Time Initialization Only
	bj_settings=Settings()
	allLevels=ReadLevels(bj_settings)
	bj_settings.levelnum=0
	bj_settings.column_heights=allLevels[bj_settings.levelnum].column_heights
	bj_settings.column_num =-1
	bj_settings.maxnumpickedbricks=allLevels[bj_settings.levelnum].maxnumpickedbricks
	pygame.init()
	screen=pygame.display.set_mode((bj_settings.screen_width,bj_settings.screen_height))
	pygame.display.set_caption("GitHub Version DecBranch brickjump.py")
	clock = pygame.time.Clock()
	pickup = Pickup(bj_settings,screen)
	#print("pickup sprite",pickup.rect.x)
	return bj_settings,allLevels, screen, clock, pickup

def reset_game(bj_settings,screen,num_bricks):
	
	# Set up the Group of bricks LayeredUpdates is a class that uses Group, 
	# so it has added features, like  Nothing 
	bricks = Group()

	bj_settings.numpickedbricks=0
	""" Make most recent screen visible"""
	""" Start up the bricks with a floor, then add running man"""
	bj_settings.column_pos = bj_settings.screen_width
	while bj_settings.column_pos>0:
		screen.fill(bj_settings.bg_color)
		#gf.check_events(bj_settings, screen, brick, pickup)
		bricks.update()
		bj_settings.column_pos -= bj_settings.brick_speed_factor
		#print ("columnpos=",bj_settings.column_pos)

		if bj_settings.column_pos % bj_settings.brick_width == 0 :
			gf.create_column(bj_settings,screen,bricks,num_bricks)	
		#bricks.draw(screen)
		#pygame.display.flip()
		#time.sleep(.003)
	return bricks

def run_game():

	[bj_settings, allLevels, screen, clock, pickup] = startup_game()

	num_bricks=1
	bricks=reset_game(bj_settings,screen,num_bricks)
	
	#
	# Add a running man standing on top of first brick, with 2x forward speed
	runningman=RunningMan(bj_settings,screen)

		
	while True:
		screen.fill(bj_settings.bg_color)
		ReStartOnR=gf.check_events(bj_settings, screen, bricks,pickup)
		Winner=False
		Loser=False
		if runningman.rect.centerx<0: 
			Loser=True
			bj_settings.losses+=1
			if bj_settings.losses==bj_settings.maxlosses :
				print(" You Lost")
				sys.exit()
		if runningman.rect.centerx>(bj_settings.screen_width-2*bj_settings.brick_width): 
			Winner=True
			bj_settings.wins+=1
			bj_settings.levelnum+=1
			bj_settings.levelnum=min(bj_settings.levelnum,len(allLevels)-1)
			print(bj_settings.levelnum," len allLevels-1 ",len(allLevels)-1)
		if ReStartOnR or Loser or Winner:
# Start a new run. Initialize scores and bricks
			bj_settings.column_heights=allLevels[bj_settings.levelnum].column_heights
			bj_settings.maxnumpickedbricks=allLevels[bj_settings.levelnum].maxnumpickedbricks
			bj_settings.column_num =-1
			bricks=reset_game(bj_settings,screen,num_bricks)
			runningman.rect.centerx = 2*bj_settings.brick_width
			runningman.rect.centery = bj_settings.screen_height-3*runningman.rect.height
			Winner=False
			Loser=False
		
		#brick.blitme()
		#bricknew.blitme()
#		gf.update_bricks(bj_settings,screen,bricks)
		bricks.update()
		runningman.update(bj_settings,bricks)
		gf.update_columns(bj_settings,screen,bricks,num_bricks)
		
		runningman.blitme()	
		bricks.draw(screen)
		textbricks="%s:    Num Bricks: %d/%d" % (allLevels[bj_settings.levelnum].title, bj_settings.numpickedbricks , bj_settings.maxnumpickedbricks)
		textscore="Num Lives: %d/%d   WINS=%d" % (bj_settings.maxlosses-bj_settings.losses , bj_settings.maxlosses, bj_settings.wins)
		xyposition=20,10
		sb.set_box(bj_settings,  screen, textscore, xyposition)
		xyposition=20,40
		sb.set_box(bj_settings,  screen, textbricks, xyposition)
		pygame.display.flip()
		clock.tick(50)
		pygame.display.set_caption("GitHub Version DecBranch brickjump.py fps: " + str(clock.get_fps()))
		time.sleep(.003)


print "brickjump.py from Anjuta Programmes/python-brickjump/src"
print "r-> reset ; s-> stop"
run_game()

