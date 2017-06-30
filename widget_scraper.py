# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 12:21:41 2017

@author: davecrob2
"""

import requests
from bs4 import BeautifulSoup



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
    
    final_season=0
    #Search of season_list to determine where Career total is. This helps us return the stats from the final season
    if "Career" in season_list:
        #print('found')
        #Tells us the index of the Career totals
        final_season=(season_list.index('Career'))
    
    
    #Variables storing different season stats. Scrapes page for individual stat categories
    games = widget_soup.find_all('td',{"data-stat":"g"})
    mp=widget_soup.find_all('td',{"data-stat":"mp_per_g"})
    fg=widget_soup.find_all('td',{"data-stat":"fg_pct"})
    three_p=widget_soup.find_all('td',{"data-stat":"fg3_pct"})
    two_p=widget_soup.find_all('td',{"data-stat":"fg2_pct"})
    eFG=widget_soup.find_all('td',{"data-stat":"efg_pct"})
    FT=widget_soup.find_all('td',{"data-stat":"ft_pct"})
    TRB=widget_soup.find_all('td',{"data-stat":"trb_per_g"})
    AST=widget_soup.find_all('td',{"data-stat":"ast_per_g"})
    STL=widget_soup.find_all('td',{"data-stat":"stl_per_g"})
    BLK=widget_soup.find_all('td',{"data-stat":"blk_per_g"})
    TOV=widget_soup.find_all('td',{"data-stat":"tov_per_g"})
    PTS=widget_soup.find_all('td',{"data-stat":"pts_per_g"})
    
    #Returns us the text for the final season for the specified stat category
    #print(PTS[final_season-1].get_text())
    #return PTS[final_season-1].get_text()

    return '''[Code](https://github.com/davecrob2/BallerBot) | r/BallerBot | [Feedback](https://np.reddit.com/message/compose/?to=BallerBot&subject=Feedback)

Games | MP | FG | 3P | 2P | eFG | FT | TRB | AST | STL | BLK | TOV | PTS
    - | - | - | - | - | - | - | - | - | - | - | - | -
    %(games)s | %(mp)s | %(fg)s | %(three_p)s | %(two_p)s | %(eFG)s | %(FT)s | %(TRB)s | %(AST)s | %(STL)s | %(BLK)s | %(TOV)s | %(PTS)s''' % {'games':games[final_season-1].get_text(),'mp':mp[final_season-1].get_text(),'fg':fg[final_season-1].get_text(),'three_p':three_p[final_season-1].get_text(),'two_p':two_p[final_season-1].get_text(),'eFG':eFG[final_season-1].get_text(),'FT':FT[final_season-1].get_text(),'TRB':TRB[final_season-1].get_text(),'AST':AST[final_season-1].get_text(),'STL':STL[final_season-1].get_text(),'BLK':BLK[final_season-1].get_text(),'TOV':TOV[final_season-1].get_text(),'PTS':PTS[final_season-1].get_text()} 
#print(seasons)




#print(soup.prettify)