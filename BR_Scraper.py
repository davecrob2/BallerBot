# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:20:28 2017

@author: davecrob2
"""


from player_scraper import bb_scrape
from string import ascii_lowercase
#Iterates through alphabet to modify link to basketball reference pages

link_list = []
all_players={}
for a in ascii_lowercase:
    link = "http://www.basketball-reference.com/players/%(a)s/" % {"a":a}
    link_list.append(link)
#print(link_list)
try:
    for link in link_list:
        all_players.update(bb_scrape(link))
        
except AttributeError:
    print("There are no names here")
