# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 12:21:41 2017

@author: davecrob2
"""

import requests
from bs4 import BeautifulSoup

link="https://widgets.sports-reference.com/wg.fcgi?site=bbr&url=/players/a/allenra02.html&div=div_per_game"

def stat_scraper(widget_link):
    #Pulls in the widget page from Basketball Reference widget site
    widget_page = requests.get(widget_link)
    
    #Parses page using Beautiful Soup
    widget_soup = BeautifulSoup(widget_page.content,'html.parser')
    
    #List to store each season that a player has played
    season_list=[]
    
    #Scraping each season to return the year
    seasons = widget_soup.find_all('th',{"data-stat":"season"},class_='left')
    
    #For loop to append all years into a list
    for i in seasons:
        season_list.append(i.get_text())
    #print(season_list)   
    
    #Search of season_list to determine where Career total is. This helps us return the stats from the final season
    if "Career" in season_list:
        #print('found')
        #Tells us the index of the Career totals
        final_season =(season_list.index('Career'))
    
    
    #Variables storing different season stats. Scrapes page for individual stat categories
    games = widget_soup.find('td',{"data-stat":"ast_per_g"})
    mp=widget_soup.find('td',{"data-stat":"mp_per_g"})
    fg=widget_soup.find('td',{"data-stat":"fg_pct"})
    three_p=widget_soup.find('td',{"data-stat":"fg3_pct"})
    two_p=widget_soup.find_all('td',{"data-stat":"fg2_pct"})
    eFG=widget_soup.find('td',{"data-stat":"efg_pct"})
    FT=widget_soup.find('td',{"data-stat":"ft_pct"})
    TRB=widget_soup.find('td',{"data-stat":"trb_per_g"})
    AST=widget_soup.find('td',{"data-stat":"ast_per_g"})
    STL=widget_soup.find('td',{"data-stat":"stl_per_g"})
    BLK=widget_soup.find('td',{"data-stat":"blk_per_g"})
    TOV=widget_soup.find('td',{"data-stat":"tov_per_g"})
    PTS=widget_soup.find('td',{"data-stat":"pts_per_g"})
    
    #Returns us the text for the final season for the specified stat category
    print(two_p[final_season-1].get_text())
    return two_p[final_season-1].get_text()




#print(seasons)




#print(soup.prettify)