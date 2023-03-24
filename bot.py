import praw
import time

# Initialize the Reddit API client
reddit = praw.Reddit(client_id='',
        client_secret='',
        username='',
        password='',
        user_agent='')

# Choose the subreddit where you want to post the message
subreddit = reddit.subreddit('subreddit')

# Read the contents of the message file.
with open('./message.txt', 'r') as f:
    message_template = f.read()
    posted_count = 0

placeholder = 'example'
placeholder_list = ['example 1',
        'example 2',
        'example 3',
        'example 4',
        'example 5']

for p in placeholder_list:
        message = message_template.replace("[PLACEHOLDER]", p)
        posted_count = posted_count + 1
        print(str(posted_count) + "). " + p + " was posted.")
        # title for your post, selftext is the message change the message in message.txt
        subreddit.submit(title=p + 'xyz title', selftext=message)
        # Pause for 5 minutes (300 seconds) before posting the next message
        time.sleep(60)
