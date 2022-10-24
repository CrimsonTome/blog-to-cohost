# import cohost library
from cohost.models.user import User
from cohost.models.block import AttachmentBlock, MarkdownBlock

# import os.environ for environment variable management, sys for exiting upon exception, time.sleep to not overload cohost or your own site with requests and feedparser for fetching feeds
from os import environ
import sys
from time import sleep
import feedparser as fp

# get number of posts
try:  
   feedLength = environ.get("LENGTH")
except KeyError: 
   print ('Please set the environment variable LENGTH with export LENGTH="NUMBER-OF-POSTS"')
   sys.exit(1)

feedLength = int(feedLength) 
# print (feedLength)



# fetch and parse the feed
data = fp.parse("https://crimsontome.com/feed/feed.xml") # replace with your feed url

# extract title, url and date from most recent post (0)
title = data.entries[0].title
url = data.entries[0].link
date = data.entries[0].updated.split("T", 1)[0] # cut off date after yyyy-mm-dd - US date... 

# extract number of posts from the feed. this is used to compare our local value, to check if there has been a post since we last posted to cohost
postNum = len(data.entries)

# print (title, url, date, postNum)


# set cookie in with below line bwlow, you will have to run again when you reload your shell. to get around this run the line below that and then reload your shell
# export COOKIE="YOUR-TOKEN-HERE"
# echo 'export COOKIE="YOUR-TOKEN-HERE"' >> ~/.bashrc
# see https://github.com/valknight/Cohost.py#tokens for how to get your token

#  try import the cookie, tells the user to set it if it does not exist
try:
   cookie = environ.get("COOKIE")
except KeyError: 
   print ('Please set the environment variable COOKIE with export COOKIE="YOUR-TOKEN-HERE"')
   sys.exit(1)


# uncomment for testing purposes
# print(cookie)

#login
user = User.loginWithCookie(cookie)

# for project in user.editedProjects:
#     print(project) # Print all pages you have edit permissions for
project = user.getProject('crimsontome427') # replace with your project name
#if there's a new post on the blog and not on cohost already
if postNum > feedLength:
    blocks = [
        # AttachmentBlock('pybug.png'), # References image file pybug.png
        # fill in some post data
        MarkdownBlock("["+title+"]("+url+") Posted on: "+date)
    ]
    # post it!
    post = project.post("Blog post #"+str(feedLength),blocks)
    print('Check out your post at {}'.format(post.url))

    # increment the length and update the bashrc so *fingers crossed* it works more consistently
    feedLength+=1
    environ["LENGTH"] = str(feedLength)
    file1 = open("/home/ctome/.bashrc", "a")  # append mode, replace with your bashrc location
    file1.write('export LENGTH="'+str(feedLength)+'"')
    file1.close()