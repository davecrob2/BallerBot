# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 23:32:01 2017

@author: davecrob2
"""

import praw
from player_scraper import bb_scrape
from string import ascii_lowercase



#Create the Reddit instance
reddit = praw.Reddit('ballerbot')

#Selects subreddit
subreddit = reddit.subreddit('pythonforengineers')
#List to store each basketball reference link
link_list = []

#Dictionary to store all player names and IDs
all_players={}

#
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
        print("There are no names here")


#Code for replying to posts
for submission in subreddit.hot(limit = 10):
    for top_level_comment in submission.comments:
        for key in all_players:
            if key in top_level_comment.body:
                #if top_level_comment.id not in replied_to:
                    top_level_comment.reply("It works!")
            #print("Bot replying to: ", submission.title)

