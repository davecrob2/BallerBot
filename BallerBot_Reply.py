# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 23:32:01 2017

@author: davecrob2
"""

import praw
import pdb
import re
import os
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

#Creates an empty list or loads list of posts we have replied to and removes empty values

if not os.path.isfile("posts_replied_to.txt"):
	posts_replied_to = []
else:
	with open("posts_replied_to.txt", "r") as f:
		posts_replied_to = f.read()
		posts_replied_to = posts_replied_to.split("\n")
		posts_replied_to = list(filter(None, posts_replied_to))

#Get the top 5 hot posts from r/NBA
subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit = 5):
	#If we haven't replied to this post
	if submission.id not in posts_replied_to:
		#Search for keywords in the specified field, in this case: Title
		for key in PlayerDict:
			if key in submission.title:#Reply to the post with text, eventually the statistics of the player
			     submission.reply("""What is your favorite sport?|Basketball is my favorite sport 
                    :--:|:--
                    What is the best sport?|Basketball""")
			     print("Bot replying to: ", submission.title)
			#Store the current submission id into our list
			     posts_replied_to.append(submission.id)
#Write our updated list back to the file
with open("posts_replied_to.txt","w") as f:
	for post_id in posts_replied_to:
		f.write(post_id + "\n")