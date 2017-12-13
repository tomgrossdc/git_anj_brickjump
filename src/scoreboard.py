#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- 
#
# scoreboard.py, part of python_brickjump.py
# Copyright (C) 2017  Tom Gross <tgrossdc@gmail.com>
# 
# python-brickjump is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# python-brickjump is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame
from pygame.locals import *
from pygame.compat import unichr_, unicode_
import sys
import locale

def set_box(bj_settings,  screen, text, xyposition):
    fg = 250, 240, 230
    bg = 5, 5, 5
    wincolor = 40, 40, 90

	#load font, prepare values
    font = pygame.font.Font(None, 80)
    a_sys_font = pygame.font.SysFont("Arial",20)
    size = a_sys_font.size(text)
	#size = a_sys_font.size(text)

    #AA, transparancy, italic
    a_sys_font.set_italic(1)
    ren = a_sys_font.render(text, 1, bg)
    #screen.blit(ren, (30 + size[0], 40 + size[1]))
    screen.blit(ren, xyposition)
    a_sys_font.set_italic(0)

