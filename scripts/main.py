from cohost.models.user import User
from cohost.models.block import AttachmentBlock, MarkdownBlock

cookie = 'yourCookie'
user = User.loginWithCookie(cookie)
for project in user.editedProjects:
    print(project) # Print all pages you have edit permissions for
project = user.getProject('vallerie') # will retrieve the page I have edit writes for with handle @vallerie
blocks = [
    AttachmentBlock('pybug.png'), # References image file pybug.png
    MarkdownBlock('**Hello from Python!**') # Example of markdown / text block
]
newPost = project.post('Title of python post!', blocks, tags=['cohost.py', 'python'])
print('Check out your post at {}'.format(newPost.url))