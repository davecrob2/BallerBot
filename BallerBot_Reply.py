# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 23:32:01 2017

@author: davecrob2
"""

import praw
import pdb
import re
import os

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
		if re.search("i love python",submission.title,re.IGNORECASE):
			#Reply to the post with text, eventually the statistics of the player
			submission.reply("Basketball is my favorite sport")
			print("Bot replying to: ", submission.title)
			#Store the current submission id into our list
			posts_replied_to.append(submission.id)
#Write our updated list back to the file
with open("posts_replied_to.txt","w") as f:
	for post_id in posts_replied_to:
		f.write(post_id + "\n")
