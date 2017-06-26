# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 23:32:01 2017

@author: davecrob2
"""

import praw
import pdb
import csv

#Variables assigned to the playerlist file stored on computer
PlayersCsv="C:\\Users\\davecrob2\\Documents\\GitHub\\BallerBot\\PlayerList_A-C.csv"
#Opens PlayersCSV and reads .csv file
with open(PlayersCsv, mode='r') as infile:
    reader = csv.reader(infile)
    
    #iterates through rows to turn the list into an accesible python dictionary
    PlayerDict = {rows[0]:rows[1] for rows in reader}

#Create the Reddit instance
reddit = praw.Reddit('ballerbot')

#Get the top 5 hot posts from r/NBA
subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit = 5):
    for key in PlayerDict:
        if key in submission.title:
            submission.reply("""What is your favorite sport?|Basketball is my favorite sport 
                    :--:|:--
                    What is the best sport?|Basketball""")
            print("Bot replying to: ", submission.title)
