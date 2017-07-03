# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 23:32:01 2017

@author: davecrob2
"""

import praw
from player_scraper import bb_scrape
from string import ascii_lowercase
from widget_scraper import stat_scraper
import os

#Create the Reddit instance
reddit = praw.Reddit('ballerbot')

#Selects subreddit
subreddit = reddit.subreddit('nba')
#List to store each basketball reference link
link_list = []
#Dictionary to store all player names and IDs
all_players={}

#Establishing list to track comments
if not os.path.isfile("C:\\Users\davecrob2\\Documents\\GitHub\\BallerBot\\posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("C:\\Users\davecrob2\\Documents\\GitHub\\BallerBot\\posts_replied_to.txt","r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to=list(filter(None,posts_replied_to))


for a in ascii_lowercase:
    link = "http://www.basketball-reference.com/players/%(a)s/" % {"a":a}
    link_list.append(link)
#print(link_list)

#For loop to update player listing from Basketball Reference website
for link in link_list:
    try:
        all_players.update(bb_scrape(link))
    except AttributeError:
        continue
        #print("There are no names here")

#Code for replying to posts
for submission in subreddit.rising(limit=50):
    #print(list(submission.comments))
    for comment in submission.comments:
        #Checks that comments aren't replied to
        if comment.id not in posts_replied_to:
            for key in all_players:
                if key in comment.body:
                    #To extract first letter of last name
                    letter = all_players[key]
                    #BR Widget that we scrape for statistics
                    widget_link='https://widgets.sports-reference.com/wg.fcgi?site=bbr&url=/players/%(letter)s/%(id)s.html&div=div_per_game' % {"letter":letter[0],'id':all_players[key]}
                    #Replying to comments
                    comment.reply({key+""" 
                                             """ + stat_scraper(widget_link)})
                    posts_replied_to.append(comment.id)

#Writing comment ids to list                
with open("C:\\Users\davecrob2\\Documents\\GitHub\\BallerBot\\posts_replied_to.txt","w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
                

