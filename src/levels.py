# levels.py
#
# Defines instances of new levels. Experiment in lists and dictionaries for objects.
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

import scoreboard as sb
import json

class Level():
        def __init__(self,settings):
            self.settings=settings
            self.column_heights= 1,2,3,1,2,3,1,2,3,1,2,3,4,8,6,5,4,3,4,5,6,1,2,4,4,5,10
            self.maxnumpickedbricks=6
            self.title=" "

        def display(self,settings,screen, xyposition):
            sb.set_box(settings,  screen, self.title, xyposition) 

def ReadLevels(bj_settings):
	levelfilename="LevelData.json"
	with open(levelfilename) as f:
		level_data=json.load(f)
		
	AllLevels=[]
	for level_dict in level_data:
		lvl=Level(bj_settings)
		lvl.column_heights = map(int,level_dict['column_hieghts'].split(','))
		print("level_dict", level_dict['column_hieghts'])
		print("lvl       ", lvl.column_heights)
		lvl.maxnumpickedbricks = int(level_dict['maxpickedbricks'])
		lvl.title = level_dict['Level Name']
		print(level_dict['Level Name'])
		AllLevels.append(lvl)
		
	return AllLevels
