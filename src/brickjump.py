# brickjump.py
import sys
import time
import pygame
from settings import Settings
import scoreboard as sb
from levels import Level

import json

bj_settings=Settings()

#def run_game():
pygame.init()
screen=pygame.display.set_mode((bj_settings.screen_width,bj_settings.screen_height))
pygame.display.set_caption("March UpHill")
screen.fill(bj_settings.bg_color)
textscore="Num Lives: %d/%d   WINS=%d" % (bj_settings.maxlosses-bj_settings.losses , bj_settings.maxlosses, bj_settings.wins)
xyposition = 20, 30
sb.set_box(bj_settings,  screen, textscore, xyposition)



#run_game()

"""read a json file with various level data
add to a list a new object based on the json data


"""

levelfilename="LevelData.json"
with open(levelfilename) as f:
	level_data=json.load(f)
AllLevels=[]
x=30
y=40
xyposition= x,y


for level_dict in level_data:
    lvl=Level(bj_settings)
    lvl.column_heights = level_dict['column_hieghts']
    lvl.maxnumpickedbricks = level_dict['maxpickedbricks']
    lvl.title = level_dict['Level Name']
    #sb.set_box(bj_settings,  screen, textscore, xyposition)
    y+=15
    xyposition= x,y
    lvl.display(bj_settings,screen,xyposition)
    print(level_dict['Level Name'])
    AllLevels.append(lvl)


print(AllLevels)

pygame.display.flip()
time.sleep(5)


