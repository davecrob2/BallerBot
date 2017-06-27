# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:20:28 2017

@author: davecrob2
"""

import requests
import re
from string import ascii_lowercase
from bs4 import BeautifulSoup
#Iterates through alphabet to modify link to basketball reference pages

link_list = []
for a in ascii_lowercase:
    link = "http://www.basketball-reference.com/players/%(a)s/" % {"a":a}
    link_list.append(link)
#print(link_list)
try:
    for link in link_list:
        #print(page)
        
        #Variable to store basketball reference player glossary
        page = requests.get(link)
    
        #Using BS4 to parse page
        soup = BeautifulSoup(page.content,'html.parser')
        
        
        #Finds "tbody" tag which contains the enitre player table
        tbody=soup.find('tbody')
        #print(soup.find('tbody'))
        #print(tbody.prettify())
        
        #Finds "tr" tag in "tbody" tag
        tr=tbody.find('tr')
        
        #Finds "th" tag in "tr" tag with class "Left"
        th=tr.find('th',class_='left')
        
        #Finds "a" tag in "th" tag
        a=th.find('a')
        
        #Stores the player name
        name =a.get_text()
        print(name)
        
        #Stores the link portion to the player page
        player_link=a['href']
        #print(player_link)    
        
        
        #Splits the player_link for final extraction of player_id
        id_extract=player_link.split(player_link[10])
        id_split=id_extract[3]
        final_extract=id_split.split(id_split[-5])
        
        #Stores the entire player_id 
        player_id=final_extract[0]
        print(player_id)
        
        #PLayer dictionary where all player names and ids will eventually be stored
        player_dict={}
        player_dict[name]=id_extract
        #print(player_dict)
except AttributeError:
    print("There are no names here")


#Test code to find all links. Needs to be modified to only find player links
#for a in soup.find_all('a',href=True):
#    print("Found the URL:",a['href'])

