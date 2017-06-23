# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 23:33:01 2017

@author: davecrob2
"""

import praw

reddit = praw.Reddit('ballerbot')

subreddit = reddit.subreddit("learnpython")

#Read only top 5 posts on the "hot" filter"
for submission in subreddit.hot(limit=5):
	print("Title: ", submission.title)
	print("Text: ", submission.selftext)
	print("Score: ", submission.score)
	print("---------------------------------\n")
