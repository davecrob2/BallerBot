# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 16:12:13 2017

@author: davecrob2
"""
import requests
from bs4 import BeautifulSoup

#Function to scrape an individual basketball reference page and combine all player names and player ids into a dictionary.
#Accepts the url to the page as an argument
def bb_scrape(link):
    #Variable to store basketball reference player glossary
    page = requests.get(link)
    
    #Using BS4 to parse page
    soup = BeautifulSoup(page.content,'html.parser')
    
    
    #Finds "tbody" tag which contains the entire player table
    tbody=soup.find('tbody')
    #print(soup.find('tbody'))
    #print(tbody.prettify())
    
    #Finds "tr" tag in "tbody" tag
    tr=tbody.find_all('tr')
    fullnames=[]
    links = []
    zipper={}

    
    #Iterates through page to pull all names and player ids
    for i in tr:
        #print(tr.prettify())
        #Finds "th" tag in "tr" tag with class "Left"
        th=i.find('th',class_='left')
        #print(th)
        
        #Finds "a" tag in "th" tag
        a=th.find('a')
        #print(a)
        
        #Stores the player name
        name =a.get_text()
        #print(name)
        
        #Stores all full names in a list
        fullnames.append(name)
        
        player_link=a['href']
        #print(player_link)
        
        #Splits the player_link for final extraction of player_id
        id_extract=player_link.split(player_link[10])
        id_split=id_extract[3]
        final_extract=id_split.split(id_split[-5])
        
        #Stores the entire player_id 
        player_id=final_extract[0]
        
        #Stores player id in a list
        links.append(player_id)
        
        
    #print(fullnames)
    #print(links)
    
        #Combines two lists into dictionary
        zipper=dict(zip(fullnames,links))
    return zipper
