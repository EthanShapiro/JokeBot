import praw
from bs4 import BeautifulSoup
from requests import request

reddit = praw.Reddit(client_id='ctN1jTBggiKifA',
                     client_secret='dt6assMNm5pMfLM-cmU0dHt5Hcw',
                     user_agent='jokebot')
# Get top 100 jokes at the time
submissions = reddit.subreddit('jokes').hot(100)

