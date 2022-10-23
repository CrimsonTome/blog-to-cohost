# import cohost library
from cohost.models.user import User
from cohost.models.block import AttachmentBlock, MarkdownBlock


# import os.environ for environment variable management, sys for exiting upon exception and time.sleep to not overload cohost or your own site with requests
from os import environ
import sys
from time import sleep

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

for project in user.editedProjects:
    print(project) # Print all pages you have edit permissions for
# project = user.getProject('username') # will retrieve the page I have edit writes for with handle @vallerie
# blocks = [
#     AttachmentBlock('pybug.png'), # References image file pybug.png
#     MarkdownBlock('**Hello from Python!**') # Example of markdown / text block
# ]
# newPost = project.post('Title of python post!', blocks, tags=['cohost.py', 'python'])
# print('Check out your post at {}'.format(newPost.url))